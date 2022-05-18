from pydantic import BaseModel, Field
import datetime, uuid

class SongAuthorBase(BaseModel):
    name: str

class SongAuthorCreate(SongAuthorBase):
    pass

class SongAuthor(SongAuthorCreate):
    id: uuid.UUID

    class Config():
        orm_mode = True

