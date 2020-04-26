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
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)


    def create_period_table(self, connection):
        try:
            c = connection.cursor()
            c.execute('''
                      CREATE TABLE periods
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, name_id INTEGER, work_time INTEGER)''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if (connection):
                connection.close()
