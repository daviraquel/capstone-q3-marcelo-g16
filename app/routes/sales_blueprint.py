from flask import Blueprint

# importar controllers
from app.controllers.sales_controller import create_sale, read_sale, read_sales, update_sale, delete_sale

# alterar nome e prefixo da blueprint
bp = Blueprint("bp_sales", __name__, url_prefix="/sales")

# declarar métodos
bp.post("")(create_sale)
bp.get("")(read_sale)
bp.get("/<int:id>")(read_sales)
bp.patch("/<int:id>")(update_sale)
bp.delete("/<int:id>")(delete_sale)