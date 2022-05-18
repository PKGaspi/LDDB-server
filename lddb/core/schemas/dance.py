from pydantic import BaseModel, Field, validator, ValidationError
import datetime, uuid

from . import song, user

class DanceBase(BaseModel):
    name: str



class DanceCreate(DanceBase):
    data: str
    creator_id: uuid.UUID
    song_id: uuid.UUID

    @validator("data")
    def parse_file(cls, v):
        # TODO: parse file looking for errors
        return v # assume ok

class Dance(DanceCreate):
    id: uuid.UUID = Field(default=uuid.uuid4())
    n_downloads: int = 0
    creator: user.User
    song: song.Song

    class Config():
        orm_mode = True

