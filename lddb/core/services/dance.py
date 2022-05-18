import uuid, io, os

from sqlalchemy.orm import Session

from lddb.core.models.dance import Dance as DanceModel
from lddb.core.schemas.dance import DanceCreate

def add_dance(db: Session, dance: DanceCreate):
    filename = str(uuid.uuid4()) + ".dnc"
    db_dance = DanceModel(
        name = dance.name,
        creator_id = dance.creator_id,
        song_id = dance.song_id,
        filename = filename,
    )
    db.add(db_dance)
    db.commit()
    file = io.open(os.path.join(os.getenv("DANCES_PATH"), filename), "wb")
    file.write(bytes(dance.data, "utf-8"))
    file.close()
    return db_dance

def get_dance(db: Session, id: uuid.UUID, download=False):
    db_dance = db.query(DanceModel).get(id)

    if db_dance != None and download:
        db_dance.downloads_count += 1
        db.commit()
        
    return db_dance

def get_dance_list(db: Session):
    return db.query(DanceModel).all()