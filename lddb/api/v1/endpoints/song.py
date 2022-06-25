import uuid, os

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from starlette.responses import FileResponse

from lddb.core.schemas.song import Song, SongCreate, SongBase
import lddb.core.services.song as SongServices
from lddb.core.database import get_db

router = APIRouter()

@router.post("/song")
async def post_song(
    file: UploadFile, 
    name: str,
    author_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    if file.content_type != "audio/wav":
        return {"code": 415,
                "msg": "Undupported Media Type. Only audio/wav is supported."
        }

    song = SongCreate(
        name = name,
        author_id = author_id,
        data = await file.read()
    )
    try:
        song_db = SongServices.add_song(db, song)
    except IntegrityError:
        return {
            "code": 418,
            "msg": "Invalid identifier"
        }
    return {
        "code": 200,
        "song": Song.from_orm(song_db).dict()
    }

@router.get("/song/{song_id}/info")
async def get_song(song_id: uuid.UUID, db: Session = Depends(get_db)):
    db_song = SongServices.get_song(db, song_id)

    if db_song == None:
        return {
            "code": 404,
            "msg": "Song not found"
        }

    return {
        "code": 200,
        "song": Song.from_orm(db_song).dict()
    }

@router.get("/song/{song_id}/data")
async def get_song(song_id: uuid.UUID, db: Session = Depends(get_db)):
    db_song = SongServices.get_song(db, song_id)

    if db_song == None:
        return {
            "code": 404,
            "msg": "Song not found"
        }

    filepath = os.path.join(os.getenv("SONGS_PATH"), db_song.filename)
    filename = db_song.name + ".wav"
    return FileResponse(filepath, media_type="audio/wav", filename=filename)


@router.get("/song_list")
async def song_list(db: Session = Depends(get_db)):
    results = SongServices.get_song_list(db)
    return {
        "code": 200,
        "list": [Song.from_orm(song).dict() for song in results]
    }