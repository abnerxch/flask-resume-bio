import sys
import yaml
from flask import Flask, render_template, jsonify, request, url_for, redirect
import io, json, os
import  datetime, time

app = Flask(__name__)

#try:
 #   app.config['GA_TRACKING_ID'] = os.environ['GA_TRACKING_ID']
#except:
 #   print('Tracking ID not set')

#with open('info.yml') as stream:
data = yaml.load(open('info.yml'))

print(data['myname'])

#info = data['info']

@app.route('/')
def index():
    age = int((datetime.date.today() - datetime.date(1997, 9, 29)).days / 365)
    return render_template('home.html', data = data)

@app.route('/estudios')
def estudios():
    return render_template("estudios.html")

@app.route("/experiencia")
def experiencia():
    #return '{name}@{age}:{email}'.format(**d['info'])
    return render_template("experiencia.html")

@app.route('/about')
def about():
    age = int((datetime.date.today() - datetime.date(1997, 9, 29)).days / 365)
    return render_template("about.html", data = data)

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")

if __name__ == '__main__':
        app.run(debug=True)