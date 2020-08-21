"""
	Launch for Navigation with Rover Robotics' Robot - Will Aug 12 2020
"""
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

#Pull from different packages
#bringup_dir = get_package_share_directory('nav2_bringup')
#launch_dir = os.path.join(bringup_dir, 'launch')
def generate_launch_description():
    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED', '1'),
		#Launch from Same Package
		#Launch Rviz
		IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/rviz.launch.py'])),
    	#Launch SLAM
		#TODO
		#Launch Controller
		IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/controller.launch.py'])),
		#Launch Localization
		#IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/localization.launch.py'])),
		#Launch Navigation
    	#IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/navigation.launch.py'])),
		#Launch SLAM
		#IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/slam.launch.py'])),


		#Pull from different packages
		#IncludeLaunchDescription(
        #    PythonLaunchDescriptionSource(os.path.join(launch_dir,
        #                                               'bringup_launch.py')),
        #    launch_arguments={
        #                      'map': "/home/ros/willmap.yaml"}.items()),
        #IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(launch_dir, 'localization_launch.py')),
    ])


