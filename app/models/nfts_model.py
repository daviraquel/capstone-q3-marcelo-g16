from collections import UserList
from sqlalchemy import Boolean, Date, ForeignKey, Column, Integer, Numeric, String
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
from app.models.users_model import UsersModel

@dataclass
class NftsModel(db.Model):
    
    id: int
    creator: int
    owner: int
    name:str
    for_sale:bool
    value:float
    description:str
    collection: int
    image: str
    created_at: str
    creator_info:str


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

    creator_info = relationship("UsersModel", foreign_keys=[creator], backref='nfts')
    