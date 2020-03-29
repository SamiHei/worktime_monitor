#! /usr/bin/python3



# This class presents working period which saves the date and the time 
class Period:


    def __init__(self, date, work_time):
        self.date = date
        self.work_time = work_time

    def get_period(self):
        return self.date, self.work_time

