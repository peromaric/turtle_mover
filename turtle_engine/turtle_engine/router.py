import starlette.websockets
from fastapi_utils.inferring_router import InferringRouter
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from turtle_engine.turtle_ai.turtle_ai import TurtleAi
from typing import Optional
import random
from starlette.websockets import WebSocket
import asyncio

"""
router with its .get and .post routes below.
include this router in a fastapi instance.
"""
router: InferringRouter = InferringRouter()
turtle_ai: Optional[TurtleAi]

@router.get(
    "/",
    summary="Home Page"
)
async def home():
    response: RedirectResponse = RedirectResponse(url="/redoc")  # redirect to interface
    return response


"""
food coords generates random 0 <= x, y <= 11 coordinates
where the poor lil' turtle can find it's food
"""


class FoodCoords(BaseModel):
    x: int
    y: int


@router.get(
    "/food_coords",
    response_model=FoodCoords,
    summary="Returns food coords"
)
async def get_food_coordinates():
    return FoodCoords(x=random.randint(0, 11), y=random.randint(0, 11))


@router.websocket("/turtle_ai_pose")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept(subprotocol=None)
    try:
        while True:
            await asyncio.sleep(0.1)
            data = await turtle_ai.get_pose()
            await websocket.send_json(data)
    # doesn't work that well, the a disgusting exception occurs on disconnect
    except (starlette.websockets.WebSocketDisconnect, starlette.websockets.WebSocketClose):
        print("Connection closed")
        await websocket.close()
