from __future__ import print_function
import roslibpy


class Publisher:
    def __init__(self, client: roslibpy.Ros):
        self.pub = roslibpy.Topic(client, '/turtlesim2/turtle2/cmd_vel', 'geometry_msgs/msg/Twist')

    def publish(self, msg: dict) -> None:
        self.pub.publish(msg)
