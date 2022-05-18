import uuid

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from lddb.core.schemas.user import User, UserCreate
import lddb.core.services.user as UserServices
from lddb.core.database import get_db

router = APIRouter()


@router.post("/user")
async def post_user(obj: UserCreate, db: Session = Depends(get_db)):
    db_obj = UserServices.add_user(db, obj)
    return {"code": 200,
            "obj": User.from_orm(db_obj).dict()
    }

@router.get("/user/{user_id}")
async def get_user(obj_id: uuid.UUID, db: Session = Depends(get_db)):
    db_obj = UserServices.get_user(db, obj_id)
    
    if db_obj == None:
        return {"code": 404, "msg": "Object not found"}

    return {"code": 200,
            "obj": User.from_orm(db_obj).dict()
    }

@router.get("/user_list")
async def user_list(db: Session = Depends(get_db)):
    results = UserServices.get_user_list(db)
    return {"code": 200,
            "list": [User.from_orm(obj).dict() for obj in results]
    }