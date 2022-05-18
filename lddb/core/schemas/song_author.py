from pydantic import BaseModel, Field
import datetime, uuid

class SongAuthorBase(BaseModel):
    name: str

class SongAuthorCreate(SongAuthorBase):
    pass

class SongAuthor(SongAuthorCreate):
    id: uuid.UUID = Field(default=uuid.uuid4())

    class Config():
        orm_mode = True

