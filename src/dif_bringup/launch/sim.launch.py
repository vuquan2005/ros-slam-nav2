"""Gazebo Fortress simulation with differential drive and a 2D LiDAR."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, EmitEvent
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    description = get_package_share_directory('dif_description')
    gazebo = get_package_share_directory('dif_gazebo')
    ros_gz = get_package_share_directory('ros_gz_sim')
    world = LaunchConfiguration('world')
    gui = LaunchConfiguration('gui')
    rviz = LaunchConfiguration('rviz')

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
        DeclareLaunchArgument('rviz', default_value='true', choices=['true', 'false']),
        Node(
            package='robot_state_publisher', executable='robot_state_publisher',
            parameters=[{'use_sim_time': True, 'robot_description': ParameterValue(
                Command([FindExecutable(name='xacro'), ' ',
                         os.path.join(description, 'urdf', 'dif.urdf.xacro'),
                         ' simulation:=true']), value_type=str)}],
            output='screen',
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(ros_gz, 'launch', 'gz_sim.launch.py')),
            launch_arguments={'gz_args': [PythonExpression([
                "'-r ' if '", gui, "' == 'true' else '-r -s '"
            ]), world], 'on_exit_shutdown': 'true'}.items(),
        ),
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
            arguments=['-d', os.path.join(description, 'rviz', 'dif.rviz')],
            parameters=[{'use_sim_time': True}], condition=IfCondition(rviz),
        ),
    ])
