from app.configs.database import db
from app.models.users_model import UsersModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


def create_user():
  session:Session = db.session
  
  data = request.get_json()

  expected_keys = ['user_name', 'email', 'password']
  entry_keys = [k for k in data.keys()]  
  try:
    for key in entry_keys:
      if key not in expected_keys:
        raise KeyError
  except:
    wrong_keys = []
    for key in entry_keys:
      if key not in expected_keys:
        wrong_keys.append(key)
    return {"error": "wrong keys",
            "expected_keys": expected_keys,
            "wrong_keys": wrong_keys}, 400

  data['user_name'] = data['user_name'].title()
  data['email'] = data['email'].lower() 
  
  user = UsersModel(**data)
  user.inserted_password = data['password']

  data['password']=user.password

  new_user = UsersModel(**data)
  try:

      db.session.add(new_user)
      db.session.commit()
  except IntegrityError as e:
      if type(e.orig) == UniqueViolation:
          return {"Error": "Username or email already in database"}, 409
  return jsonify(new_user), 201


# ========================================================================================
@jwt_required()
def read_users():
    session: Session = db.session
    users_list = session.query(UsersModel).all()

    if users_list == []:
        return {"Error": "There are no users on database"}, 404

    return jsonify(users_list), 200


# ========================================================================================
@jwt_required()
def read_user():
    session: Session = db.session

    user = get_jwt_identity()
    selected_user = UsersModel.query.get(user["id"])

    if not selected_user:
        return {"Error": "User not found"}, 404

    return jsonify(selected_user)


# ========================================================================================
@jwt_required()
def update_user(user_email:str):
  session:Session = db.session
  data = request.get_json()

  updatable_data = ['email', 'password', 'update_date']
  entry_keys = [k for k in data.keys()]  
  try:
    for key in entry_keys:
      if key not in updatable_data:
        raise KeyError
  except:
    wrong_keys = []
    for key in entry_keys:
      if key not in updatable_data:
        wrong_keys.append(key)
    return {"error": "data is not updatable",
            "updatable_data": updatable_data,
            "wrong_keys": wrong_keys}, 400

  data['email'] = data['email'].lower()

  now = datetime.utcnow()
  print('*'*100, now)
  data['update_date'] = now

  user = get_jwt_identity()
  selected_user = UsersModel.query.get(user["id"])
  if not selected_user:
    return{'Error':'User not found'}, 404
  
  for key, value in data.items():
    setattr(selected_user, key, value)
  
  try:
    session.add(selected_user)
    session.commit()
  except IntegrityError as e:
    if type(e.orig == UniqueViolation):
      return{'Error':'Email already exists'}, 409


# ========================================================================================
@jwt_required()
def delete_user():
    session: Session = db.session

    user = get_jwt_identity()

    selected_user = UsersModel.query.get(user["id"])

    if selected_user:
        session.delete(selected_user)
        session.commit()

        return "", 204

    return {"Error": "User not found"}, 404


# ========================================================================================
def login_user():
    data = request.get_json()

    user: UsersModel = UsersModel.query.filter_by(email=data["email"]).first()

    if not user or not user.check_password(data["password"]):
        return {"detail": "email and password missmatch"}, 401

    token = create_access_token(user, expires_delta=timedelta(minutes=30))

    return {"access_token": token}, 200
