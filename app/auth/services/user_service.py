from typing import Optional

from jose import JWTError, jwt
from sqlalchemy.orm import Session

from utils import http
from utils.auth import verify_password
from utils.constant import *
from ..config import ALGORITHM, SECRET_KEY
from ..models.user_model import TUser
from ..schemas.token_schema import TokenData


def get_user(db: Session, user_id: str) -> Optional[TUser]:
    return db.get(TUser, user_id)


def get_user_by_email(db: Session, user_email: str) -> Optional[TUser]:
    return db.query(TUser).filter(TUser.email == user_email).first()


def authenticate_user(db: Session, user_email: str, password: str):
    user = get_user_by_email(db, user_email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_current_user(db: Session, token: str, is_active: bool = False) -> TUser:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")

        if user_id is None:
            raise http.error(message="Could not validate credentials")
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise http.error(message="Could not validate credentials")

    user = get_user(db=db, user_id=token_data.user_id)

    if user is None:
        raise http.error(message="Could not validate credentials")

    if is_active:
        if user.status != STATUS_ACTIVE:
            raise http.error(message="Inactive user")
        return user
    return user
