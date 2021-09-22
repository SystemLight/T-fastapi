from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///db/database.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # 默认情况下，SQLite 将只允许一个线程与其通信
    # 这是为了防止意外地为不同的事物（对于不同的请求）共享相同的连接
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def session():
    s = SessionLocal()
    try:
        yield s
    finally:
        s.close()
