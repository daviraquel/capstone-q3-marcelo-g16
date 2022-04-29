from flask import Blueprint

# importar controllers
from app.controllers.nfts_controller import create_nft, read_nft, read_nfts, update_nft, delete_nft

# alterar nome e prefixo da blueprint
bp = Blueprint("bp_nfts", __name__, url_prefix="/nfts")

# declarar métodos
bp.post("")(create_nft)
bp.get("")(read_nft)
bp.get("/<int:id>")(read_nfts)
bp.patch("/<int:id>")(update_nft)
bp.delete("/<int:id>")(delete_nft)