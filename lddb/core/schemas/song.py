from pydantic import BaseModel, Field
import datetime, uuid

class SongBase(BaseModel):
    name: str
    author: str

class SongCreate(SongBase):
    pass

class Song(SongCreate):
    id: uuid.UUID = Field(default=uuid.uuid4)
    file: bytes

    class Config():
        orm_mode = True
