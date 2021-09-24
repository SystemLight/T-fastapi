import datetime
import unittest
import os
from passlib.context import CryptContext

from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoic2EiLCJleHAiOjE2MzIyOTQwODJ9.n5w2N79Uy86rAfJFaTDth1nZPwbi68zDiGqO3Xzo52g"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


class TestPython(unittest.TestCase):

    def test_makedirs(self):
        """

        测试 os.makedirs 方法

        :return:

        """
        os.makedirs("asd/asd/asdf/asdf", exist_ok=True)

    def test_jose_encode(self):
        """

        python_jose

        :return:

        """
        encoded_jwt = jwt.encode(
            {
                "user_id": "sa",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            },
            SECRET_KEY,
            algorithm=ALGORITHM
        )
        print(encoded_jwt)

    def test_jose_decode(self):
        """

        python_jose

        :return:

        """
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)

    def test_passlib(self):
        """

        python_jose

        :return:

        """

        print(get_password_hash("hash"))
        self.assertFalse(verify_password(b"password", b"$2b$12$ylpw.Bac9Zm3Ey29WueqlefQbv.WvVcfbHb62PI9d4QXTFMJYSRFm"))
        self.assertTrue(verify_password(b"hash", b"$2b$12$ylpw.Bac9Zm3Ey29WueqlefQbv.WvVcfbHb62PI9d4QXTFMJYSRFm"))

    def test_cachelib(self):
        """

        cachelib

        :return:

        """
