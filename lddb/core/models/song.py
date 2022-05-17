import uuid, datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    author = relationship("User", back_populates="dances")
    upload_date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    dances = relationship("Dance", back_populates="song")