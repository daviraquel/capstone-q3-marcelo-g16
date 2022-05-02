from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import (  # importar tipagens necessárias Integer, String, etc
    Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import backref, relationship
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
#importar outros models relacionados
#from app.models.outro_model import OutroModel


@dataclass
class UsersModel(db.Model):
    id: int
    user_name:str
    email:str
    create_date:str
    last_update:str
    


    now = datetime.utcnow
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(120), nullable=False)
    create_date = Column(DateTime, default=now)
    last_update = Column(DateTime, default=now)
    

    #adicionar relacionamento
    #outro = relationship("OutroModel",backref(...))
    @property
    def inserted_password(self):
        raise AttributeError("You dont't have access to the password")

    @inserted_password.setter
    def inserted_password(self, password_to_hash):
        self.password = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare):
        
        return check_password_hash(self.password, password_to_compare)