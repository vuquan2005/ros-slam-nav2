"""Navigate in Gazebo while SLAM Toolbox builds the map."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.descriptions import ParameterFile


def generate_launch_description():
    bringup = get_package_share_directory('dif_bringup')
    description = get_package_share_directory('dif_description')
    gazebo = get_package_share_directory('dif_gazebo')
    slam_arguments = {
        'gui': 'true',
        'gui_config': '',
        'rviz': 'true',
        'rviz_config': os.path.join(description, 'rviz', 'nav.rviz'),
        'world': os.path.join(gazebo, 'worlds', 'room.sdf'),
        'slam_params_file': os.path.join(bringup, 'config', 'slam.yaml'),
    }
    params = ParameterFile(LaunchConfiguration('nav2_params_file'), allow_substs=True)
    velocity_input = [('cmd_vel', 'cmd_vel_nav')]
    servers = [
        ('nav2_controller', 'controller_server', velocity_input),
        ('nav2_planner', 'planner_server', []),
        ('nav2_behaviors', 'behavior_server', velocity_input),
        ('nav2_velocity_smoother', 'velocity_smoother',
         velocity_input + [('cmd_vel_smoothed', 'cmd_vel')]),
        ('nav2_bt_navigator', 'bt_navigator', []),
    ]

    return LaunchDescription([
        *[DeclareLaunchArgument(name, default_value=default)
          for name, default in slam_arguments.items()],
        DeclareLaunchArgument('nav2_params_file', default_value=os.path.join(
            bringup, 'config', 'nav2.yaml')),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(bringup, 'launch', 'slam.launch.py')),
            launch_arguments={name: LaunchConfiguration(name) for name in slam_arguments}.items(),
        ),
        *[Node(package=package, executable=name, name=name, output='screen',
               parameters=[params, {'use_sim_time': True}], remappings=remappings)
          for package, name, remappings in servers],
        Node(
            package='nav2_lifecycle_manager', executable='lifecycle_manager',
            name='lifecycle_manager_navigation', output='screen',
            parameters=[{'use_sim_time': True, 'autostart': True,
                         'node_names': [name for _, name, _ in servers]}],
        ),
    ])
