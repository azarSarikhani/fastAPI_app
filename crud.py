from sqlalchemy.orm import Session
from models.animals import AnimalModel



def get_animals(db: Session, skip: int = 0, limit: int = 100):
    result = db.query(AnimalModel).offset(skip).limit(limit).all()
    return result




