import uuid, os, io

from fastapi import APIRouter, File, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette.responses import FileResponse


from lddb.core.schemas.dance import Dance, DanceCreate
import lddb.core.services.dance as DanceServices
from lddb.core.database import get_db

router = APIRouter()


@router.post("/dance")
async def create_dance(dance: DanceCreate, db: Session = Depends(get_db)):
    try:
        dance_db = DanceServices.add_dance(db, dance)
    except IntegrityError:
        return {
            "code": 418,
            "msg": "Invalid identifier"
        }
    return {
        "code": 200,
        "dance": Dance.from_orm(dance_db).dict()
    }

@router.get("/dance/{dance_id}/info")
async def get_dance(dance_id: uuid.UUID, db: Session = Depends(get_db)):
    db_dance = DanceServices.get_dance(db, dance_id)

    if db_dance == None:
        return {
            "code": 404,
            "msg": "Dance not found"
        }

    return {
        "code": 200,
        "dance": Dance.from_orm(db_dance).dict()
    }

@router.get("/dance/{dance_id}/data")
async def get_dance(dance_id: uuid.UUID, db: Session = Depends(get_db)):
    db_dance = DanceServices.get_dance(db, dance_id, download=True)

    if db_dance == None:
        return {
            "code": 404,
            "msg": "Dance not found"
        }

    filepath = os.path.join(os.getenv("DANCES_PATH"), db_dance.filename)
    filename = db_dance.name + ".dnc"
    return FileResponse(filepath, media_type="text/dnc", filename=filename)

@router.get("/dance_list")
async def dance_list(db: Session = Depends(get_db)):
    results = DanceServices.get_dance_list(db)
    return {
        "code": 200,
        "list": [Dance.from_orm(dance).dict() for dance in results]
    }
