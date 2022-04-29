from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    # importar models
    from app.models.categories_collections_table import categories_collections
    from app.models.categories_model import CategoriesModel
    from app.models.collections_model import CollectionsModel
    from app.models.nfts_model import NftsModel
    from app.models.sales_model import SalesModel
    from app.models.users_model import UsersModel
