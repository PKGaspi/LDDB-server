from pydantic import BaseModel, Field
import datetime, uuid

from . import song_author

class SongBase(BaseModel):
    name: str

class SongCreate(SongBase):
    data: bytes
    author_id: uuid.UUID

class Song(SongBase):
    author: song_author.SongAuthor
    created_at: datetime.datetime
    modified_at: datetime.datetime
    id: uuid.UUID

    class Config():
        orm_mode = True
