#! /usr/bin/python3


import time


"""
This module contains list of Period data structures and methods for handling
"""
class PeriodsModule:

    def __init__(self):
        self.periods = []


    def add_period(self, period):
        self.periods.append(period)


    def get_periods(self):
        return self.periods


    def get_periods_by_year_and_month(self, year, month):
        
        periods_list = []
        
        for period in self.get_periods():
            temp_time = time.strptime(period.get_date(), "%d.%m.%Y")
            if (temp_time.tm_year == year and temp_time.tm_mon == month):
                periods_list.append(period)

        return periods_list

