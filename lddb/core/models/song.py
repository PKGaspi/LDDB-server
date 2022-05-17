import uuid, datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class Song(Base):
    __tablename__ = "songs"

    name = Column(String, nullable=False)
    author = relationship("User", back_populates="dances")
    dances = relationship("Dance", back_populates="song")