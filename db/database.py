#! /usr/bin/python3

import sqlite3


class DatabaseModule:


    def __init__(self, db_name):
        self.db_name = db_name


    """
    Creates connection to database and returns the connection (if db doesn't exist, creates it)
    
    Excepts sqlite3 Error
    """
    def create_connection(self):
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)


    '''
    Decorator function for SELECT statements

    Wraps connection and close to this function which is used in every insert

    Arguments:
        *args = Values to be given for the statement

    Returns:
        Data from the SELECT statement
    '''
    def get_data_decor(func):
        def wrapper(self, *args):
            try:
                con = self.create_connection()
                c = con.cursor()
                data = func(self, c, *args)
                return data
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
                con.close()
        return wrapper


    """
    Select statement to get all the saved periods
    """
    @get_data_decor
    def get_periods(self, c):
        c.execute('SELECT * FROM periods;')
        return c.fetchall()


    """
    Get period names from period_names table by using period name id

    period_name_id : int, id of the searched period name
    """
    @get_data_decor
    def get_period_name_by_id(self, c, period_name_id):
        c.execute('SELECT period_name FROM period_names WHERE name_id=?;', (period_name_id,))
        return c.fetchone()


    """
    Select statement to get period_name_id by period_name

    period : Period, where the periods name id is taken
    """
    @get_data_decor
    def get_period_name_id(self, c, period):
        c.execute('SELECT name_id FROM period_names WHERE period_name=?;', (period.get_name(),))
        return c.fetchone()


    '''
    Decorator function for INSERT and UPDATE statements

    Wraps connection, commit and close to this function which is used in every insert

    Arguments:
        *args = Values to be given for the statement
    '''
    def insert_data_decor(func):
        def wrapper(self, *args):
            try:
                con = self.create_connection()
                c = con.cursor()
                func(self, c, *args)
                con.commit()
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
                con.close()
        return wrapper


    """
    Insert statement for period to periods table

    period : Period, period to be added to database
    period_name_id : int, id of the periods name
    """
    @insert_data_decor
    def insert_period(self, c, period, period_name_id):
        c.execute('''
                  INSERT INTO periods (date, name_id, work_time)
                  VALUES(?, ?, ?);''', (str(period.get_date()), period_name_id, str(period.get_work_time())))


    """
    Insert statement for period name into period_names table

    period : Period, period where the period name is taken to be inserted in the period_names table
    """
    @insert_data_decor
    def insert_period_name(self, c, period):
        c.execute('''
                  INSERT INTO period_names (period_name)
                  VALUES(?);''', (period.get_name(),))


    """
    Update existing periods work_time

    period : Period, period to be updated in the database
    period_name_id : int, id of the periods name
    """
    @insert_data_decor
    def update_period(self, c, period, period_name_id):
        c.execute('UPDATE periods SET work_time=work_time + ? WHERE date=? AND name_id=?;',
                  (period.get_work_time(), period.get_date(), period_name_id))


    def create_table_decor(func):
        def wrapper(self, *args):
            try:
                c = self.create_connection()
                func(self, c, *args)
                c.commit()
            except sqlite3.Error as e:
                print(e)
            finally:
                c.close()
        return wrapper


    """
    Creates table for period data structures

    connection : sqlite3.connect, creates periods table to database
    """
    @create_table_decor
    def create_periods_table(self, connection, c):
        c.execute('''
                  CREATE TABLE periods
                  (date DATE, 
                   name_id INTEGER, 
                   work_time INTEGER, 
                   PRIMARY KEY (date, name_id),
                   FOREIGN KEY(name_id) REFERENCES period_names(name_id));''')


    """
    Creates table for period names and links with relation to period table using name_id

    connection : sqlite3.connect, creates period names table to database
    """
    @create_table_decor
    def create_period_names_table(self, connection, c):
            c.execute('''
                      CREATE TABLE period_names
                      (name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      period_name TEXT UNIQUE);''')


    """
    Creates the database on the first start

    connection : sqlite3.connect, creates database using connection
    """
    def create_database(self, connection):
        try:
            self.create_periods_table(connection)
            self.create_period_names_table(connection)
        except sqlite3.Error as e:
            print(e)
        finally:
            connection.close()







