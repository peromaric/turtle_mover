from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class PoseMsg(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None
    theta: Optional[float] = None
    linear_velocity: Optional[float] = None
    angular_velocity: Optional[float] = None