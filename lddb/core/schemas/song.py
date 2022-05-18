from pydantic import BaseModel, Field
import datetime, uuid

from . import song_author

class SongBase(BaseModel):
    name: str

class SongCreate(SongBase):
    data: bytes
    author_id: uuid.UUID

class Song(SongBase):
    id: uuid.UUID
    author: song_author.SongAuthor

    class Config():
        orm_mode = True
