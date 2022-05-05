from flask import request, jsonify
from app.configs.database import db
from app.models.collections_model import CollectionsModel
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def create_collection():
    user = get_jwt_identity()
    data = request.get_json()

    expected_keys = ["name", "description"]
    entry_keys = [k for k in data.keys()]

    if not expected_keys == entry_keys:
        return {"msg": {"expected keys": expected_keys, "entry keys": entry_keys}}, 400

    data["name"] = data["name"].title()
    data["creator"] = user["id"]
    new_collection = CollectionsModel(**data)

    try:
        db.session.add(new_collection)
        db.session.commit()
    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {"Error": "Collection already on database"}, 409

    return jsonify(new_collection), 201


# ========================================================================================
def read_collections():
    session: Session = db.session

    collections = session.query(CollectionsModel).all()

    if collections == []:
        return {"Error": "There are no collections on database"}, 404

    return jsonify(collections), 200


# ========================================================================================
def read_collection(name):
    session: Session = db.session

    collection = (
        session.query(CollectionsModel)
        .filter(CollectionsModel.name == name.title())
        .first()
    )

    if not collection:
        return {"Error": "Collection not found"}, 404

    return jsonify(collection), 200


# ========================================================================================
@jwt_required()
def update_collection(name):
    session: Session = db.session
    user = get_jwt_identity()
    data = request.get_json()
    keys = [k for k in data.keys()]

    selected_collection = (
        session.query(CollectionsModel)
        .filter(CollectionsModel.name == name.title())
        .first()
    )

    if not selected_collection:
        return {"Error": "Collection not found"}, 404

    if user["id"] != selected_collection.id:
        return {"detail": "only the creator of the collection can update"}, 401

    try:
        if data["description"]:
            selected_collection.description = data["description"]

            session.add(selected_collection)
            session.commit()

            return jsonify(selected_collection), 200
    except KeyError:
        return {"msg": {"expected key": "description", "entry keys": keys}}, 400


# ========================================================================================
@jwt_required()
def delete_collection(name):
    session: Session = db.session
    user = get_jwt_identity()

    selected_collection = selected_collection = (
        session.query(CollectionsModel)
        .filter(CollectionsModel.name == name.title())
        .first()
    )
    if not selected_collection:
        return {"Error": "Collection not found"}, 404

    if user["id"] != selected_collection.id:
        return {"detail": "only the creator of the collection can update"}, 401

    session.delete(selected_collection)
    session.commit()

    return "", 204
