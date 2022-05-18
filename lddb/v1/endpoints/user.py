import uuid

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from lddb.core.schemas.user import User, UserCreate
import lddb.core.services.user as UserServices
from lddb.core.database import get_db

router = APIRouter()


@router.post("/user")
async def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserServices.add_user(db, user)
    return {
        "code": 200,
        "user": User.from_orm(db_user).dict()
    }

@router.get("/user/{user_id}")
async def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = UserServices.get_user(db, user_id)
    
    if db_user == None:
        return {
            "code": 404, 
            "msg": "Object not found"
        }

    return {
        "code": 200,
        "user": User.from_orm(db_user).dict()
    }

@router.get("/user_list")
async def user_list(db: Session = Depends(get_db)):
    results = UserServices.get_user_list(db)
    return {
        "code": 200,
        "list": [User.from_orm(user).dict() for user in results]
    }