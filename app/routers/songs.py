import uuid
from fastapi import APIRouter

from ..models.songs import Song

router = APIRouter()


@router.get("/song_list")
async def song_list():
    return {"song_list": [{"id": uuid.uuid4(), "name": "test", "author": "gaspi"}, {"id": uuid.uuid4(), "name": "test2"}]}

@router.post("/song")
async def post_song(song: Song):
    return {"status": "ok"}

@router.get("/song/{song_id}")
async def get_song(song_id: uuid.UUID):
    return {"id": song_id}

# @app.get("/dance/{dance_id}/scores")
# async def get_dance_scores(dance_id: uuid.UUID):
#     return {"id": dance_id}
