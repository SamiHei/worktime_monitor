#! /usr/bin/python3


from datetime import date


# This class presents working period which saves the date and the time 
class Period:


    def __init__(self, work_time):
        self.date = date.today().strftime("%d.%m.%Y")
        self.work_time = work_time


    def set_date(self, date):
        self.date = date


    # Time worked in seconds
    def set_work_time(self, work_time):
        self.work_time = work_time


    def get_period(self):
        return self.date, self.work_time

