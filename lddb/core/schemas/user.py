from pydantic import BaseModel, Field
import datetime, uuid

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class User(UserCreate):
    id: uuid.UUID = Field(default=uuid.uuid4)

    class Config():
        orm_mode = True

