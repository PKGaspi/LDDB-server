import uuid
from fastapi import FastAPI

from .routers import dances, songs

app = FastAPI()

app.include_router(dances.router)
app.include_router(songs.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
async def status():
    return {"status": "ok", "version": "1.0"}

