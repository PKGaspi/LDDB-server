import uuid
from sqlalchemy import Column, String

from lddb.core.database import Base

class File(Base):
    __tablename__ = "files"

    filename = Column(String, unique=True, nullable=False)