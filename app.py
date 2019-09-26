import sys
import yaml
from flask import Flask

app = Flask(__name__)

with open('info.yml') as stream:
    d = yaml.safe_load(stream)

info = d['info']
# "concatenate" host, ip and path
print('{name}@{age}:{email}'.format(**d['info']))

@app.route('/')
def admin():
    return '{name}@{age}:{email}'.format(**d['info'])

if __name__ == '__main__':
        app.run(debug=True)