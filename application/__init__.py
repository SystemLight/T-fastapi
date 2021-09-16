from fastapi import FastAPI

from .routes import user


def register_app(app: FastAPI):
    app.include_router(user.router)
