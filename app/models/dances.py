from pydantic import BaseModel, Field
import datetime, uuid

from .songs import Song

class Dance(BaseModel):
    name: str
    author: str
    upload_timestamp: datetime.datetime = Field(defualt=datetime.datetime.now())
    file: str
    n_downloads: int = 0
    song_id: uuid.UUID


