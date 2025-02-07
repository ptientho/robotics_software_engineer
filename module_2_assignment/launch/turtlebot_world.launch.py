#!/usr/bin/env python3
#
# Copyright 2019 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Joep Tool

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    model_folder = 'turtlebot3_waffle_pi'
    #launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    robot_desc_path = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'urdf', model_folder + '.urdf')
    world = os.path.join(
        get_package_share_directory('turtlebot3_gazebo'),
        'worlds',
        'empty_workd.world'
    )
    urdf = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'models', model_folder, 'model.sdf')
    with open(robot_desc_path, 'r') as infp:
        robot_desc = infp.read()

    bot_name1 = 'turtlebot1'
    bot_name2 = 'turtlebot2'
    bot_name3 = 'turtlebot3'
    bot_name4 = 'turtlebot4'
    bot_name5 = 'turtlebot5'
    # Robot 1
    spawn_robot1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', bot_name1,
            '-file', urdf,
            '-x', '0',
            '-y', '0',
            '-z', '0.01',
            '-robot_namespace', bot_name1,
        ],
        output='screen'
    )
    robot_state_publisher1 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=bot_name1,
        output='screen',
        parameters=[{'robot_description': robot_desc,
                     'use_sim_time': use_sim_time,
                     'frame_prefix': bot_name1 + '/'}],
    )
    # Robot 2
    spawn_robot2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', bot_name2,
            '-file', urdf,
            '-x', '2',
            '-y', '2',
            '-z', '0.01',
            '-robot_namespace', bot_name2,
        ],
        output='screen'
    )
    robot_state_publisher2 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=bot_name2,
        output='screen',
        parameters=[{'robot_description': robot_desc,
                     'use_sim_time': use_sim_time,
                     'frame_prefix': bot_name2 + '/'}],
    )
    # Robot 3
    spawn_robot3 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', bot_name3,
            '-file', urdf,
            '-x', '4',
            '-y', '4',
            '-z', '0.01',
            '-robot_namespace', bot_name3,
        ],
        output='screen'
    )
    robot_state_publisher3 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=bot_name3,
        output='screen',
        parameters=[{'robot_description': robot_desc,
                     'use_sim_time': use_sim_time,
                     'frame_prefix': bot_name3 + '/'}],
    )
    # Robot 4
    spawn_robot4 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', bot_name4,
            '-file', urdf,
            '-x', '6',
            '-y', '6',
            '-z', '0.01',
            '-robot_namespace', bot_name4,
        ],
        output='screen'
    )
    robot_state_publisher4 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=bot_name4,
        output='screen',
        parameters=[{'robot_description': robot_desc,
                     'use_sim_time': use_sim_time,
                     'frame_prefix': bot_name4 + '/'}],
    )
    # Robot 5
    spawn_robot5 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', bot_name5,
            '-file', urdf,
            '-x', '8',
            '-y', '8',
            '-z', '0.01',
            '-robot_namespace', bot_name5,
        ],
        output='screen'
    )
    robot_state_publisher5 = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=bot_name5,
        output='screen',
        parameters=[{'robot_description': robot_desc,
                     'use_sim_time': use_sim_time,
                     'frame_prefix': bot_name5 + '/'}],
    )
    
    # Gazebo launch
    gzserver_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    gzclient_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
        )
    )


    ld = LaunchDescription()

    # Add the commands to the launch description
    ld.add_action(gzserver_cmd)
    ld.add_action(gzclient_cmd)
    ld.add_action(spawn_robot1)
    ld.add_action(robot_state_publisher1)
    ld.add_action(spawn_robot2)
    ld.add_action(robot_state_publisher2)
    ld.add_action(spawn_robot3)
    ld.add_action(robot_state_publisher3)
    ld.add_action(spawn_robot4)
    ld.add_action(robot_state_publisher4)
    ld.add_action(spawn_robot5)
    ld.add_action(robot_state_publisher5)
    

    return ld
