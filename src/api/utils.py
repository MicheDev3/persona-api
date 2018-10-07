#!/usr/bin/env python
# coding=UTF-8

import hmac
import base64
import hashlib
import datetime

from functools import wraps

from schema import SchemaError

from flask import request, abort

from src import settings


#########################################
# Utils                                 #
#########################################
def check_permission(f):
    """
    Check request permission
    """
    def get_signature():
        """
        :return: signature to be matched against the request
        """
        # using a date plus a salt in order to create the raw string
        raw = datetime.date.today().strftime('%d/%m/%Y') + u"#persona#api#"
        digest = hmac.new(
            settings.SECRET_KEY, raw.encode('utf-8'), hashlib.sha256
        ).digest()
        return base64.b64encode(digest).decode()

    @wraps(f)
    def decorated(*args, **kwargs):
        signature = request.headers.get('Authorization', None)
        if not signature or signature != get_signature():
            abort(403)
        return f(*args, **kwargs)

    return decorated
#########################################


#########################################
# Base Validator                        #
#########################################
class Validator(object):
    """
    Base class for validating data
    """

    def __init__(self, data, method):
        self._data = data
        self._method = method

    def validator(self):
        raise NotImplementedError

    def _run_validation(self):
        if not self._data:
            raise SchemaError("No data provided")
        return self.validator().validate(self._data)

    def is_valid(self):
        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self._run_validation()
            except SchemaError as exc:
                self._validated_data = {}
                self._errors = exc.code
            else:
                self._errors = {}

        return not bool(self._errors)

    @property
    def method(self):
        return self._method

    @property
    def validated_data(self):
        if not hasattr(self, '_validated_data'):
            msg = 'You must call `.is_valid()` before accessing `.validated_data`.'
            raise AssertionError(msg)
        return self._validated_data

    @property
    def errors(self):
        if not hasattr(self, '_errors'):
            msg = 'You must call `.is_valid()` before accessing `.errors`.'
            raise AssertionError(msg)
        return self._errors
#########################################


#########################################
# Base View                             #
#########################################
class View(object):

    def __init__(self, data, method):
        self._method = method
        self._data = self.get_data(data)

    def get_data(self, data):
        raise NotImplementedError

    def behaviour(self):
        raise NotImplementedError

    def execute(self):
        return self.behaviour()

#########################################
