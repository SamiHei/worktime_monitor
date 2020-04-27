#! /usr/bin/python3

import sqlite3


# Documentation: https://docs.python.org/3/library/sqlite3.html

class DatabaseModule:


    def __init__(self, db_name):
        self.db_name = db_name


    '''
    Creates connection to database and returns the connection (if db doesn't exist, creates it)
    '''
    def create_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)


    '''
    Insert statement for period
    
    TODO: period name id 
    '''
    def insert_period(self, period):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('''
                      INSERT INTO periods(date, name_id, work_time)
                      VALUES(?, ?, ?);''', (str(period.get_date()), 1, str(period.get_work_time())))
            con.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            con.close()


    '''
    TODO: This doesn't work yet!
    '''
    def insert_period_name(self, period):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('''
                      INSERT INTO period_names(id, period_name)
                      VALUES(?);''', period.get_name())
            con.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            con.close()



    '''
    Creates the database on the first start
    '''
    def create_database(self, connection):
        try:
            self.create_periods_table(connection)
            self.create_period_names_table(connection)
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()


    '''
    Creates table for period data structures
    '''
    def create_periods_table(self, connection):
        try:
            c = connection.cursor()
            c.execute('''
                      CREATE TABLE periods
                      (date DATE, name_id INTEGER, work_time INTEGER, PRIMARY KEY (date, name_id));''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)


    '''
    Creates table for period names and links with relation to period table using name_id
    '''
    def create_period_names_table(self, connection):
        try:
            c = connection.cursor()
            c.execute('''
                      CREATE TABLE period_names
                      (name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      period_name TEXT,
                      FOREIGN KEY(name_id) REFERENCES periods(name_id));''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)
