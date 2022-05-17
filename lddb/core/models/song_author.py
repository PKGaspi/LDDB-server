import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class SongAuthor(Base):
    __tablename__ = "song_authors"
    
    name = Column(String, nullable=False)
    songs = relationship("Song", back_populates="author")