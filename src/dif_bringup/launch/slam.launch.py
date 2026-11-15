"""Start the simulation and build a map with asynchronous SLAM Toolbox."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    bringup = get_package_share_directory('dif_bringup')
    description = get_package_share_directory('dif_description')
    gazebo = get_package_share_directory('dif_gazebo')
    toolbox = get_package_share_directory('slam_toolbox')
    return LaunchDescription([
        DeclareLaunchArgument('gui', default_value='true', choices=['true', 'false']),
        DeclareLaunchArgument('gui_config', default_value='',
                             description='Gazebo GUI config path; empty uses Gazebo defaults'),
        DeclareLaunchArgument('rviz', default_value='true', choices=['true', 'false']),
        DeclareLaunchArgument('world', default_value=os.path.join(gazebo, 'worlds', 'room.sdf')),
        DeclareLaunchArgument('slam_params_file', default_value=os.path.join(
            bringup, 'config', 'slam.yaml')),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(bringup, 'launch', 'sim.launch.py')),
            launch_arguments={
                'gui': LaunchConfiguration('gui'),
                'gui_config': LaunchConfiguration('gui_config'),
                'rviz': LaunchConfiguration('rviz'),
                'world': LaunchConfiguration('world'),
                'rviz_config': os.path.join(description, 'rviz', 'slam.rviz'),
            }.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(toolbox, 'launch', 'online_async_launch.py')),
            launch_arguments={
                'use_sim_time': 'true',
                'slam_params_file': LaunchConfiguration('slam_params_file'),
            }.items(),
        ),
    ])
