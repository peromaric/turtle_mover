from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class Linear(BaseModel):
    x: float = 0
    y: float = 0
    z: float = 0


class Angular(BaseModel):
    x: float = 0
    y: float = 0
    z: float = 0


class TwistMsg(BaseModel):
    linear: Optional[Linear] = None
    angular: Optional[Angular] = None
