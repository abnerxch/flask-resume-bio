from readInfo import readData
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def admin():
    for section in readData.cfg:
        return jsonify(section)

if __name__ == '__main__':
    app.run(debug=True)