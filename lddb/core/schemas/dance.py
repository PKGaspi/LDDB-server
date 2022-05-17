from pydantic import BaseModel, Field
import datetime, uuid

from lddb.core.schemas.song import Song

class DanceCreate(BaseModel):
    name: str
    author: str
    file: str
    song_id: uuid.UUID

class Dance(DanceCreate):
    id: uuid.UUID
    created_at: datetime.datetime = Field(defualt=datetime.datetime.now())
    n_downloads: int = 0

