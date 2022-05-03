from app.configs.database import db
from app.models.users_model import UsersModel
from flask import jsonify, request
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required


def create_user():
    session: Session = db.session

    data = request.get_json()
    data["user_name"] = data["user_name"].title()
    data["email"] = data["email"].lower()

    expected_keys = ["user_name", "email", "password"]
    entry_keys = [k for k in data.keys()]

    if not expected_keys == entry_keys:
        return {"msg": {"expected keys": expected_keys, "entry keys": entry_keys}}, 400

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
def update_user():
    session: Session = db.session
    data = request.get_json()
    data["email"] = data["email"].lower()

    # now = datetime.utcnow
    # print('*'*100, now)
    # data['update_date'] = now

    user = get_jwt_identity()
    selected_user = UsersModel.query.get(user["id"])

    if not selected_user:
        return {"Error": "User not found"}, 404

    updatable_data = ["email", "password", "update_date"]
    for key, value in data.items():
        if key in updatable_data:
            setattr(selected_user, key, value)

    try:
        session.add(selected_user)
        session.commit()
    except IntegrityError as e:
        if type(e.orig == UniqueViolation):
            return {"Error": "Email already exists"}, 409

    return jsonify(selected_user), 200


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
