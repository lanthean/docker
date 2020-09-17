#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   http://martinbortel.cz
# @Contact  me@martinbortel.cz
# @Created
#
# @Package Sudoku via evolutionary algorithms
"""

# Imports
import logging
from flask import Flask, render_template, request
from modules.db import DB

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def prepare_data():
    db = DB()
    db.connect()
    tables = db.query("SHOW TABLES;")
    # eo:prepare_data()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', tables=prepare_data())
    # eo:index()

# boilerplate code to run the main function if it is not a import..
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# EOF
###