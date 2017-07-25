from flask import Flask
from pymongo import MongoClient

from app.conf.config import sys_config

client = MongoClient(sys_config['database']['db_host'])
db_connect = client[sys_config['database']['db_name']]
app = Flask(__name__)
