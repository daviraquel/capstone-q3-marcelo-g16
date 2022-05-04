from flask import request, jsonify
from app.configs.database import db
from app.models.categories_model import CategoriesModel
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from flask_jwt_extended import jwt_required


@jwt_required()
def create_category():
    session: Session = db.session

    data = request.get_json()
    data["name"] = data["name"].title()

    expected_keys = ["name", "description"]
    entry_keys = [k for k in data.keys()]

    if not expected_keys == entry_keys:
        return {"msg": {"expected keys": expected_keys, "entry keys": entry_keys}}, 400

    new_category = CategoriesModel(**data)

    try:
        db.session.add(new_category)
        db.session.commit()
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {"Error": "Category already on database"}, 409

    return jsonify(new_category), 201


# ========================================================================================
def read_categories():
    session: Session = db.session

    categories = session.query(CategoriesModel).all()

    if not categories:
        return {"Error": "There are no categories on database"}, 404

    return jsonify(categories), 200


# ========================================================================================
def read_category(name: str):
    session: Session = db.session

    category = (
        session.query(CategoriesModel)
        .filter(CategoriesModel.name == name.title())
        .first()
    )

    if not category:
        return {"Error": "Category not found"}, 404

    return jsonify(category), 200


# ========================================================================================
@jwt_required()
def update_category(name: str):

    session: Session = db.session
    data = request.get_json()
    keys = [k for k in data.keys()]

    selected_category = (
        session.query(CategoriesModel)
        .filter(CategoriesModel.name == name.title())
        .first()
    )
    print("@" * 100, selected_category)
    if not selected_category:
        return {"Error": "Category not found"}, 404

    try:
        if data["description"]:

            selected_category.description = data["description"]

            session.add(selected_category)
            session.commit()

            return jsonify(selected_category), 200
    except KeyError:
        return {"msg": {"expected key": "description", "entry keys": keys}}
    return "update"


# ========================================================================================
@jwt_required()
def delete_category(name):
    session: Session = db.session

    selected_category = selected_category = (
        session.query(CategoriesModel)
        .filter(CategoriesModel.name == name.title())
        .first()
    )
    if not selected_category:
        return {"Error": "Category not found"}, 404

    session.delete(selected_category)
    session.commit()

    return "", 204
