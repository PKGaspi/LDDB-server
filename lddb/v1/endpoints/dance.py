import uuid
from fastapi import APIRouter, File

from lddb.core.schemas.dance import Dance

router = APIRouter()


@router.post("/dance")
async def create_dance(dance: Dance):
    # TODO: validate and create entry in database
    return {"status": "ok"}

@router.get("/dance/{dance_id}")
async def get_dance(dance_id: uuid.UUID):
    # TODO: fetch in database
    return {"id": dance_id}

@router.get("/dance_list")
async def dance_list():
    # TODO: fetch a page of results
    return {"dance_list": [{"id": uuid.uuid4(), "name": "test", "author": "gaspi"}, {"id": uuid.uuid4(), "name": "test2"}]}
