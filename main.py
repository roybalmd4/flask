'''
    Pull data from AZMET each time the webpage is accessed.  The largest amount of rows that
    would be imported would be 24x365 (8760)
'''

import sqlalchemy
import psycopg2
import pandas as pd 
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'