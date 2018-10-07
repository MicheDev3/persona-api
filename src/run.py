#!/usr/bin/env python
# coding=UTF-8

import os
import zipfile

import settings

import logging.config

from flask import Flask

from api.v1.routes import v1

logging.config.dictConfig(settings.LOGGING)

app = Flask(__name__)

# registering the version 1 api as a blueprint
app.register_blueprint(v1, url_prefix='/api/v1')


@app.before_first_request
def setup_data():
    # as required the fake_profiles.zip is unziped in runtime
    path = settings.BASEPATH + '/assets/fake_profiles.zip'

    if not os.path.isfile(path):
        return

    with zipfile.ZipFile(path, 'r') as zipped:
        zipped.extractall(settings.BASEPATH + '/assets')

    os.remove(path)


if __name__ == "__main__":
    # enabling tls for communications with the server using
    # a self signed certificate
    cert_path = settings.BASEPATH + '/assets/cert/'
    context = (cert_path + 'certificate.pem', cert_path + 'key.pem')
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT, ssl_context=context, threaded=True)
