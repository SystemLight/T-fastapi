from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from application import crud
from application.db import session
from application import schemas

router = APIRouter(prefix="/items")


@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(session)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
