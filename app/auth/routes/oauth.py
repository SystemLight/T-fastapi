from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.db import session
from utils import http
from ..config import *
from ..schemas.token_schema import Token
from ..services.user_service import authenticate_user
from ..utils import create_token

router = APIRouter(prefix="/oauth")


@router.post("/login", response_model=Token, tags=["auth-oauth"])
def login(db: Session = Depends(session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise http.error(message="Incorrect username or password")

    access_token = create_token(
        data={"user_id": user.id},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"token_type": "bearer", "access_token": access_token}
