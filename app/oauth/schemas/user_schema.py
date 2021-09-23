from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    status: Optional[str] = None  # 0：启用，1：禁用，2：删除


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
