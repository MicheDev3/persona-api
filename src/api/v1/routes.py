#!/usr/bin/env python
# coding=UTF-8

from flask import Blueprint, request, jsonify

from views import *
from validators import *

from src.api.utils import check_permission


v1 = Blueprint("v1", __name__)


@v1.route('/search', methods=['GET'])
@check_permission
def search():
    validator = SearchValidator(request.args.to_dict(), request.method)
    if validator.is_valid():
        data = SearchView(validator.validated_data, request.method).execute()
        return jsonify({'data': data}), 200

    errors = validator.errors
    return jsonify({'errors': errors}), 400


@v1.route('/people', methods=['GET', 'DELETE'])
@check_permission
def people():
    validator = PeopleValidator(request.args.to_dict(), request.method)
    if validator.is_valid():
        data = PeopleView(validator.validated_data, request.method).execute()
        return jsonify({'data': data}), 200

    errors = validator.errors
    return jsonify({'errors': errors}), 400
