import yaml
from flask import *

class readData():
        with open("info.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        for section in cfg:
            print(section)
        print(cfg['mysql'])
        print(cfg['other'])