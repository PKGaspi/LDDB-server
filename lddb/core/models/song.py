import uuid, datetime
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from lddb.core.database import Base

from . import song_author, file

class Song(Base):
    __tablename__ = "songs"

    name = Column(String, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey(song_author.SongAuthor.id))
    author = relationship("SongAuthor", backref="songs")
    filename = Column(String, nullable=False)