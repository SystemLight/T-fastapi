from fastapi import FastAPI

from . import oauth

url_prefix = ""


def register_routes(app: FastAPI):
    app.include_router(oauth.router, prefix=url_prefix)
