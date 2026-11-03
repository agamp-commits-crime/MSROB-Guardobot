import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, ExecuteProcess,
                            IncludeLaunchDescription, SetEnvironmentVariable,
                            TimerAction)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    pkg = get_package_share_directory('teambot_bringup')
    tb4_gz = get_package_share_directory('turtlebot4_gz_bringup')
    tb4_viz = get_package_share_directory('turtlebot4_viz')
    ros_share = os.path.dirname(get_package_share_directory('turtlebot4_description'))

    world = os.path.join(pkg, 'worlds', 'museum_world.sdf')
    resource_path = ':'.join([
        os.path.join(pkg, 'models'),
        os.path.join(pkg, 'models', 'exhibits'),
        ros_share,
    ])

    spawn = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(tb4_gz, 'launch', 'turtlebot4_spawn.launch.py')),
        launch_arguments={
            'world': 'museum_world',
            'namespace': LaunchConfiguration('namespace'),
            'use_sim_time': LaunchConfiguration('use_sim_time'),
            'model': LaunchConfiguration('model'),
            'x': LaunchConfiguration('x'),
            'y': LaunchConfiguration('y'),
            'z': LaunchConfiguration('z'),
            'yaw': LaunchConfiguration('yaw'),
            'rviz': 'false',
        }.items())

    rviz = Node(
        package='rviz2', executable='rviz2', output='screen',
        arguments=['-d', os.path.join(pkg, 'rviz', 'teambot.rviz')],
        parameters=[{'use_sim_time': True}],
        condition=IfCondition(LaunchConfiguration('rviz')))

    return LaunchDescription([
        DeclareLaunchArgument('namespace', default_value=''),
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        DeclareLaunchArgument('model', default_value='standard'),
        DeclareLaunchArgument('x', default_value='3.59'),
        DeclareLaunchArgument('y', default_value='-1.78'),
        DeclareLaunchArgument('z', default_value='0.0'),
        DeclareLaunchArgument('yaw', default_value='0.0'),
        DeclareLaunchArgument('rviz', default_value='true'),
        DeclareLaunchArgument('teleop', default_value='true'),
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', resource_path),
        ExecuteProcess(cmd=['gz', 'sim', '-r', world], output='screen'),
        Node(package='ros_gz_bridge', executable='parameter_bridge',
             name='clock_bridge', output='screen',
             arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock']),
        TimerAction(period=5.0, actions=[spawn]),
        TimerAction(period=10.0, actions=[rviz]),
        TimerAction(period=12.0, actions=[ExecuteProcess(
            cmd=['gnome-terminal', '--', 'bash', '-c',
                 'ros2 run teleop_twist_keyboard teleop_twist_keyboard '
                 '--ros-args -p stamped:=true; exec bash'],
            condition=IfCondition(LaunchConfiguration('teleop')))]),
    ])
