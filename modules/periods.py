#! /usr/bin/python3


"""
This module contains methods for saving, reading, handling and presenting
"""
class PeriodsModule:


    def __str__(self):
        i = 0
        for p in self.periods:
            string = "Period {}\n".format(i)
            string += str(p.get_date()) + "\n"
            string += str(p.get_work_time()) + "\n"
            i += 1
        return string


    def add_period(self, period):
        self.periods.append(period)


    # def get_years(list_of_periods):
        
