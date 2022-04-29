from flask import Blueprint

# importar controllers
from app.controllers.collections_controller import create_collection, read_collection, read_collections, update_collection, delete_collection

# alterar nome e prefixo da blueprint
bp = Blueprint("bp_collections", __name__, url_prefix="/collections")

# declarar métodos
bp.post("")(create_collection)
bp.get("")(read_collections)
bp.get("/<name>")(read_collection)
bp.patch("/<name>")(update_collection)
bp.delete("/<name>")(delete_collection)