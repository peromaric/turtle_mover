from fastapi import FastAPI
import turtle_engine.router
from turtle_engine.router import router as turtle_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from turtle_engine.turtle_ai.turtle_ai import TurtleAi


class TurtleEngine:
    def __init__(self):
        self.turtle_ai = TurtleAi(self)
        self.api: FastAPI = FastAPI(
            title="TurtleEngine",
            description="Tell the turtle where to move"
        )
        turtle_engine.router.turtle_ai = self.turtle_ai
        self.api.include_router(turtle_router)
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:3000"], #allow frontend to connect
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"], )

        self.turtle_ai.connect_to_ros()
        self._run_uvicorn()


    def _run_uvicorn(self) -> None:
        uvicorn.run(self.api, host="0.0.0.0", port=8888)

    def get_api(self) -> FastAPI:
        return self.api
