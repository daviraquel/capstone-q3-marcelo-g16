from flask import Blueprint
# importar blueprints
from app.routes.categories_blueprint import bp as bp_categories
from app.routes.collections_blueprint import bp as bp_collections
from app.routes.nfts_blueprint import bp as bp_nfts
from app.routes.sales_blueprint import bp as bp_sales
from app.routes.users_blueprint import bp as bp_users
            
bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

#registrar blueprints
bp_api.register_blueprint(bp_categories)
bp_api.register_blueprint(bp_collections)
bp_api.register_blueprint(bp_nfts)
bp_api.register_blueprint(bp_sales)
bp_api.register_blueprint(bp_users)