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

class Dance(DanceBase):
    downloads_count: int
    creator: user.User
    song: song.Song
    created_at: datetime.datetime
    modified_at: datetime.datetime
    id: uuid.UUID

    class Config():
        orm_mode = True

