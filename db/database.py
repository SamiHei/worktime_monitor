#! /usr/bin/python3

import sqlite3


# Documentation: https://docs.python.org/3/library/sqlite3.html
# TODO: error logging to file?

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
    Select statement to get all the saved periods
    '''
    def get_periods(self):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('SELECT * FROM periods;')
            periods = c.fetchall()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()
            con.close()

        return periods


    '''
    Insert statement for period to periods table
    '''
    def insert_period(self, period, period_name_id):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('''
                      INSERT INTO periods (date, name_id, work_time)
                      VALUES(?, ?, ?);''', (str(period.get_date()), period_name_id, str(period.get_work_time())))
            con.commit()
        except sqlite3.Error:
            raise sqlite3.Error
        finally:
            c.close()
            con.close()


    '''
    Update existing periods work_time
    '''
    def update_period(self, period, period_name_id):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('UPDATE periods SET work_time=work_time + ? WHERE date=? AND name_id=?;',
                      (period.get_work_time(), period.get_date(), period_name_id))
            con.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()
            con.close()


    '''
    Insert statement for period name into period_names table
    '''
    def insert_period_name(self, period):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('''
                      INSERT INTO period_names (period_name)
                      VALUES(?);''', (period.get_name(),))
            con.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()
            con.close()


    def get_period_name_by_id(self, period_name_id):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('SELECT period_name FROM period_names WHERE name_id=?', (period_name_id,))
            period_name = c.fetchone()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()
            con.close()

        return period_name


    '''
    Select statement to get period_name_id by period_name
    '''
    def get_period_name_id(self, period):
        try:
            con = self.create_connection()
            c = con.cursor()
            c.execute('SELECT name_id FROM period_names WHERE period_name=?', (period.get_name(),))
            period_name_id = c.fetchone()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()
            con.close()

        return period_name_id


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
                      (date DATE, 
                       name_id INTEGER, 
                       work_time INTEGER, 
                       PRIMARY KEY (date, name_id),
                       FOREIGN KEY(name_id) REFERENCES period_names(name_id));''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()


    '''
    Creates table for period names and links with relation to period table using name_id
    '''
    def create_period_names_table(self, connection):
        try:
            c = connection.cursor()
            c.execute('''
                      CREATE TABLE period_names
                      (name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      period_name TEXT UNIQUE);''')
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            c.close()

