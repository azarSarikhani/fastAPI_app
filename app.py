import uvicorn
from crud import get_animals
from sqlalchemy.orm import Session
#from models import animals
from schemas.animal_schema import Animal
from models.database import SessionLocal, engine
from fastapi import Depends, FastAPI, HTTPException

#animals.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/animals/", response_model=list[Animal])
def read_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    animals = get_animals(db, skip=skip, limit=limit)
    return animals


if __name__ == "__main__":
    print("this function is called directly.")
    uvicorn.run("app:app", reload=True)