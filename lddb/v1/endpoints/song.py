import uuid
from fastapi import APIRouter, UploadFile

from lddb.core.schemas.song import Song, SongCreate

router = APIRouter()


@router.get("/song_list")
async def song_list():
    # TODO
    return {"song_list": [{"id": uuid.uuid4(), "name": "test", "author": "gaspi"}, {"id": uuid.uuid4(), "name": "test2"}]}

@router.post("/song")
async def post_song(song: SongCreate, file: UploadFile):
    # TODO
    
    return {"status": "ok"}

@router.get("/song/{song_id}")
async def get_song(song_id: uuid.UUID):
    # TODO
    return {"id": song_id}

# @app.get("/dance/{dance_id}/scores")
# async def get_dance_scores(dance_id: uuid.UUID):
#     return {"id": dance_id}
