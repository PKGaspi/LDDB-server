import uuid

from sqlalchemy.orm import Session

from lddb.core.models.user import User as UserModel
from lddb.core.schemas.user import UserCreate

def get_user(db: Session, id: uuid.UUID):
    return db.query(UserModel).get(id)

def get_user_list(db: Session):
    return db.query(UserModel).all()

def add_user(db: Session, obj: UserCreate):
    db_obj = UserModel(
        username = obj.username,
    )
    db.add(db_obj)
    db.commit()
    return db_obj