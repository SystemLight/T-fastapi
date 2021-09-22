from fastapi import FastAPI

from . import upload

url_prefix = ""


def register_routes(app: FastAPI):
    app.include_router(upload.router, prefix=url_prefix)
