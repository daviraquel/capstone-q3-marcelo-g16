from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import (  # importar tipagens necessárias Integer, String, etc
    Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import backref, relationship
from datetime import datetime
#importar outros models relacionados
#from app.models.outro_model import OutroModel


@dataclass
class UsersModel(db.Model):
    id: int
    user_name:str
    email:str
    create_date:str
    update_date:str
    


    now = datetime.utcnow
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    create_date = Column(DateTime, default=now)
    update_date = Column(DateTime)
    

    #adicionar relacionamento
    #outro = relationship("OutroModel",backref(...))
