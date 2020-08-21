"""
        Rover Navigation Launch For Rover Robotics - Will Aug 12 2020
"""
from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import SetEnvironmentVariable, DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    lifecycle_nodes = ['nav_controller_server',
                       'nav_planner_server',
                       'nav_recoveries_server',
                       'nav_bt_navigator',
                       'nav_waypoint_follower']

    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    #controller config path;
    config_filepath = Path(get_package_share_directory('rovercontrol'), 'config', 'config.yaml').resolve() 
    assert config_filepath.is_file()

    return LaunchDescription([
        Node(
            name="slam_toolbox",
            package='slam_toolbox',
            executable='sync_slam_toolbox_node', 
            output='screen',
            parameters=[config_filepath]),
        Node(
            name="nav_map_saver",
            package='nav2_map_server',
            executable='map_saver_server',
            output='screen',
            parameters=[config_filepath]),

        Node(
            name='nav_lifecycle_manager_slam',
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            output='screen',
            parameters=[config_filepath])

    ])




