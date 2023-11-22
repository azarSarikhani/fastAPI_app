from pydantic import BaseModel


class AnimalBase(BaseModel):
    name: str | None = None



class Animal(AnimalBase):
    id: int

    class Config:
        from_attributes = True


class AnimalCreate(AnimalBase):
    pass


