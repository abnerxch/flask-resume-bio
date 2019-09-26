#!/usr/bin/env python
from readInfo import readData
from flask import Flask, jsonify
import sys
import yaml

app = Flask(__name__)


@app.route('/', methods='GET')
def admin():
    os2 = lectura.d['os2']
    # "concatenate" host, ip and path
    print('{host}@{ip}:{path}'.format(**lectura.d['os2']))

if __name__ == '__main__':
    app.run(debug=True)