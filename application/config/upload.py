import os
import posixpath
from enum import Enum

from fastapi import Path

from common.utils import security


class UploadPath(str, Enum):
    default = "default"


UPLOAD_CHUNK_PATH_DICT = {
    UploadPath.default: "default/"
}

UPLOAD_PATH_DICT = {
    UploadPath.default: "default/"
}


def get_upload(upload_key: UploadPath = Path(..., description="上传文件块位置")):
    """

    获取上传文件路径

    :param upload_key:
    :return:

    """
    # 文件块上传根目录
    root_path = posixpath.abspath(UPLOAD_CHUNK_PATH_DICT[upload_key])

    def func(folder):
        path = security.safe_join(root_path, folder)
        os.makedirs(path, exist_ok=True)
        return path

    return func
