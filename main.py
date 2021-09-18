import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

import application

from common.utils import http

app = FastAPI(
    title="T-fastapi",
    description="fastapi开发模板",
    version="0.1.0",
    debug=True,
    docs_url="/swagger",
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(http.FailException)
async def fail_exception_handler(request: Request, exc: http.FailException):
    return JSONResponse(
        status_code=200,
        content=http.fail(data=exc.data, message=exc.message),
    )


# 注册应用包
application.register_app(app)


@app.get("/")
def root():
    return http.ok(data="Welcome to T-fastapi")


if __name__ == '__main__':
    """

    常用地址：

        - http://127.0.0.1:5000
        - http://127.0.0.1:5000/swagger
        - https://fastapi.tiangolo.com/zh/tutorial/first-steps/

    """
    uvicorn.run(app="main:app", host="0.0.0.0", port=5000, reload=False, debug=False)
