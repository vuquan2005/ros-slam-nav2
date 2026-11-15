"""Read a generic SDL joystick and send differential-drive velocity commands."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    bringup = get_package_share_directory('dif_bringup')
    config = LaunchConfiguration('config_file')
    return LaunchDescription([
        DeclareLaunchArgument('config_file', default_value=os.path.join(
            bringup, 'config', 'joy.yaml')),
        DeclareLaunchArgument('device_id', default_value='0'),
        DeclareLaunchArgument('start_joy', default_value='true', choices=['true', 'false'],
                             description='Read a physical controller; false uses an external /joy publisher'),
        DeclareLaunchArgument('cmd_vel', default_value='/cmd_vel'),
        Node(
            package='joy', executable='joy_node', name='joy_node',
            parameters=[config, {'device_id': ParameterValue(
                LaunchConfiguration('device_id'), value_type=int)}],
            output='screen', condition=IfCondition(LaunchConfiguration('start_joy')),
        ),
        Node(
            package='teleop_twist_joy', executable='teleop_node',
            name='teleop_twist_joy_node', parameters=[config], output='screen',
            remappings=[('cmd_vel', LaunchConfiguration('cmd_vel'))],
        ),
    ])
