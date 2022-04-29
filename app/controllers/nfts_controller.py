from flask import request, jsonify
from app.configs.database import db
from app.models.nfts_model import NftsModel
      
def create_nft():
  data = request.get_json()

  new_example = NftsModel(**data)

  db.session.add(new_example)
  db.session.commit()

  return jsonify(new_example), 201

def read_nfts():
  #função para o método get
  return "read all"

def read_nft(id):
  #função para o método get
  return "read one"

def update_nft(id):
  # função para o método patch
  return "update"

def delete_nft(id):
  # função para o delete
  return "delete"