from pydantic import BaseModel, Field, validator, ValidationError
import datetime, uuid

from . import song, user

class DanceBase(BaseModel):
    name: str
    creator: user.User
    file: str
    song: song.Song

    @validator("file")
    def parse_file(cls, v):
        # TODO: parse file looking for errors
        return v # assume ok


class DanceCreate(DanceBase):
    pass

class Dance(DanceCreate):
    id: uuid.UUID = Field(default=uuid.uuid4())
    n_downloads: int = 0

    class Config():
        orm_mode = True

