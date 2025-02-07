import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    
    # include launch file of turtlebot3 simulation
    turtlebot3_simulation_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('turtlebot3_gazebo'), 'launch'), 
            '/turtlebot3_world.launch.py'])
    )
    
    circle_move_node = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        parameters=[
            {'cmd_vel_topic': '/cmd_vel'},       
        ]
    )
    
    spiral_move_node = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/cmd_vel'},       
        ]
    )
    
    return LaunchDescription([
        turtlebot3_simulation_node,
        #circle_move_node,
        spiral_move_node,
    ])