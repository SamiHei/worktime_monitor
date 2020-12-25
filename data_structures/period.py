#! /usr/bin/python3


from datetime import date


"""
This class presents working period which saves the date and the time 

    date is presented in the format of DD.MM.YYYY
    work_time is presented in seconds    
"""
class Period:


    def __init__(self):
        self.name = None
        self.date = date.today()
        self.work_time = 0

    
    def create_period_from_db(self, db_period_data, period_name):
        self.set_name(period_name)
        self.set_date(db_period_data[0])
        self.set_work_time(db_period_data[2])


    def get_date(self):
        return self.date


    def get_work_time(self):
        return self.work_time

        
    def set_date(self, date):
        self.date = date


    # Time worked in seconds
    def set_work_time(self, work_time):
        self.work_time = work_time


    def get_period(self):
        return self.date, self.work_time


    def set_name(self, name):
        self.name = name.lower().strip()


    def get_name(self):
        return self.name

