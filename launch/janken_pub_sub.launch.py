import launch
import launch.actions
import launch.substitutions
import launch_ros.actions



def generate_launch_description():
      janken_publisher = launch_ros.actions.Node(
              package='mypkg',
              executable='janken_publisher',
              output='screen'
              )
      janken_subscriber = launch_ros.actions.Node(
              package='mypkg',
              executable='janken_subscriber',
              output='screen'
              )
      return launch.LaunchDescription([janken_publisher, janken_subscriber])
