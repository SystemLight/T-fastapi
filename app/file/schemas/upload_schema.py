from pydantic import BaseModel


class UploadSchema(BaseModel):
    identifier: str
    filename: str
    chunk_size: int
