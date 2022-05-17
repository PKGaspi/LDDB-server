import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class Song(Base):
    __tablename__ = "song_authors"
    
    name = Column(String, nullable=False)
    songs = relationship("Song", back_populates="author")