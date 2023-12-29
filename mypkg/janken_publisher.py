# パブリッシャーノード (janken_publisher.py)

import rclpy
from rclpy.node import Node
import random

from std_msgs.msg import String

class JankenPublisher(Node):

    def __init__(self):
        super().__init__('janken_publisher')
        self.publisher_ = self.create_publisher(String, 'janken_topic', 10)
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.publish_janken)

    def publish_janken(self):
        janken_options = ['rock', 'paper', 'scissors']
        selected_move = random.choice(janken_options)
        msg = String()
        msg.data = selected_move
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    janken_publisher = JankenPublisher()
    rclpy.spin(janken_publisher)
    janken_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

