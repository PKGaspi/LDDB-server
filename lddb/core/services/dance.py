import uuid

from sqlalquemy.orm import Session

from . import models, schemas

def get_dance(db: Session, id: uuid.UUID):
    return db.query(models.dance.Dance).get(id)

def get_dance_list(db: Session):
    return db.query(models.dance.Dance).all()

def add_dance(db: Session, dance: schemas.dance.DanceCreate):
    print(dance)
    dance = schemas.dance.Dance(obj)
    print(dance)
    db_dance = models.dance.Dance(
        id = dance.id,
        name = dance.name,
        creator = dance.creator,
        song = db.query
    )
    db.add(db_dance)
    db.commit()
    return id