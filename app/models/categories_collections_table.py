from app.configs.database import db


categories_collections = db.Table('categories_collections',
    db.Column('id', db.Integer, primary_key=True),
    # Coluna primeira referência
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    # Coluna segunda referência
    db.Column('collection_id', db.Integer, db.ForeignKey('collections.id'))
)