from flask import request, jsonify
from app.configs.database import db
from app.models.sales_model import SalesModel
      
def create_sale():
  data = request.get_json()

  new_example = SalesModel(**data)

  db.session.add(new_example)
  db.session.commit()

  return jsonify(new_example), 201

def read_sales():
  #função para o método get
  return "read all"

def read_sale(id):
  #função para o método get
  return "read one"

def update_sale(id):
  # função para o método patch
  return "update"

def delete_sale(id):
  # função para o delete
  return "delete"