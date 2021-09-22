import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils import http
from config.exception import register_exception_handler
from app import register_all_routes

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

register_exception_handler(app)
register_all_routes(app)


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
    uvicorn.run(app="main:app", host="0.0.0.0", port=5000, reload=True, debug=False)
