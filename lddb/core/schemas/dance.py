from pydantic import BaseModel, Field
import datetime, uuid

from . import song, user

class DanceBase(BaseModel):
    name: str
    creator: user.User
    file: str
    song: song.Song

class DanceCreate(DanceBase):
    pass

class Dance(DanceCreate):
    id: uuid.UUID = Field(default=uuid.uuid4)
    n_downloads: int = 0

    class Config():
        orm_mode = True

