#!/usr/bin/env python
# coding=UTF-8

from src.api.utils import View

from src.logic.reader import Reader

__all__ = ['SearchView', 'PeopleView']


#########################################
# Persona Views                         #
#########################################
class SearchView(View):

    methods = {'GET': 'search'}

    def get_data(self, data):
        return {'key': 'username', 'value': data['username']}

    def behaviour(self):
        reader = Reader('/assets/fake_profiles.json')
        method = getattr(reader, self.methods[self._method])
        return method(**self._data)


class PeopleView(View):

    methods = {'GET': 'read', 'DELETE': 'delete'}

    def get_data(self, data):
        if self._method == 'GET':
            return {'offset': data['offset'], 'limit': data['limit']}
        elif self._method == 'DELETE':
            return {'key': 'username', 'value': data['username']}

    def behaviour(self):
        reader = Reader('/assets/fake_profiles.json')
        method = getattr(reader, self.methods[self._method])
        return method(**self._data)
#########################################
