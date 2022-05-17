import uuid
from sqlalchemy import Column, String, relationship

from lddb.core.database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(uuid.UUID, primary_key=True)
    name = Column(String, nullable=False)
    author = relationship("User", back_populates="dances")
    upload_date = Column(datetime.datetime, nullable=False, default=datetime.datetime.now)
    dances = relationship("Dance", back_populates="song")