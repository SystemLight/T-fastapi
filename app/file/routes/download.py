from fastapi import APIRouter, Depends, Query
from starlette.responses import FileResponse

from typing import Callable, Optional

from ..config import get_download

router = APIRouter(prefix="/download")


@router.get("/{download_key}", tags=["file-download"])
def download_file(
    download: Callable[[str], str] = Depends(get_download),
    file_id: str = Query(...),
    is_download: Optional[bool] = Query(False)
):
    """

    下载文件

    :param download:
    :param file_id: 文件唯一标识符
    :param is_download:是否为下载文件，不填写或者false则根据类型返回显示
    :return:

    """
    file_path, file_name = download(file_id)
    if is_download:
        return FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
    return FileResponse(file_path)
