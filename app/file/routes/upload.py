import os
import posixpath
from typing import Callable

from fastapi import APIRouter, File, UploadFile, Depends, Query, Form, Body
from fastapi.responses import JSONResponse

from utils import http
from utils.security import safe_join
from ..config import get_upload
from ..schemas.upload_schema import UploadSchema

router = APIRouter(prefix="/upload")


@router.get("/{upload_key}", tags=["file-upload"])
def check_upload(
    upload: Callable[[str], str] = Depends(get_upload),
    check_number: int = Query(..., alias="chunkNumber", description="当前块编号，默认从1开始"),
    chunk_size: int = Query(..., alias="chunkSize", description="期望块大小"),
    current_chunk_size: int = Query(..., alias="currentChunkSize", description="当前块实际大小"),
    total_size: int = Query(..., alias="totalSize", description="文件总大小"),
    identifier: str = Query(..., alias="identifier", description="文件唯一标识"),
    filename: str = Query(..., alias="filename", description="文件原始名称"),
    relative_path: str = Query(..., alias="relativePath", description="文件相对路径"),
    total_chunks: int = Query(..., alias="totalChunks", description="总块数"),
):
    """

    检测上传块是否存在::

        - 404: 校验块不存在
        - [200, 201, 202]: 校验块存在
        - [400, 415, 500, 501]: 接口请求错误

    使用simple-upload.js::

        https://github.com/simple-uploader/Uploader/blob/develop/README_zh-CN.md
        new Uploader({
            target: 'http://127.0.0.1:5000/upload/default',
            singleFile: true,
            simultaneousUploads: 5,
            chunkSize: 1024 * 1024 * 10,
            successStatuses: [200, 201, 202],
            permanentErrors: [400, 415, 500, 501],
            testChunks: false,
            allowDuplicateUploads: false
          })

    :param total_chunks:
    :param relative_path:
    :param filename:
    :param identifier:
    :param total_size:
    :param current_chunk_size:
    :param chunk_size:
    :param check_number:
    :param upload: 上传文件位置
    :return:

    """
    return JSONResponse(content=http.fail(), status_code=404)


@router.post("/{upload_key}", tags=["upload-upload"])
def post_upload(
    upload: Callable[[str], str] = Depends(get_upload),
    check_number: int = Form(..., alias="chunkNumber", description="当前块编号，默认从1开始"),
    chunk_size: int = Form(..., alias="chunkSize", description="期望块大小"),
    current_chunk_size: int = Form(..., alias="currentChunkSize", description="当前块实际大小"),
    total_size: int = Form(..., alias="totalSize", description="文件总大小"),
    identifier: str = Form(..., alias="identifier", description="文件唯一标识"),
    filename: str = Form(..., alias="filename", description="文件原始名称"),
    relative_path: str = Form(..., alias="relativePath", description="文件相对路径"),
    total_chunks: int = Form(..., alias="totalChunks", description="总块数"),
    file: UploadFile = File(...)
):
    """

    文件块上传

    :param upload: 上传路径获取函数
    :param total_chunks:
    :param relative_path:
    :param filename:
    :param identifier:
    :param total_size:
    :param current_chunk_size:
    :param chunk_size:
    :param check_number:
    :param file: 文件实体
    :return:

    """
    folder = upload(identifier)
    with open(safe_join(folder, str(check_number)), "wb") as fp:
        for data in file.file:
            fp.write(data)
    file.file.close()
    return http.ok()


@router.put("/{upload_key}", tags=["upload-upload"])
def merge_upload(
    upload: Callable[[str], str] = Depends(get_upload),
    upload_schema: UploadSchema = Body(..., description="上传文件实体信息")
):
    """

    合并文件块完成文件上传

    :param upload: 上传路径获取函数
    :param upload_schema: 上传文件实体信息
    :return:

    """
    folder = upload(upload_schema.identifier)
    with open(posixpath.join(folder, upload_schema.filename), "wb") as target_fp:
        for i in range(1, upload_schema.chunk_size + 1):
            chunk_path = posixpath.join(folder, str(i))
            with open(chunk_path, "rb") as chunk_fp:
                target_fp.write(chunk_fp.read())
                target_fp.flush()
            os.remove(chunk_path)
    return http.ok()
