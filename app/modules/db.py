#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
# @Author   martin.bortel@gmail.com
# @Created  09/2020
#
# @Package Sudoku game generator via evolutionary algorithms
"""
import mysql.connector
import logging
import yaml

# Configure db
class DB():

    def __init__(self):
        self.connect()
        # eo:DB()

    def get_config(self):
        with open('./conf/db.yaml') as f:
            self.db_config = yaml.safe_load(f)
        print(self.db_config)
        # eo:get_config()

    def connect(self):
        self.get_config()
        try:
            self.mysql = mysql.connector.connect(**self.db_config)
        except mysql.connector.Error as e:
            raise e
        # eo:connect()

    def query(self, query):
        try:
            rs = self.cur.execute()
        except mysql.connector.Error as e:
            logging.error("MySQL connection failed: {}".format(e))
            return False
        else:
            return rs
        # eo:query()

    #eo:DB


class DBObject(DB):
    """docstring for DbObject"""
    def __init__(self, arg):
        super(DbObject,DB).__init__()
        self.arg = arg
        # eo:DbObject()
            
    # eo:DBObject
