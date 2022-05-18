import os, uuid, datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    isolation_level="SERIALIZABLE",
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(declarative_base()):
    __abstract__ = True
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    modified_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()