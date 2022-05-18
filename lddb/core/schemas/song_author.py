from pydantic import BaseModel, Field
import datetime, uuid

class SongAuthorBase(BaseModel):
    name: str

class SongAuthorCreate(SongAuthorBase):
    pass

class SongAuthor(SongAuthorCreate):
    created_at: datetime.datetime
    modified_at: datetime.datetime
    id: uuid.UUID

    class Config():
        orm_mode = True

