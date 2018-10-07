#!/usr/bin/env python
# coding=UTF-8

import logging

import pandas

from src import settings

logger = logging.getLogger(__name__)


#########################################
# Reader class                          #
#########################################
class Reader(object):
    """
        This class will manage the persona data for reading or deleting
    """

    def __init__(self, path):
        self._path = settings.BASEPATH + path

    def _open(self):
        # lazy initialization
        logger.debug("Opening with pandas the json")
        self._dataset = pandas.read_json(self._path)

    def _save(self):
        logger.debug("Saving change into dataset")
        with open(self._path, "w") as data:
            data.write(self._dataset.to_json())

    def read(self, offset, limit):
        # if the object is still in memory
        # no need to open the data again
        if not hasattr(self, '_dataset'):
            self._open()

        start = int(offset)
        end = int(offset) + int(limit)
        logger.debug("Reading dataset: limit %s, offset %s" % (limit, offset))
        return self._dataset.query('index > %s & index < %s' % (start, end)).to_dict('records')

    def search(self, key, value):
        # if the object is still in memory
        # no need to open the data again
        if not hasattr(self, '_dataset'):
            self._open()

        logger.debug("Searching using key %s and value %s" % (key, value))
        return self._dataset.query('%s=="%s"' % (key, value)).to_dict('records')

    def delete(self, key, value):
        # if the object is still in memory
        # no need to open the data again
        if not hasattr(self, '_dataset'):
            self._open()

        previous = len(self._dataset)
        self._dataset = self._dataset[
            getattr(self._dataset, key) != value
        ]

        self._save()

        logger.debug("Deleting using key %s and value %s" % (key, value))
        return "%s user(s) with %s equals to %s deleted" % (previous - len(self._dataset), key, value)
#########################################
