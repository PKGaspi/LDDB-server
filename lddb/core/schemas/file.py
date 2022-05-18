from pydantic import BaseModel, Field
import datetime, uuid

class FileBase(BaseModel):
    filename: str

class FileCreate(FileBase):
    pass

class File(FileCreate):
    id: uuid.UUID
    
    class Config():
        orm_mode = True

