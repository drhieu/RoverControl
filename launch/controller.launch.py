"""
        RoverControl Launch For Rover Robotics - Will Aug 12 2020
"""
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    #controller config path;
    config_filepath = Path(get_package_share_directory('rovercontrol'), 'config', 'config.yaml').resolve() 
    assert config_filepath.is_file() 

    return LaunchDescription([
        Node(
            package='joy', executable='joy_node', name='joy_node',
            ),#parameters=[config_filepath]),
        Node(
            package='rovercontrol', executable='rovercontrol_node',
            name='rovercontrol_node', parameters=[config_filepath]),
    ])
