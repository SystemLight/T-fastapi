from sqlalchemy import Column, Integer, String

from config.db import Base


class TUser(Base):
    __tablename__ = "t_user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, default="")
    username = Column(String, default="")
    status = Column(Integer, default=0)
