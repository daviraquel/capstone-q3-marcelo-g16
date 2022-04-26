from flask import request, jsonify
from app.configs.database import db
from app.models.categories_model import CategoriesModel
      
def create_category():
  data = request.get_json()

  new_example = CategoriesModel(**data)

  db.session.add(new_example)
  db.session.commit()

  return jsonify(new_example), 201

def read_categories():
  #função para o método get
  return "read all"

def read_category(id):
  #função para o método get
  return "read one"

def update_category(id):
  # função para o método patch
  return "update"

def delete_category(id):
  # função para o delete
  return "delete"