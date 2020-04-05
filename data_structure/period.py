#! /usr/bin/python3


from datetime import date


"""
This class presents working period which saves the date and the time 

    date is presented in the format of DD.MM.YYYY
    work_time is presented in seconds    
"""
class Period:


    def __init__(self):
        self.date = date.today().strftime("%d.%m.%Y")
        self.work_time = 0


    def __str__(self):
        string = "Date " + str(self.date) + " "
        string += "Work time: " + str(self.work_time) + "s"
        return string
    

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

