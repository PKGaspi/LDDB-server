from pydantic import BaseModel, Field
import datetime, uuid

from . import song_author

class SongBase(BaseModel):
    name: str
    author: song_author.SongAuthor

class SongCreate(SongBase):
    data: bytes

class Song(SongCreate):
    id: uuid.UUID = Field(default=uuid.uuid4())

    class Config():
        orm_mode = True
