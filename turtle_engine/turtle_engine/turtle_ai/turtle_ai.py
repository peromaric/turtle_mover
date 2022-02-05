import roslibpy
from typing import Optional
from turtle_engine.module import Module
from .subscriber import Subscriber
from .publisher import Publisher
from .msg_models.twist_msg import TwistMsg, Linear, Angular
import time
import random
from threading import Thread


class TurtleAi(Module):
    def __init__(self, turtle_engine):
        super().__init__(turtle_engine)
        self.pose: Optional[dict] = None
        self.cmd_vel: Optional[dict] = None
        self.client = roslibpy.Ros(host='0.0.0.0', port=9090)
        self.sub: Optional[Subscriber] = None
        self.pub: Optional[Publisher] = None

    def connect_to_ros(self) -> None:
        # run ros client
        self.client.run()
        self.sub = Subscriber(self.client)
        self.pub = Publisher(self.client)

        # set initial cmd_vel
        self.cmd_vel = self._generate_cmd_vel(x=1)

        # start the thread which tracks and updates the state of this class
        Thread(target=self._update_turtle_state, daemon=True).start()

    def disconnect_from_ros(self) -> None:
        self.client.terminate()

    def _calculate_new_cmd(self) -> None:
        # hope nothing bad happens ;-o
        self.cmd_vel = self._generate_cmd_vel(x=random.randint(-3, 3),
                                              y=random.randint(-3, 3),
                                              z=random.randint(0, 2))

    async def get_pose(self) -> Optional[dict]:
        return self.pose

    def _update_turtle_state(self):
        while self.client.is_connected:
            time.sleep(1)
            self.pose = self.sub.msg
            self._calculate_new_cmd()
            self.pub.publish(self.cmd_vel)

    def _generate_cmd_vel(self, x: int = 0, y: int = 0, z: int = 0) -> dict:
        cmd_vel = TwistMsg()
        cmd_linear = Linear()
        cmd_angular = Angular()
        # float cast done on purpose, twist demands it
        cmd_linear.x = float(x)
        cmd_linear.y = float(y)
        cmd_angular.z = float(z)
        cmd_vel.linear = cmd_linear
        cmd_vel.angular = cmd_angular
        return cmd_vel.dict()
