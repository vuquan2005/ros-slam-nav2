"""Check model and integration contracts without starting a ROS graph."""

import ast
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import xacro
import yaml


ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / 'src/dif_description/urdf/dif.urdf.xacro'


class WorkspaceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sim = ET.fromstring(xacro.process_file(
            str(MODEL), mappings={'simulation': 'true'}).toxml())
        cls.display = ET.fromstring(xacro.process_file(
            str(MODEL), mappings={'simulation': 'false'}).toxml())

    def test_connected_tf_tree(self):
        links = {link.attrib['name'] for link in self.sim.findall('link')}
        children = set()
        parents = {}
        for joint in self.sim.findall('joint'):
            parent = joint.find('parent').attrib['link']
            child = joint.find('child').attrib['link']
            self.assertIn(parent, links)
            self.assertIn(child, links)
            self.assertNotIn(child, children)
            children.add(child)
            parents[child] = parent
        self.assertEqual(links - children, {'base_footprint'})
        for link in links:
            seen = set()
            while link in parents:
                self.assertNotIn(link, seen, 'TF cycle')
                seen.add(link)
                link = parents[link]
            self.assertEqual(link, 'base_footprint')

    def test_physical_model(self):
        for link in self.sim.findall('link'):
            inertial = link.find('inertial')
            if link.attrib['name'] == 'base_footprint':
                continue
            self.assertIsNotNone(inertial, link.attrib['name'])
            self.assertGreater(float(inertial.find('mass').attrib['value']), 0)
            tensor = inertial.find('inertia').attrib
            diagonal = [float(tensor[name]) for name in ('ixx', 'iyy', 'izz')]
            for value in diagonal:
                self.assertGreater(value, 0)
                self.assertLessEqual(2 * value, sum(diagonal) + 1e-10)
            self.assertTrue(all(float(tensor[k]) == 0 for k in ('ixy', 'ixz', 'iyz')))

    def test_drive_geometry_matches_joints(self):
        drive = self.sim.find("gazebo/plugin[@name='ignition::gazebo::systems::DiffDrive']")
        joints = {j.attrib['name']: j for j in self.sim.findall('joint')}
        active = {name for name, joint in joints.items()
                  if joint.attrib['type'] == 'continuous'}
        self.assertEqual(active, {'left_wheel_joint', 'right_wheel_joint'})
        left = joints[drive.findtext('left_joint')]
        right = joints[drive.findtext('right_joint')]
        ly = float(left.find('origin').attrib['xyz'].split()[1])
        ry = float(right.find('origin').attrib['xyz'].split()[1])
        self.assertGreater(ly, 0)
        self.assertLess(ry, 0)
        self.assertAlmostEqual(ly - ry, float(drive.findtext('wheel_separation')))
        for joint in (left, right):
            self.assertEqual(joint.find('axis').attrib['xyz'], '0 1 0')
            child = joint.find('child').attrib['link']
            cylinder = self.sim.find(f"link[@name='{child}']/collision/geometry/cylinder")
            self.assertAlmostEqual(float(cylinder.attrib['radius']),
                                   float(drive.findtext('wheel_radius')))
        self.assertEqual(drive.findtext('frame_id'), 'odom')
        self.assertEqual(drive.findtext('child_frame_id'), 'base_footprint')

    def test_lidar_and_bridge_contract(self):
        bridges = yaml.safe_load((ROOT / 'src/dif_gazebo/config/bridge.yaml').read_text())
        by_topic = {b['ros_topic_name']: b for b in bridges}
        self.assertEqual(set(by_topic), {'/clock', '/cmd_vel', '/odom', '/tf', '/joint_states', '/scan'})
        for topic, bridge in by_topic.items():
            self.assertEqual(bridge['gz_topic_name'], topic)
            self.assertEqual(bridge['direction'], 'ROS_TO_GZ' if topic == '/cmd_vel' else 'GZ_TO_ROS')
        self.assertEqual(by_topic['/scan']['ros_type_name'], 'sensor_msgs/msg/LaserScan')
        sensor = self.sim.find("gazebo[@reference='laser_frame']/sensor")
        self.assertEqual(sensor.findtext('topic'), '/scan')
        self.assertEqual(sensor.findtext('ignition_frame_id'), 'laser_frame')
        self.assertIsNotNone(self.sim.find("link[@name='laser_frame']"))
        self.assertIsNone(self.display.find('gazebo/plugin'))
        self.assertIsNone(self.display.find('gazebo/sensor'))

    def test_world_and_package_dependencies(self):
        world = ET.parse(ROOT / 'src/dif_gazebo/worlds/room.sdf').find('world')
        self.assertEqual(world.attrib['name'], 'default')
        self.assertIn('ignition::gazebo::systems::Sensors',
                      {p.attrib['name'] for p in world.findall('plugin')})
        packages = {}
        for path in (ROOT / 'src').glob('*/package.xml'):
            manifest = ET.parse(path)
            packages[manifest.findtext('name')] = manifest
        self.assertEqual(set(packages), {'dif_description', 'dif_gazebo', 'dif_bringup'})
        for manifest in packages.values():
            for dependency in manifest.findall('exec_depend'):
                if dependency.text.startswith('dif_'):
                    self.assertIn(dependency.text, packages)

    def test_launch_and_config_syntax(self):
        for path in (ROOT / 'src').rglob('*.py'):
            ast.parse(path.read_text(), filename=str(path))
        for path in (ROOT / 'src').rglob('*.rviz'):
            yaml.safe_load(path.read_text())
        for path in [ROOT / '.devcontainer/devcontainer.json', ROOT / '.vscode/tasks.json']:
            json.loads(path.read_text())


if __name__ == '__main__':
    unittest.main()
