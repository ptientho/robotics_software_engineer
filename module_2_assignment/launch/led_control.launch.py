from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='module_2_assignment',
            executable='led_control',
            name='led_publisher',
        ),
        Node(
            package='module_2_assignment',
            executable='led_receiver',
            name='led_subscriber',
        ),
    ])
