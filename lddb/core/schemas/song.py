from pydantic import BaseModel, Field
import datetime

class SongCreate(BaseModel):
    name: str
    author: str

class Song(SongCreate):
    id: UUID
    created_at: datetime.datetime = Field(defualt=datetime.datetime.now())
    file: bytes

