#!/usr/bin/env python
# coding=UTF-8

import os


BASEPATH = os.path.dirname(os.path.abspath(__file__))

#########################################
# Server setting                        #
#########################################
HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])

DEBUG = os.environ['DEBUG'].upper() == "TRUE"

SECRET_KEY = os.environ['SECRET_KEY']
#########################################


#########################################
# Logging settings                      #
#########################################
LOG_LEVEL = os.environ['LOG_LEVEL'].upper()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(name)s] [%(process)d] [%(thread)d]: %(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s [%(name)s]: %(asctime)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
            'level': LOG_LEVEL,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': LOG_LEVEL,
        }
    },
    'loggers': {
        'flask': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARNING',
        },
        'persona-api': {
            'handlers': ['console'],
            'propagate': True,
            'level': LOG_LEVEL,
        },
    }
}
#########################################
