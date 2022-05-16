import uuid
from fastapi import APIRouter, UploadFile

from ..models.songs import Song

router = APIRouter()


@router.get("/song_list")
async def song_list():
    # TODO
    return {"song_list": [{"id": uuid.uuid4(), "name": "test", "author": "gaspi"}, {"id": uuid.uuid4(), "name": "test2"}]}

@router.post("/song")
async def post_song(song: Song):
    # TODO
    return {"status": "ok"}

@router.post("/song_file")
async def post_song_file(file: UploadFile):
    # TODO
    return {"id": uuid.uuid4()}

@router.get("/song/{song_id}")
async def get_song(song_id: uuid.UUID):
    # TODO
    return {"id": song_id}

# @app.get("/dance/{dance_id}/scores")
# async def get_dance_scores(dance_id: uuid.UUID):
#     return {"id": dance_id}
