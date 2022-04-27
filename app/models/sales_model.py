from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import backref, relationship


@dataclass
class SalesModel(db.Model):
    id: int
    seller: str
    buyer: str
    item: float
    value: float

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    seller = Column(String(50), ForeignKey("users.user_name"), nullable=False)
    buyer = Column(String(50), ForeignKey("users.user_name"), nullable=False)
    item = Column(Numeric, ForeignKey("nfts.id"), nullable=False)
    value = Column(Numeric, nullable=False)

    nfts = relationship("NftsModel", backref="nfts")
