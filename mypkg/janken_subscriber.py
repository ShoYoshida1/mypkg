# サブスクライバーノード (janken_subscriber.py)

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class JankenSubscriber(Node):

    def __init__(self):
        super().__init__('janken_subscriber')
        self.subscription = self.create_subscription(String,'janken_topic',self.callback,10)
        print("waiting....")

    def callback(self, msg):
        self.get_logger().info(f'Received')
        user_input = input('Enter your move (rock, paper, scissors): ')
        self.compare_moves(msg.data, user_input)

    def compare_moves(self, publisher_move, user_move):
        if publisher_move == user_move:
            self.get_logger().info('It\'s a draw!')
        elif (
            (publisher_move == 'rock' and user_move == 'scissors') or
            (publisher_move == 'paper' and user_move == 'rock') or
            (publisher_move == 'scissors' and user_move == 'paper')
        ):
            self.get_logger().info('You lose!')
        else:
            self.get_logger().info('You win!')

def main(args=None):
    rclpy.init(args=args)
    janken_subscriber = JankenSubscriber()
    rclpy.spin(janken_subscriber)
    janken_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

