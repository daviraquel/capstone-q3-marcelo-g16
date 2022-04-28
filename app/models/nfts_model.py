from sqlalchemy import Boolean, ForeignKey, Column, Integer, Numeric, String, Date
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime

#importar outros models relacionados
#from app.models.outro_model import OutroModel


@dataclass
class NftsModel(db.Model):
    
    id: int
    creator: str
    owner: int
    name:str
    for_sale:bool
    value:float
    description:str
    collection = int
    image = str
    created_at = str


    __tablename__ = "nfts" 

    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey('users.id'), nullable=False)
    owner = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    for_sale = Column(Boolean, nullable=False, default=True)
    value = Column(Numeric, nullable=False)
    description = Column(String(50), nullable=False)
    collection = Column(Integer, ForeignKey('collections.id'), nullable=False)
    image = Column(String)
    created_at = Column(Date, default=datetime.now())

    creator = relationship("UserModel", backref=backref('nfts', uselist=True), uselist=False)
    