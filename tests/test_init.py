import unittest

from app import create_data


class TestInit(unittest.TestCase):

    def test_create_data(self):
        """

        创建数据到数据库

        :return:

        """
        create_data()
