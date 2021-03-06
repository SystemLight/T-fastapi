from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.oauth.config import oauth2_scheme
from app.oauth.schemas import user_schema
from app.oauth.services import user_service
from config.db import session

router = APIRouter(prefix="/users")


@router.get("/me", response_model=user_schema.User, tags=["default-users"])
def current_user(db: Session = Depends(session), token: str = Depends(oauth2_scheme)):
    return user_service.get_current_user(db, token)
