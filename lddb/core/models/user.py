import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from lddb.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    username = Column(String, nullable=False)
    dances = relationship("Dance", back_populates="creator")