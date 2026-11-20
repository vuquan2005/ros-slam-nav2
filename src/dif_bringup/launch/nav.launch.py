"""Navigate in Gazebo while SLAM Toolbox builds the map."""
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
    nav2 = get_package_share_directory('nav2_bringup')
    slam_arguments = {
        'gui': 'true',
        'gui_config': '',
        'rviz': 'true',
        'rviz_config': os.path.join(description, 'rviz', 'nav.rviz'),
        'world': os.path.join(gazebo, 'worlds', 'room.sdf'),
        'slam_params_file': os.path.join(bringup, 'config', 'slam.yaml'),
    }

    return LaunchDescription([
        *[DeclareLaunchArgument(name, default_value=default)
          for name, default in slam_arguments.items()],
        DeclareLaunchArgument('nav2_params_file', default_value=os.path.join(
            bringup, 'config', 'nav2.yaml')),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(bringup, 'launch', 'slam.launch.py')),
            launch_arguments={name: LaunchConfiguration(name) for name in slam_arguments}.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nav2, 'launch', 'navigation_launch.py')),
            launch_arguments={
                'use_sim_time': 'true',
                'params_file': LaunchConfiguration('nav2_params_file'),
            }.items(),
        ),
    ])
