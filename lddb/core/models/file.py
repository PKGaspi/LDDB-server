import uuid
from sqlalchemy import Column, String

from lddb.core.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(uuid.UUID, primary_key=True)
    filename = Column(String, unique=True, nullable=False)