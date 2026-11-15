"""Gazebo Fortress simulation with differential drive and a 2D LiDAR."""
import os
import shlex

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, EmitEvent, OpaqueFunction
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    description = get_package_share_directory('dif_description')
    gazebo = get_package_share_directory('dif_gazebo')
    ros_gz = get_package_share_directory('ros_gz_sim')
    world = LaunchConfiguration('world')
    gui = LaunchConfiguration('gui')
    rviz = LaunchConfiguration('rviz')

    def launch_gazebo(context):
        args = ['-r']
        if gui.perform(context) == 'false':
            args.append('-s')
        gui_config = LaunchConfiguration('gui_config').perform(context)
        if gui_config and gui.perform(context) == 'true':
            config_path = os.path.abspath(os.path.expanduser(gui_config))
            if not os.path.isfile(config_path):
                raise FileNotFoundError(f'Gazebo GUI config does not exist: {config_path}')
            args.extend(['--gui-config', config_path])
        args.append(world.perform(context))
        return [IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(ros_gz, 'launch', 'gz_sim.launch.py')),
            launch_arguments={'gz_args': shlex.join(args), 'on_exit_shutdown': 'true'}.items(),
        )]

    spawn = Node(
        package='ros_gz_sim', executable='create', output='screen',
        arguments=['-world', 'default', '-topic', 'robot_description',
                   '-name', 'dif', '-allow_renaming', 'false', '-z', '0.03'],
    )

    def after_spawn(event, context):
        # Fail visibly if creation failed instead of leaving an empty simulation.
        if event.returncode != 0:
            return [EmitEvent(event=Shutdown(reason='Failed to spawn dif robot'))]
        return []

    return LaunchDescription([
        DeclareLaunchArgument('world', default_value=os.path.join(gazebo, 'worlds', 'room.sdf'),
                              description='SDF world with world name default'),
        DeclareLaunchArgument('gui', default_value='true', choices=['true', 'false']),
        DeclareLaunchArgument('gui_config', default_value='',
                             description='Gazebo GUI config path; empty uses Gazebo defaults'),
        DeclareLaunchArgument('rviz', default_value='true', choices=['true', 'false']),
        DeclareLaunchArgument('rviz_config', default_value=os.path.join(
            description, 'rviz', 'dif.rviz')),
        Node(
            package='robot_state_publisher', executable='robot_state_publisher',
            parameters=[{'use_sim_time': True, 'robot_description': ParameterValue(
                Command([FindExecutable(name='xacro'), ' ',
                         os.path.join(description, 'urdf', 'dif.urdf.xacro'),
                         ' simulation:=true']), value_type=str)}],
            output='screen',
        ),
        OpaqueFunction(function=launch_gazebo),
        Node(
            package='ros_gz_bridge', executable='parameter_bridge', output='screen',
            parameters=[{'use_sim_time': True,
                         'config_file': os.path.join(gazebo, 'config', 'bridge.yaml')}],
        ),
        RegisterEventHandler(OnProcessExit(target_action=spawn, on_exit=after_spawn)),
        # ros_gz_sim create waits for the world service and robot_description.
        spawn,
        Node(
            package='rviz2', executable='rviz2', output='screen',
            arguments=['-d', LaunchConfiguration('rviz_config')],
            parameters=[{'use_sim_time': True}], condition=IfCondition(rviz),
        ),
    ])
