import uuid
from sqlalchemy import Column, String

from lddb.core.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    filename = Column(String, unique=True, nullable=False)