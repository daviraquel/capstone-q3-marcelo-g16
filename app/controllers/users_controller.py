from flask import request, jsonify
from app.configs.database import db
from app.models.users_model import UsersModel
      
def create_user():
  data = request.get_json()

  new_example = UsersModel(**data)

  db.session.add(new_example)
  db.session.commit()

  return jsonify(new_example), 201

def read_users():
  #função para o método get
  return "read all"

def read_user(id):
  #função para o método get
  return "read one"

def update_user(id):
  # função para o método patch
  return "update"

def delete_user(id):
  # função para o delete
  return "delete"