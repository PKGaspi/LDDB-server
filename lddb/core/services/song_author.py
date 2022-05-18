import uuid

from sqlalchemy.orm import Session

from lddb.core.models.song_author import SongAuthor as SongAuthorModel
from lddb.core.schemas.song_author import SongAuthorCreate

def get_song_author(db: Session, id: uuid.UUID):
    return db.query(SongAuthorModel).get(id)

def get_song_author_list(db: Session):
    return db.query(SongAuthorModel).all()

def add_song_author(db: Session, obj: SongAuthorCreate):
    print(obj)
    db_obj = SongAuthorModel(
        id=uuid.uuid4(),
        name=obj.name,
    )
    db.add(db_obj)
    db.commit()
    return db_obj