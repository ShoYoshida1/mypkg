#SPDX-FileCopyrightText: 2023 Sho Yoshida
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class jankenpub():
    def __init__(self, node):
        self.publisher = node.create_publisher(String, 'janken_pub', 10)
        node.create_timer(0.5, self.publish_janken_pub)

    def publish_janken_pub(self):
        janken_option = ['rock', 'paper', 'scissors']
        selected_move = random.choice(janken_option)
        msg = String()
        msg.data = selected_move
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = Node('janken_pub')
    janken_pub = jankenpub(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
