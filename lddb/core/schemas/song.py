from pydantic import BaseModel, Field
import datetime, uuid

class SongCreate(BaseModel):
    name: str
    author: str

class Song(SongCreate):
    id: uuid.UUID
    created_at: datetime.datetime = Field(defualt=datetime.datetime.now())
    file: bytes

