from flask import Blueprint

# importar controllers
from app.controllers.categories_controller import create_category, read_categories,read_category, update_category, delete_category

# nome e prefixo da blueprint
bp = Blueprint("bp_categories", __name__, url_prefix="/categories")

# declarar métodos
bp.post("")(create_category)
bp.get("")(read_categories)
bp.get("/<int:id>")(read_category)
bp.patch("/<int:id>")(update_category)
bp.delete("/<int:id>")(delete_category)