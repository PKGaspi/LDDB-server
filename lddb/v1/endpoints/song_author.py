import uuid

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from lddb.core.schemas.song_author import SongAuthor, SongAuthorCreate
import lddb.core.services.song_author as SongAuthorServices
from lddb.core.database import get_db

router = APIRouter()

@router.post("/song_author")
async def post_song_author(song_author: SongAuthorCreate, db: Session = Depends(get_db)):
    db_song_author = SongAuthorServices.add_song_author(db, song_author)
    return {"code": 200,
            "song_author": SongAuthor.from_orm(db_song_author).dict()
    }

@router.get("/song_author/{song_author_id}")
async def get_song_author(song_author_id: uuid.UUID, db: Session = Depends(get_db)):
    db_song_author = SongAuthorServices.get_song_author(db, song_author_id)
    
    if db_song_author == None:
        return {"code": 404, "msg": "Song Author not found"}

    return {"code": 200,
            "song_author": SongAuthor.from_orm(db_song_author).dict()
    }
   
@router.get("/song_author_list")
async def song_author_list(db: Session = Depends(get_db)):
    results = SongAuthorServices.get_song_author_list(db)
    return {"code": 200,
            "list": [SongAuthor.from_orm(song_author).dict() for song_author in results]
    }
