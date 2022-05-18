import uuid

from sqlalchemy.orm import Session

from . import models, schemas

def add_dance(db: Session, dance: schemas.dance.DanceCreate):
    print(dance)
    filename = uuid.uuid4() + ".dnc"
    file = io.open(os.path.join(os.getenv("DANCES_PATH"), filename), "wb")
    f.write(dance.data)
    f.close()
    db_dance = models.dance.Dance(
        name = dance.name,
        creator_id = dance.creator_id,
        song_id = dance.song_id,
        filename = filename,
    )
    db.add(db_dance)
    db.commit()
    return db_dance

def get_dance(db: Session, id: uuid.UUID):
    return db.query(models.dance.Dance).get(id)

def get_dance_list(db: Session):
    return db.query(models.dance.Dance).all()