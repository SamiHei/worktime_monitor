#! /usr/bin/python3

from data_structure.period import Period
from modules.timer import TimerModule


class Monitor:

    def main():
        timer = TimerModule()
        result = timer.time_it()
        test_period = Period(result)
        date, work_time = test_period.get_period()
        print()
        print(date)
        print("Worktime in minutes: {:.2f}".format(work_time / 60))
        print("Worktime in hours: {:.2f}".format((work_time/60)/60))
        print()


    if __name__=='__main__':
        main()

