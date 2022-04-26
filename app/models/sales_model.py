from sqlalchemy import ForeignKey, Column, Integer # importar tipagens necessárias Integer, String, etc
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass

#importar outros models relacionados
#from app.models.outro_model import OutroModel


@dataclass
class SalesModel(db.Model):
    id: int
    #estabelecer relações de tipo para serialização dataclass

    __tablename__ = "sales" #mudar nome da tabela

    id = Column(Integer, primary_key=True)
    #construção da tabela, adicionar foreign keys ao final

    #adicionar relacionamento
    #outro = relationship("OutroModel",backref(...))