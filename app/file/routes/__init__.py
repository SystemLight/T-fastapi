from fastapi import FastAPI

from . import download
from . import upload

url_prefix = "/file"


def register_routes(app: FastAPI):
    app.include_router(upload.router, prefix=url_prefix)
    app.include_router(download.router, prefix=url_prefix)
