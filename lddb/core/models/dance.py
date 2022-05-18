import uuid, datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from lddb.core.database import Base
from . import song, user

class Dance(Base):
    __tablename__ = "dances"

    name = Column(String, nullable=False)
    creator_id = Column(UUID(as_uuid=True), ForeignKey(user.User.id))
    creator = relationship("User", backref="dances")
    song_id = Column(UUID(as_uuid=True), ForeignKey(song.Song.id))
    song = relationship("Song", backref="dances")
    filename = Column(String, nullable=False)
    downloads_count = Column(Integer, nullable=False, default=0)