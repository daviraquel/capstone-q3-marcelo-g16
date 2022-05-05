from flask import request, jsonify
from app.configs.database import db
from sqlalchemy.orm import Session
from app.models.nfts_model import NftsModel
from sqlalchemy.exc import DataError, ProgrammingError, IntegrityError
from psycopg2.errors import ForeignKeyViolation, NotNullViolation
from http import HTTPStatus
from copy import deepcopy
from flask_jwt_extended import get_jwt_identity, jwt_required


session: Session = db.session


@jwt_required()
def create_nft():
    user = get_jwt_identity()
    data = request.get_json()

    expected_keys = ["name", "value", "for_sale", "description", "image", "collection"]
    entry_keys = [k for k in data.keys()]

    try:
        for key in entry_keys:
            if key not in expected_keys:
                raise KeyError

        data["description"] = data["description"].lower()

        data["creator"] = user["id"]
        data["owner"] = user["id"]

        new_nft = NftsModel(**data)

        session.add(new_nft)
        session.commit()

        return jsonify(new_nft), HTTPStatus.OK
    except IntegrityError as e:
        if type(e.orig) == ForeignKeyViolation:
            return {
                "error": "insert a collection already registered."
            }, HTTPStatus.BAD_REQUEST
        return {
            "error": "wrong keys",
            "expected_keys": expected_keys,
        }, HTTPStatus.BAD_REQUEST

    except KeyError:
        wrong_keys = []
        for key in entry_keys:
            if key not in expected_keys:
                wrong_keys.append(key)
        return {
            "error": "wrong keys",
            "expected_keys": expected_keys,
            "wrong_keys": wrong_keys,
        }, HTTPStatus.BAD_REQUEST


##################################################################################################################
def read_nfts():
    try:
        read_all = session.query(NftsModel).all()

        return jsonify(read_all), HTTPStatus.OK
    except:
        return [], HTTPStatus.OK


##################################################################################################################
def read_nft(id):
    read_one = session.query(NftsModel).filter(NftsModel.id == id).first()
    
    if read_one:
        return jsonify(read_one), HTTPStatus.OK
    else:
        return {"error": f"ntf id {id} not found"}, HTTPStatus.NOT_FOUND


##################################################################################################################
@jwt_required()
def update_nft(id):
    user = get_jwt_identity()
    try:
        data = request.get_json()

        acepted_keys = ["value", "for_sale", "description", "image"]
        wrong_keys = []

        if not data:
            raise KeyError

        for key in data.keys():
            if (
                key != "value"
                and key != "for_sale"
                and key != "description"
                and key != "image"
            ):
                wrong_keys.append(key)
                raise KeyError

        wanted_nft = session.query(NftsModel).get(id)
        for key, value in data.items():
            setattr(wanted_nft, key, value)

        if user["id"] != wanted_nft.creator_info.id:
            return {
                "detail": "only the creator of the NFT can update"
            }, HTTPStatus.UNAUTHORIZED

        session.add(wanted_nft)
        session.commit()

        return jsonify(wanted_nft), HTTPStatus.CREATED

    except KeyError:
        return {
            "error": {"expected_keys": acepted_keys, "received": wrong_keys}
        }, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"error": f"nft id {id} not found"}, HTTPStatus.NOT_FOUND
    except (DataError, ProgrammingError):
        return {"error": f"correct the values passed"}, HTTPStatus.BAD_REQUEST


##################################################################################################################
@jwt_required()
def delete_nft(id):
    user = get_jwt_identity()
    try:
        delete_one = session.query(NftsModel).get(id)

        if user["id"] != delete_one.creator_info.id:
            return {
                "detail": "only the creator of the NFT can delete"
            }, HTTPStatus.UNAUTHORIZED

        session.delete(delete_one)
        session.commit()

        return "", HTTPStatus.NO_CONTENT
    except:
        return {"error": f"nft id {id} not found"}, HTTPStatus.NOT_FOUND
