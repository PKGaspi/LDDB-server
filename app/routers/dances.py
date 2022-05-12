import uuid
from fastapi import APIRouter

router = APIRouter()


@router.get("/dance_list")
async def dance_list():
    return {"dance_list": [{"id": uuid.uuid4(), "name": "test", "author": "gaspi"}, {"id": uuid.uuid4(), "name": "test2"}]}

@router.post("/dance")
async def post_dance(dance):
    return {"status": "ok"}

@router.get("/dance/{dance_id}")
async def get_dance(dance_id: uuid.UUID):
    return {"id": dance_id}

# @app.get("/song/{song_id}/dances")
# async def get_song(song_id: uuid.UUID):
#     return {[]}
