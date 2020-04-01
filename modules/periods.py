#! /usr/bin/python3


"""
This class contains all the periods and methods saving, reading and presenting
"""
class Periods:

    periods = []


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

