import os
import posixpath
from enum import Enum

from fastapi import Path, HTTPException

from utils import security


class UploadPath(str, Enum):
    default = "default"


UPLOAD_PATH_DICT = {
    UploadPath.default: "default/"
}


def get_upload(upload_key: UploadPath = Path(..., description="上传文件块位置")):
    """

    获取文件上传目录

    :param upload_key:
    :return:

    """
    root_path = posixpath.abspath(UPLOAD_PATH_DICT[upload_key])

    def func(folder):
        path = security.safe_join(root_path, folder)
        os.makedirs(path, exist_ok=True)
        return path

    return func


class DownloadPath(str, Enum):
    default = "default"


DOWNLOAD_PATH_DICT = {
    DownloadPath.default: "default/"
}


def get_download(download_key: DownloadPath = Path(..., description="下载文件块位置")):
    """

    获取下载文件路径

    :param download_key:
    :return:

    """
    root_path = posixpath.abspath(DOWNLOAD_PATH_DICT[download_key])

    def func(folder):
        path = security.safe_join(root_path, folder)
        if not posixpath.exists(path):
            raise HTTPException(404, "The access file does not exist")
        for filename in os.listdir(path):
            return posixpath.join(path, filename), filename

    return func
