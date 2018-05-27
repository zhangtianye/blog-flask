#!/bin/python
#-*-coding:UTF-8-*-

from __future__ import unicode_literals
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'index!'

if __name__ == '__main__':
    # app.debug = True
    app.run(host="0.0.0.0")
