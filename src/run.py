#!/usr/bin/env python
# coding=UTF-8

import os
import zipfile

import settings

from flask import Flask

from api.v1.routes import v1

app = Flask(__name__)

app.register_blueprint(v1, url_prefix='/api/v1')


@app.before_first_request
def setup_data():
    path = settings.BASEPATH + '/assets/fake_profiles.zip'

    if not os.path.isfile(path):
        return

    with zipfile.ZipFile(path, 'r') as zipped:
        zipped.extractall(settings.BASEPATH + '/assets')

    os.remove(path)


if __name__ == "__main__":
    cert_path = settings.BASEPATH + '/assets/cert/'
    context = (cert_path + 'certificate.pem', cert_path + 'key.pem')
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT, ssl_context=context, threaded=True)
