from app.configs.database import db
from app.models.users_model import UsersModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime


def create_user():
  session:Session = db.session
  
  data = request.get_json()
  data['user_name'] = data['user_name'].title()
  data['email'] = data['email'].lower()

  expected_keys = ['user_name', 'email', 'password']
  entry_keys = [k for k in data.keys()]

  if not expected_keys==entry_keys:
    return {'msg':{'expected keys':expected_keys, 'entry keys':entry_keys}}, 400


  new_user = UsersModel(**data)
  
  try:

    db.session.add(new_user)
    db.session.commit()
  except IntegrityError as e:
    if type(e.orig) == UniqueViolation:
      return {'Error':'Username or email already in database'}, 409
  return jsonify(new_user), 201


#========================================================================================
def read_users():
  session:Session = db.session
  users_list = session.query(UsersModel).all()

  if users_list == []:
        return{'Error':'There are no users on database'}, 404

  return jsonify(users_list), 200


#========================================================================================
def read_user(user_email:str):
  session:Session = db.session

  selected_user = session.query(UsersModel).filter(UsersModel.email==user_email.lower()).first()
  if not selected_user:
    return{'Error':'User not found'}, 404
  
  return jsonify(selected_user)


#========================================================================================
def update_user(user_email:str):
  session:Session = db.session
  data = request.get_json()
  data['email'] = data['email'].lower()

  now = datetime.utcnow()
  print('*'*100, now)
  data['update_date'] = now

  selected_user = session.query(UsersModel).filter(UsersModel.email==user_email.lower()).first()
  if not selected_user:
    return{'Error':'User not found'}, 404
  
  updatable_data = ['email', 'password', 'update_date']
  for key, value in data.items():
    if key in updatable_data:
      setattr(selected_user, key, value)
  
  try:
    session.add(selected_user)
    session.commit()
  except IntegrityError as e:
    if type(e.orig == UniqueViolation):
      return{'Error':'Email already exists'}, 409
      
  return jsonify(selected_user), 200


#========================================================================================
def delete_user(user_email:str):
  session:Session = db.session
  selected_user = session.query(UsersModel).filter(UsersModel.email==user_email).first()
  if not selected_user:
    return{'Error':'User not found'}, 404
  session.delete(selected_user)
  session.commit()

  return "", 204
