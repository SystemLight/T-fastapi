from fastapi import FastAPI

from .routes import register_routes


def register_app(app: FastAPI):
    register_routes(app)
