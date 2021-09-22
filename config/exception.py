from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from utils import http


def register_exception_handler(app: FastAPI):
    @app.exception_handler(http.FailException)
    async def fail_exception_handler(request: Request, exc: http.FailException):
        return JSONResponse(
            status_code=400,
            content=http.fail(data=exc.data, message=exc.message),
        )
