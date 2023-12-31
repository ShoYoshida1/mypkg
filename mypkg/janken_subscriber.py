#SPDX-FileCopyrightText: 2023 Sho Yoshida
#SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import threading
import sys

class jankensub():
    def __init__(self, node):
        self.publisher = node.create_subscription(String, 'janken_pub', self.callback, 10)
        print("Waiting....")

    def callback(self, msg):
        print ("Received")
        publisher_move = msg.data
        user_move = input('Enter your move (rock, paper, scissors): ')
        
        if publisher_move== user_move:
            print("It\'s a draw!")
        elif (
            (publisher_move == 'rock' and user_move == 'scissors') or
            (publisher_move == 'paper' and user_move == 'rock') or
            (publisher_move == 'scissors' and user_move == 'paper')
        ):
            print("You lose!")
        elif (
            (publisher_move == 'rock' and user_move == 'paper') or
            (publisher_move == 'paper' and user_move == 'scissors') or
            (publisher_move == 'scissors' and user_move == 'rock')
        ):
            print("You win!")
        

def main():
    rclpy.init()
    node = Node('janken_sub')
    janken_sub = jankensub(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
