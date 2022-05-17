import uuid
from sqlalchemy import Column, String, relationship

from lddb.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(uuid.UUID, primary_key=True)
    username = Column(String, nullable=False)
    dances = relationship("Dance", back_populates="creator")