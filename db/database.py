#! /usr/bin/python3

import sqlite3


# Documentation: https://docs.python.org/3/library/sqlite3.html

class DatabaseModule:


    def __init__(self):
        self.db_name = "database.db"


    '''
    Creates connection to database and returns the connection (if db doesn't exist, creates it)
    '''
    def create_connection(self):
        conn = sqlite3.connect(self.db_name)
        conn.close()
