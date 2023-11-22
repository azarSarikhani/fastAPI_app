from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
import os



class AnimalModel(Base):
    __tablename__ = os.environ.get('tablename')

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # is_active = Column(Boolean, default=True)


