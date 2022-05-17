import uuid, datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class Dance(Base):
    __tablename__ = "dances"

    name = Column(String, nullable=False)
    creator = relationship("User", back_populates="dances")
    song = relationship("Song", back_populates="dances")
    downloads_count = Column(Integer, nullable=False, default=0)