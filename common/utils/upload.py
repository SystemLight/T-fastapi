from fastapi import Form

from .security import safe_join


class ExistsError(Exception):
    ...


class UploadError(Exception):
    ...


class ChunkFile:
    """

    :param check_number: 当前块编号，默认从1开始
    :param chunk_size: 期望块大小
    :param current_chunk_size: 当前块实际大小
    :param total_size: 文件总大小
    :param identifier: 唯一标识
    :param filename: 文件原始名称
    :param relative_path: 文件相对路径
    :param total_chunks: 总块数

    """

    def __init__(
        self,
        check_number: int = Form(..., alias="chunkNumber", description="当前块编号，默认从1开始"),
        chunk_size: int = Form(..., alias="chunkSize", description="期望块大小"),
        current_chunk_size: int = Form(..., alias="currentChunkSize", description="当前块实际大小"),
        total_size: int = Form(..., alias="totalSize", description="文件总大小"),
        identifier: str = Form(..., alias="identifier", description="文件唯一标识"),
        filename: str = Form(..., alias="filename", description="文件原始名称"),
        relative_path: str = Form(..., alias="relativePath", description="文件相对路径"),
        total_chunks: int = Form(..., alias="totalChunks", description="总块数"),
    ):
        self.check_number = check_number
        self.chunk_size = chunk_size
        self.current_chunk_size = current_chunk_size
        self.total_size = total_size
        self.identifier = identifier
        self.filename = filename
        self.relative_path = relative_path
        self.total_chunks = total_chunks

        self.save_folder = "."

    def __call__(self):
        return self

    def save(self, file):
        with open(safe_join(self.save_folder, str(self.check_number)), "wb") as fp:
            for data in file:
                fp.write(data)
