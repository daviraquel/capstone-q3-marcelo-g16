from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import (  # importar tipagens necessárias Integer, String, etc
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import backref, relationship
from app.models.categories_collections_table import categories_collections


@dataclass
class CollectionsModel(db.Model):
    id: int
    creator: int
    name: str
    description: str

    __tablename__ = "collections"
    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(120), nullable=False, unique=True)
    description = Column(String(250))

    # adicionar relacionamento
    categories = relationship(
        "CategoriesModel", secondary=categories_collections, backref="collections"
    )
    # outro = relationship("OutroModel",backref(...))
