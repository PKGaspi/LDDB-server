import uuid, os
from dotenv import load_dotenv
from fastapi import FastAPI

from lddb.v1.endpoints import dance, song
from lddb.core.database import SessionLocal, engine, Base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

load_dotenv()

app = FastAPI()


app.include_router(dance.router)
app.include_router(song.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/status")
async def status():
    return {"status": "ok", "version": "1.0"}

