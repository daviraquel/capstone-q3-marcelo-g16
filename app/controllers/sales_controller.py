from http import HTTPStatus

from app.configs.database import db
from app.models.sales_model import SalesModel
from app.modules import only_allowed_fields, set_wrong_fields
from flask import jsonify, request
from sqlalchemy.orm import Session

fields = ["seller", "buyer", "item", "value"]

session: Session = db.session


def create_sale():
    try:
        data = request.get_json()
        missing_fields = [key for key in fields if key not in data.keys()]
        wrong_fields = set_wrong_fields(
            data,
            fields[:2],
            [fields[2]],
        )

        if missing_fields:
            raise KeyError

        elif wrong_fields:
            return {"wrong_fields": wrong_fields}, HTTPStatus.BAD_REQUEST

        new_sale = SalesModel(**data)

        session.add(new_sale)
        session.commit()

        return jsonify(new_sale), HTTPStatus.CREATED

    except KeyError:
        return {"missing_fields": missing_fields}, HTTPStatus.BAD_REQUEST


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
    wrong_fields = set_wrong_fields(
        data,
        fields[:2],
        [fields[2]],
    )

    if not_allowed_fields:
        return not_allowed_fields, HTTPStatus.BAD_REQUEST

    elif wrong_fields:
        return {"wrong_fields": wrong_fields}, HTTPStatus.BAD_REQUEST

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
