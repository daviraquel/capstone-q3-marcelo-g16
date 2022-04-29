from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import (  # importar tipagens necessárias Integer, String, etc
    Column, ForeignKey, Integer, String)
from sqlalchemy.orm import backref, relationship

#importar outros models relacionados
#from app.models.outro_model import OutroModel


@dataclass
class CategoriesModel(db.Model):
    id: int
    name:str
    description:str

    __tablename__ = "categories" 

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250))


    #adicionar relacionamento
    #outro = relationship("OutroModel",backref(...))
