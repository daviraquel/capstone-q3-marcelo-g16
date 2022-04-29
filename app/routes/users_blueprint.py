from flask import Blueprint

# importar controllers
from app.controllers.users_controller import create_user, read_user, read_users, update_user, delete_user

# alterar nome e prefixo da blueprint
bp = Blueprint("bp_users", __name__, url_prefix="/users")

# declarar métodos
bp.post("")(create_user)
bp.get("/<user_email>")(read_user)
bp.get("")(read_users)
bp.patch("//<user_email>")(update_user)
bp.delete("/<user_email>")(delete_user)