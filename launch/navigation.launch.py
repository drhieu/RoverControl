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

    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    #controller config path;
    config_filepath = Path(get_package_share_directory('rovercontrol'), 'config', 'config.yaml').resolve() 
    assert config_filepath.is_file()

    return LaunchDescription([
        Node(
            name= "nav_controller_server",
            package='nav2_controller',
            executable='controller_server',
            output={'both': 'log'},
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_planner_server',
            package='nav2_planner',
            executable='planner_server',
            output='screen',
            namespace= "/",
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_recoveries_server',
            package='nav2_recoveries',
            executable='recoveries_server',
            output='screen',
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_bt_navigator',
            package='nav2_bt_navigator',
            executable='bt_navigator',
            output='screen',
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_waypoint_follower',
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            output='screen',
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name="nav_lifecycle_manager_navigation",
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            output='screen',
            parameters=[config_filepath]),
    ])
