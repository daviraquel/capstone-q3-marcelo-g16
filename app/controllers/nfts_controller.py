from flask import request, jsonify
from app.configs.database import db
from sqlalchemy.orm import Session
from app.models.nfts_model import NftsModel
from sqlalchemy.exc import DataError, ProgrammingError, IntegrityError
from psycopg2.errors import ForeignKeyViolation, NotNullViolation
from http import HTTPStatus
from copy import deepcopy

session: Session = db.session

def create_nft():
  try:
    data = request.get_json()

    data['description'] = data['description'].lower()

    new_nft = NftsModel(**data)

    session.add(new_nft)
    session.commit()

    return jsonify(new_nft), HTTPStatus.OK
  except IntegrityError as e:
    if type(e.orig) == ForeignKeyViolation:
      return {"error": "insert a creator, owner or collection that is already registered."}, HTTPStatus.BAD_REQUEST
    if type(e.orig) == NotNullViolation:
      acepted_keys = ['creator', 'owner','name','value', 'for_sale','description', 'image', 'collection']
      missing_keys = deepcopy(acepted_keys)
      for key in data.keys():
        if key in acepted_keys:
          missing_keys.remove(key)
      return {"error": {"mandatory keys": acepted_keys, 'missing keys': missing_keys}}, HTTPStatus.BAD_REQUEST

##################################################################################################################
def read_nfts():
  try:
    read_all = session.query(NftsModel).all()
  
    return jsonify(read_all),HTTPStatus.OK
  except: 
    return [], HTTPStatus.OK

##################################################################################################################
def read_nft(id):
  read_one = session.query(NftsModel).filter(NftsModel.id == id).first()
  if read_one:
    session.commit()
    return jsonify(read_one), HTTPStatus.OK
  else:
    return {"error": f"ntf id {id} not found"}, HTTPStatus.BAD_REQUEST

##################################################################################################################
def update_nft(id):
  try:
    data = request.get_json()
    acepted_keys = ['value', 'for_sale','description', 'image']
    wrong_keys = []

    for key in data.keys():
      if key != 'value' and key != 'for_sale' and key != 'description' and key != 'image': 
        wrong_keys.append(key)
        raise KeyError

    wanted_nft = session.query(NftsModel).get(id)
    for key, value in data.items():
      setattr(wanted_nft,key,value)

    session.add(wanted_nft)
    session.commit()

    return jsonify(wanted_nft), HTTPStatus.CREATED

  except KeyError:
    return {'error': {'correct keys': acepted_keys, 'received': wrong_keys}}, HTTPStatus.BAD_REQUEST
  except AttributeError:
    return {'error': f'nft id {id} not foud'}, HTTPStatus.BAD_REQUEST
  except (DataError, ProgrammingError):
    return {'error': f'correct the values passed'},HTTPStatus.BAD_REQUEST      

##################################################################################################################
def delete_nft(id):
  try:
    delete_one = session.query(NftsModel).get(id)
    session.delete(delete_one)
    session.commit()

    return "", HTTPStatus.NO_CONTENT
  except:
    return {'error': f'nft id {id} not found'}, HTTPStatus.BAD_REQUEST