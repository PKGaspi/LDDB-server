import uuid, datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from lddb.core.database import Base
from . import file, song

class Dance(Base):
    __tablename__ = "dances"

    name = Column(String, nullable=False)
    creator = relationship("User", backref="dances")
    song_id = Column(String(36), ForeignKey(song.Song.id))
    song = relationship("Song", backref="dances")
    file_id = Column(String(36), ForeignKey(file.File.id))
    file = relationship("File", backref="content")
    downloads_count = Column(Integer, nullable=False, default=0)