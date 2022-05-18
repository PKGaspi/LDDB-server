import uuid, io, os

from sqlalchemy.orm import Session

from . import models, schemas

def get_song(db: Session, id: uuid.UUID):
    return db.query(models.song.Song).get(id)

def get_song_list(db: Session):
    return db.query(models.song.Song).all()

def add_song(db: Session, song: schemas.song.SongCreate):
    print(song)
    song = schemas.song.Song(song)
    print(song)
    file = io.open(os.path.join(os.getenv("SONG_PATH"), song.id), "wb")
    f.write(song.data)
    f.close()
    db_song = models.song.Song(
        id = song.id,
        name = song.name,
        author = song.author.id,
        file = song.id,
    )
    db.add(db_song)
    db.commit()
    return db_song