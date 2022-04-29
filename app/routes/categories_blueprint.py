from flask import Blueprint

# importar controllers
from app.controllers.categories_controller import create_category, read_categories,read_category, update_category, delete_category

# nome e prefixo da blueprint
bp = Blueprint("bp_categories", __name__, url_prefix="/categories")

# declarar métodos
bp.post("")(create_category)
bp.get("")(read_categories)
bp.get("/<name>")(read_category)
bp.patch("/<name>")(update_category)
bp.delete("/<name>")(delete_category)