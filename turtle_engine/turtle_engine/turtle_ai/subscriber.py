from __future__ import print_function
import roslibpy
from typing import Optional


class Subscriber:
    def __init__(self, client: roslibpy.Ros):
        self.sub = roslibpy.Topic(client, '/turtlesim2/turtle1/pose', 'turtlesim/msg/Pose')
        # self.sub = roslibpy.Topic(client, '/turtlesim1/turtle1/cmd_vel', 'geometry_msgs/msg/Twist')
        self.msg: Optional[dict] = None
        self.sub.subscribe(lambda msg: self._message_callback(msg))

    def _message_callback(self, msg: dict = Optional[dict]) -> None:
        self.msg = msg

