import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, DeclareLaunchArgument
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    
    move_arg = DeclareLaunchArgument('is_spiral', default_value='false', description='True if spiral movement, false if circular movement')
    move_config = LaunchConfiguration('is_spiral')
    # include launch file of turtlebot3 simulation
    turtlebot3_simulation_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('module_2_assignment'), 'launch'), 
            '/turtlebot_world.launch.py'])
    )
    
    bot_name1 = 'turtlebot1'
    bot_name2 = 'turtlebot2'
    bot_name3 = 'turtlebot3'
    bot_name4 = 'turtlebot4'
    bot_name5 = 'turtlebot5'
    
    spiral_move_node1 = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/'+bot_name1+'/cmd_vel'},       
        ],
        condition=IfCondition(move_config)
    )
    
    spiral_move_node2 = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/'+bot_name2+'/cmd_vel'},       
        ],
        condition=IfCondition(move_config)
    )
    spiral_move_node3 = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/'+bot_name3+'/cmd_vel'},       
        ],
        condition=IfCondition(move_config)
    )
    spiral_move_node4 = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/'+bot_name4+'/cmd_vel'},       
        ],
        condition=IfCondition(move_config)
    )
    spiral_move_node5 = Node(
        package='module_2_assignment',
        executable='move_spiral',
        name='spiral_move_node',
        parameters=[
            {'cmd_vel_topic': '/'+bot_name5+'/cmd_vel'},       
        ],
        condition=IfCondition(move_config)
    )
    
    circle_move_node1 = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        namespace=bot_name1,
        parameters=[
            {'cmd_vel_topic': '/'+bot_name1+'/cmd_vel'},       
        ],
        condition=UnlessCondition(move_config)
    )
    
    circle_move_node2 = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        namespace=bot_name2,
        parameters=[
            {'cmd_vel_topic': '/'+bot_name2+'/cmd_vel'},       
        ],
        condition=UnlessCondition(move_config)
    )
    
    circle_move_node3 = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        namespace=bot_name3,
        parameters=[
            {'cmd_vel_topic': '/'+bot_name3+'/cmd_vel'},       
        ],
        condition=UnlessCondition(move_config)
    )
    
    circle_move_node4 = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        namespace=bot_name4,
        parameters=[
            {'cmd_vel_topic': '/'+bot_name4+'/cmd_vel'},       
        ],
        condition=UnlessCondition(move_config)
    )
    
    circle_move_node5 = Node(
        package='module_2_assignment',
        executable='move_circle',
        name='circle_move_node',
        namespace=bot_name5,
        parameters=[
            {'cmd_vel_topic': '/'+bot_name5+'/cmd_vel'},       
        ],
        condition=UnlessCondition(move_config)
    )
    
    return LaunchDescription([
        move_arg,
        turtlebot3_simulation_node,
        spiral_move_node1,
        spiral_move_node2,
        spiral_move_node3,
        spiral_move_node4,
        spiral_move_node5,
        circle_move_node1,
        circle_move_node2,
        circle_move_node3,
        circle_move_node4,
        circle_move_node5,
    ])