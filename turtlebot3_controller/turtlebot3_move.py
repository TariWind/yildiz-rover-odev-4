#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Turtlebot3Controller(Node):

    def __init__(self):
        super().__init__("turtlebot3_controller")

        self.cmd_publish = self.create_publisher(
            Twist, '/cmd_vel', 10
        )

        self.odom_subscriber = self.create_subscription(
            Odometry, '/odom', self.odom_callback, 10
        )

        self.timer = self.create_timer(
            0.1, self.robot_move
        )

        self.goal_x = 2.0
        self.curr_x = 0.0
        self.goal_achieved = False

        self.get_logger().info("Turtlebot Controller node has started!")

    def odom_callback(self, msg):
        self.curr_x = msg.pose.pose.position.x

    def robot_move(self):
        twist = Twist()

        distance = self.goal_x - self.curr_x

        if abs(distance) < 0.05:
            if not self.goal_achieved:
                twist.linear.x = 0.0
                twist.angular.z = 0.0

                self.cmd_publish.publish(twist)
                self.goal_achieved = True
                self.get_logger().info("Destination reached, the robot has stopped!")

        else:
            if not self.goal_achieved:
                twist.linear.x = 0.2
                twist.angular.z = 0.0
                self.cmd_publish.publish(twist)

            
           
    

def main(args=None):
    rclpy.init(args=args)

    node = Turtlebot3Controller()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

        