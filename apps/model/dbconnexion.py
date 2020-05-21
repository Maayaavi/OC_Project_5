#! /usr/bin/env python3
# coding: utf-8

from settings import *
import pymysql


class SQLconnexion(object):
    """ Context Manager for SQL connexion into the database """

    def __init__(self):
        self.host = HOST
        self.user = USERNAME
        self.pw = PASSWORD
        self.db = DATABASE
        self.con = None

    def __enter__(self):
        self.con = pymysql.connect(host=self.host, user=self.user,
                                   passwd=self.pw, db=self.db, charset='utf8mb4')
        return self.con

    def __exit__(self, type, value, traceback):
        self.con.close()
