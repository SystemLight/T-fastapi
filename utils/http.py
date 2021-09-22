from typing import Any


def ok(data: Any = None, message: str = "ok"):
    return {"code": 200, "message": message, "data": data}


def fail(data: Any = None, message: str = "fail"):
    return {"code": 400, "message": message, "data": data}


class FailException(Exception):

    def __init__(self, data: Any = None, message: str = "fail"):
        self.code = 400
        self.message = message
        self.data = data


def error(data: Any = None, message: str = "fail"):
    return FailException(data, message)
