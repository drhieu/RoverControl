"""
        Rover Localization Launch For Rover Robotics - Will Aug 12 2020
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
            name='nav_map_server',
            package='nav2_map_server',
            executable='map_server',
            #output='screen',
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_amcl',
            package='nav2_amcl',
            executable='amcl',
            #output={'both': 'log'},
            parameters=[config_filepath],
            remappings=remappings),

        Node(
            name='nav_lifecycle_manager_localization',
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            output={'both': 'log'},
            parameters=[config_filepath]),
            # parameters=[{'use_sim_time': use_sim_time},
            #             {'autostart': autostart},
            #             {'node_names': lifecycle_nodes}])
    ])
