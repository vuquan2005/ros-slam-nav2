"""Inspect the URDF without starting Gazebo."""
import os
import shlex

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    description = get_package_share_directory('dif_description')
    return LaunchDescription([
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': ParameterValue(Command([
                 FindExecutable(name='xacro'), ' ',
                 shlex.quote(os.path.join(description, 'urdf', 'dif.urdf.xacro')),
             ]), value_type=str)}]),
        Node(package='joint_state_publisher', executable='joint_state_publisher'),
        Node(package='rviz2', executable='rviz2', arguments=[
            '-d', os.path.join(description, 'rviz', 'display.rviz'),
        ]),
    ])
