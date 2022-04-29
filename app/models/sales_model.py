from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import backref, relationship


@dataclass
class SalesModel(db.Model):
    id: int
    seller: int
    buyer: int
    item: int
    value: float

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    seller = Column(Integer, ForeignKey("users.id"), nullable=False)
    buyer = Column(Integer, ForeignKey("users.id"), nullable=False)
    item = Column(Integer, ForeignKey("nfts.id"), nullable=False)
    value = Column(Numeric, nullable=False)

    nfts = relationship("NftsModel", backref="nfts")
