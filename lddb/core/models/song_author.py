import uuid
from sqlalchemy import Column, String, relationship

from lddb.core.database import Base

class Song(Base):
    __tablename__ = "song_authors"
    
    id = Column(uuid.UUID, primary_key=True)
    name = Column(String, nullable=False)
    songs = relationship("Song", back_populates="author")