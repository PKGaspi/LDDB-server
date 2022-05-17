import uuid, datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from lddb.core.database import Base

from . import song_author, file

class Song(Base):
    __tablename__ = "songs"

    name = Column(String, nullable=False)
    author_id = Column(String(36), ForeignKey(song_author.SongAuthor.id))
    author = relationship("User", backref="dances")
    file_id = Column(String(36), ForeignKey(file.File.id))
    file = relationship("File", backref="content")