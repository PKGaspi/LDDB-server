import uuid

from sqlalchemy.orm import Session

from . import models, schemas

def get_dance(db: Session, id: uuid.UUID):
    return db.query(models.dance.Dance).get(id)

def get_dance_list(db: Session):
    return db.query(models.dance.Dance).all()

def add_dance(db: Session, dance: schemas.dance.DanceCreate):
    print(dance)
    dance = schemas.dance.Dance(dance)
    print(dance)
    db_dance = models.dance.Dance(
        id = dance.id,
        name = dance.name,
        creator = dance.creator,
        song = schemas.song.Song(db.query(models.song.Song).get(dance.song.id))
    )
    db.add(db_dance)
    db.commit()
    return db_dance