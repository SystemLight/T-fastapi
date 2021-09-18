from typing import List

from fastapi import APIRouter, Depends, Request, Path, Query, Body, Form, UploadFile, File
from sqlalchemy.orm import Session

from application import crud
from application.db import session
from application import schemas
from common.utils import http

router = APIRouter(prefix="/users")


@router.post("/casual", tags=["user"])
def create_casual_user(user: schemas.UserCreate, db: Session = Depends(session)):
    crud.create_casual_user(db=db, user=user)
    return http.ok()


@router.post("/", response_model=schemas.User, tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise http.error(message="Email already registered")

    _user = crud.create_user(db=db, user=user)
    return _user


@router.get("/", response_model=List[schemas.User], tags=["user"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(session)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User, tags=["user"])
def read_user(user_id: int, db: Session = Depends(session)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise http.error(message="User not found")
    return db_user


@router.post("/{user_id}/items/", response_model=schemas.Item, tags=["user"])
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(session)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
