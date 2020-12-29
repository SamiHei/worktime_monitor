#! /usr/bin/python3


import time
from data_structures.period import Period

"""
This module contains list of Period data structures and methods for handling
"""
class PeriodsModule:

    def __init__(self, db):
        self.periods = []
        if (db != None):
            self.get_periods_from_db(db)


    def add_period(self, period):
        self.periods.append(period)


    def update_period_time(self, period, time):
        for p in self.periods:
            if (period.get_date() == p.get_date()):
                if (period.get_name() == p.get_name()):
                    p.update_work_time(time)


    def get_periods(self):
        return self.periods


    def check_if_period_exists(self, period):
        for p in self.periods:
            if (period.get_date() == p.get_date()):
                if (period.get_name() == p.get_name()):
                    return True
        return False


    """
    Returns periods with given year and month

    year : int, year which the searched periods are from
    month : int, month which the searched periods are from
    """
    def get_periods_by_year_and_month(self, year, month):
        
        periods_list = []
        
        for period in self.get_periods():
            temp_time = time.strptime(period.get_date(), "%Y-%m-%d")
            if (temp_time.tm_year == year and temp_time.tm_mon == month):
                periods_list.append(period)

        return periods_list


    """
    Gets all the periods from the database and adds to PeriodsModule periods list

    db : DatabaseModule, used to call database method to get all periods
    """
    def get_periods_from_db(self, db):
        db_periods = db.get_periods()
        for x in range(0, len(db_periods)):
            temp_period = Period()
            period_name = db.get_period_name_by_id(db_periods[x][1])[0]
            temp_period.create_period_from_db(db_periods[x], period_name)
            self.add_period(temp_period)

