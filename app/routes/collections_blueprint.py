from flask import Blueprint

# importar controllers
from app.controllers.collections_controller import create_collection, read_collection, read_collections, update_collection, delete_collection

# alterar nome e prefixo da blueprint
bp = Blueprint("bp_collections", __name__, url_prefix="/collections")

# declarar métodos
bp.post("")(create_collection)
bp.get("")(read_collection)
bp.get("/<int:id>")(read_collections)
bp.patch("/<int:id>")(update_collection)
bp.delete("/<int:id>")(delete_collection)