#! /usr/bin/python3

from data_structure.period import Period
from modules.periods import Periods
from modules.timer import TimerModule


class Monitor:

    def main():
        periods_list = Periods()
        timer = TimerModule()
        result = timer.time_it()
        test_period = Period(result)
        date, work_time = test_period.get_period()
        periods_list.add_period(test_period)
        # print()
        # print(date)
        # print(test_period)
        # print()
        print("Worktime in minutes: {:.2f}".format(work_time / 60))
        print("Worktime in hours: {:.2f}".format((work_time/60)/60))
        # print()
        # print(periods_list)


    if __name__=='__main__':
        main()

