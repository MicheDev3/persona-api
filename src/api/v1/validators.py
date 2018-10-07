#!/usr/bin/env python
# coding=UTF-8

from schema import Schema, Optional

from src.api.utils import Validator

__all__ = ['SearchValidator', 'PeopleValidator']


#########################################
# Validators                            #
#########################################
class SearchValidator(Validator):
    """
    Search API Validator
    """

    mapping = {'GET': {'username': basestring}}

    def validator(self):
        return Schema(self.mapping[self.method])


class PeopleValidator(Validator):
    """
    People API Validator
    """

    mapping = {'DELETE': {'username': basestring},
               'GET': {'offset': basestring, Optional('limit', default="20"): basestring}}

    def validator(self):
        return Schema(self.mapping[self.method])
#########################################
