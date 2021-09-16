from .item import *
from .user import *

from application import db


def create_all():
    db.Base.metadata.create_all(bind=db.engine)
