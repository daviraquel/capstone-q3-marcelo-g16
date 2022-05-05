from http import HTTPStatus

from app.configs.database import db
from app.models.nfts_model import NftsModel
from app.models.sales_model import SalesModel
from app.models.users_model import UsersModel
from app.modules import only_allowed_fields, set_wrong_fields
from flask import jsonify, request
from sqlalchemy.orm import Session
from flask_jwt_extended import get_jwt_identity, jwt_required

fields = ["item"]

session: Session = db.session

@jwt_required()
def create_sale():    
    data = request.get_json()

    #verificação de chaves da requisição
    try:
        missing_fields = [key for key in fields if key not in data.keys()]
        wrong_fields = set_wrong_fields(data, [], fields[:3])

        if missing_fields or wrong_fields:
            raise KeyError
    except KeyError:
        if missing_fields:
            return {"missing_fields": missing_fields}, HTTPStatus.BAD_REQUEST
        if wrong_fields:
            return {"wrong_fields": wrong_fields}, HTTPStatus.BAD_REQUEST

    #verificação da existencia da nft a ser vendida
    try:
        sold_nft = session.query(NftsModel).get(data["item"])
        if not sold_nft:
            raise ValueError
    except:
        return {"error": "item not found"}, HTTPStatus.NOT_FOUND

    buyer_dict = get_jwt_identity()
    buyer = session.query(UsersModel).get(buyer_dict["id"])
    seller = session.query(UsersModel).get(sold_nft.owner)

    # verificação se o comprador já não possui o item 
    try:    
        if buyer.id == seller.id:
            raise ValueError
    except:
        return {"error": "you already own this item"}, HTTPStatus.BAD_REQUEST
    
    #verificação se o comprador possui saldo suficiente e atualização dos saldos
    try:
        if sold_nft.value > buyer.balance:
            raise ValueError
        minus = float(buyer.balance) - float(sold_nft.value)
        setattr(buyer, "balance", minus)
        plus = float(seller.balance) + float(sold_nft.value)
        setattr(seller, "balance", plus)
        setattr(sold_nft, "owner", buyer.id)
        setattr(sold_nft, "for_sale", False)
    except:
        return {"error": f"balance not enough, your account balance is: {buyer.balance}"}, HTTPStatus.BAD_REQUEST

    sale_data ={
        "seller": seller.id,
        "buyer": buyer.id,
        "item": data["item"],
        "value": sold_nft.value,
    }

    new_sale = SalesModel(**sale_data)

    session.add(buyer)
    session.add(seller)
    session.add(sold_nft)
    session.add(new_sale)
    session.commit()

    return jsonify(new_sale), HTTPStatus.CREATED



def read_sales():
    sales = SalesModel.query.all()

    return jsonify(sales), HTTPStatus.OK


def read_sale(id):
    sale = SalesModel.query.filter_by(id=id).first()

    if not sale:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    return jsonify(sale), HTTPStatus.OK


def update_sale(id):
    sale = SalesModel.query.filter_by(id=id).first()

    if not sale:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    data = request.get_json()
    not_allowed_fields = only_allowed_fields(data, fields)
    wrong_fields = set_wrong_fields(data, [], fields[:3])

    if not_allowed_fields:
        return not_allowed_fields, HTTPStatus.BAD_REQUEST

    elif wrong_fields:
        return {"wrong_fields": wrong_fields}, HTTPStatus.BAD_REQUESTfields[:2]

    SalesModel.query.filter_by(id=id).update(data)

    session.commit()

    sale = SalesModel.query.filter_by(id=id).first()

    return jsonify(sale), HTTPStatus.OK


def delete_sale(id):
    sale = SalesModel.query.filter_by(id=id).first()

    if not sale:
        return {"error": "not found"}, HTTPStatus.NOT_FOUND

    session.delete(sale)
    session.commit()

    return {}, HTTPStatus.NO_CONTENT
