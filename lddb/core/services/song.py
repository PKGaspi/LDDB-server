import uuid, io, os

from sqlalchemy.orm import Session

from lddb.core.models.song import Song as SongModel
from lddb.core.schemas.song import SongCreate

def get_song(db: Session, id: uuid.UUID):
    return db.query(SongModel).get(id)

def get_song_list(db: Session):
    return db.query(SongModel).all()

def add_song(db: Session, song: SongCreate):
    filename = str(uuid.uuid4()) + ".wav"
    db_song = SongModel(
        name = song.name,
        author_id = song.author_id,
        filename = filename,
    )
    db.add(db_song)
    db.commit()
    file = io.open(os.path.join(os.getenv("SONGS_PATH"), filename), "wb")
    file.write(song.data)
    file.close()
    return db_song