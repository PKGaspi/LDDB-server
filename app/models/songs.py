from pydantic import BaseModel, Field
import datetime

class Song(BaseModel):
    name: str
    author: str
    upload_timestamp: datetime.datetime = Field(defualt=datetime.datetime.now())
    file: bytes


