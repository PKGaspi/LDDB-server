import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class SongAuthor(Base):
    __tablename__ = "song_authors"
    
    name = Column(String, nullable=False)