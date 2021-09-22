import unittest
import os


class TestPython(unittest.TestCase):

    def test_makedirs(self):
        """

        测试 os.makedirs 方法

        :return:

        """
        os.makedirs("asd/asd/asdf/asdf", exist_ok=True)
