from flask import request, jsonify
from app.configs.database import db
from app.models.collections_model import CollectionsModel
      
def create_collection():
  data = request.get_json()

  new_example = CollectionsModel(**data)

  db.session.add(new_example)
  db.session.commit()

  return jsonify(new_example), 201

def read_collections(id):
  #função para o método get
  return "read all"

def read_collection(id):
  #função para o método get
  return "read one"

def update_collection(id):
  # função para o método patch
  return "update"

def delete_collection(id):
  # função para o delete
  return "delete"