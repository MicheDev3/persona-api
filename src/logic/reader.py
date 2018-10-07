#!/usr/bin/env python
# coding=UTF-8

import pandas

from src import settings


class Reader(object):

    def __init__(self, path):
        self._path = settings.BASEPATH + path

    def _open(self):
        # lazy initialization
        self._dataset = pandas.read_json(self._path)

    def _save(self):
        with open(self._path, "w") as data:
            data.write(self._dataset.to_json())

    def read(self, offset, limit):
        if not hasattr(self, '_dataset'):
            self._open()

        offset = int(offset)
        limit = int(offset) + int(limit)
        return self._dataset.query('index > %s & index < %s' % (offset, offset + limit)).to_dict('records')

    def search(self, key, value):
        if not hasattr(self, '_dataset'):
            self._open()

        return self._dataset.query('%s=="%s"' % (key, value)).to_dict('records')

    def delete(self, key, value):
        if not hasattr(self, '_dataset'):
            self._open()

        previous = len(self._dataset)
        self._dataset = self._dataset[
            getattr(self._dataset, key) != value
        ]

        self._save()

        return "%s user(s) with %s equals to %s deleted" % (previous - len(self._dataset), key, value)
