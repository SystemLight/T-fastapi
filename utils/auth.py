from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: bytes, hashed_password: bytes):
    return pwd_context.verify(plain_password, hashed_password)


def gen_password_hash(password):
    return pwd_context.hash(password)
