import uuid

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from lddb.core.schemas.song_author import SongAuthor, SongAuthorCreate
import lddb.core.services.song_author as SongAuthorServices
from lddb.core.database import get_db

router = APIRouter()


@router.get("/song_author_list")
async def song_author_list(db: Session = Depends(get_db)):
    results = SongAuthorServices.get_song_author_list(db)
    return {"code": 200,
            "list": [SongAuthor.from_orm(obj).dict() for obj in results]
    }

@router.post("/song_author")
async def post_song_author(obj: SongAuthorCreate, db: Session = Depends(get_db)):
    db_obj = SongAuthorServices.add_song_author(db, obj)
    return {"code": 200,
            "obj": SongAuthor.from_orm(db_obj).dict()
    }

@router.get("/song_author/{song_author_id}")
async def get_song_author(obj_id: uuid.UUID, db: Session = Depends(get_db)):
    db_obj = SongAuthorServices.get_song_author(db, obj_id)
    
    if db_obj == None:
        return {"code": 404, "msg": "Object not found"}

    return {"code": 200,
            "obj": SongAuthor.from_orm(db_obj).dict()
    }
    

# @app.get("/dance/{dance_id}/scores")
# async def get_dance_scores(dance_id: uuid.UUID):
#     return {"id": dance_id}
