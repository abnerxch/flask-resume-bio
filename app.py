import sys
import yaml
from flask import Flask, render_template, jsonify, request, url_for, redirect
import io, json, os
import  datetime, time

app = Flask(__name__)

try:
    app.config['GA_TRACKING_ID'] = os.environ['GA_TRACKING_ID']
except:
    print('Tracking ID not set')

with open('info.yml') as stream:
    d = yaml.safe_load(stream)

info = d['info']

@app.route('/')
def index():
    age = int((datetime.date.today() - datetime.date(1995, 4, 22)).days / 365)
    return render_template('home.html', age=age)

@app.route('/info')
def info():
    return render_template("layout.html")

@app.route("/academica")
def academica():
    #return '{name}@{age}:{email}'.format(**d['info'])
    return render_template("academica.html")

@app.route('/laboral')
def laboral():
    return render_template("laboral.html")

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

if __name__ == '__main__':
        app.run(debug=True)