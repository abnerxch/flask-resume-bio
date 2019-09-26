import sys
import yaml
from flask import Flask, render_template

app = Flask(__name__)

with open('info.yml') as stream:
    d = yaml.safe_load(stream)

info = d['info']

@app.route('/')
def home():
    return render_template("info.html")

@app.route('/info')
def info():
    return render_template("info.html")

@app.route("/academica")
def academica():
    return '{name}@{age}:{email}'.format(**d['info'])

@app.route('/laboral')
def laboral():
    return 'laboral'

@app.route('/contacto')
def contacto():
    return 'contacto'

if __name__ == '__main__':
        app.run(debug=True)