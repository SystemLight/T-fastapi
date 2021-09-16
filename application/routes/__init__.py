from fastapi import FastAPI

from . import user
from . import item


def register_routes(app: FastAPI):
    app.include_router(user.router)
    app.include_router(item.router)
