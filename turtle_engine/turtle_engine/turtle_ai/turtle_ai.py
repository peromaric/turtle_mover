import roslibpy
from typing import Optional
from turtle_engine.module import Module
from .subscriber import Subscriber
from .publisher import Publisher


class TurtleAi(Module):
    def __init__(self, turtle_engine):
        super().__init__(turtle_engine)
        self.pose: Optional[dict] = None
        self.cmd_vel: Optional[dict] = None
        self.client = roslibpy.Ros(host='localhost', port=9090)
        self.sub: Optional[Subscriber] = None
        self.pub: Optional[Publisher] = None

    def connect_to_ros(self) -> None:
        self.client.run()
        self.sub = Subscriber(self.client)
        self.pub = Publisher(self.client)

        # publish initial cmd_vel
        # self.pub.publish()

    def disconnect_from_ros(self) -> None:
        self.client.terminate()

    def _calculate_new_cmd(self):
        if self.pose['x'] <= 0 | self.pose['x'] >= 11:
            self.pub.publish(self.cmd_vel)

    def get_pose(self) -> Optional[dict]:
        # self._calculate_new_cmd()
        return self.sub.msg
