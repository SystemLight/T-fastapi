from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.db import session
from utils import http
from ..schemas.token_schema import Token
from ..services.user_service import authenticate_user
from ..utils import encode_token

router = APIRouter(prefix="/oauth")


@router.post("/login", response_model=Token, tags=["auth-oauth"])
def login(db: Session = Depends(session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise http.error(message="Incorrect username or password")

    return {"token_type": "bearer", "access_token": encode_token({"user_id": user.id})}
