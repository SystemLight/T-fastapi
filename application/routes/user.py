from fastapi import APIRouter

from common.utils import http

router = APIRouter(prefix="/users")


@router.get("/exception")
def test_user_exception():
    raise http.error(message="测试的错误")
    return http.ok({"content": "user", "userID": user_id})


@router.get("/{user_id}")
def get_user(user_id: int):
    return http.ok({"content": "user", "userID": user_id})
