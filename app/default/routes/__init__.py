from fastapi import FastAPI

from . import user

url_prefix = "/default"


def register_routes(app: FastAPI):
    app.include_router(user.router, prefix=url_prefix)
