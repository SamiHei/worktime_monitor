#! /usr/bin/python3


from data_structure.period import Period
from modules.timer import TimerModule


class Monitor:

    def main():
        timer = TimerModule()
        result = timer.time_it()
        test_period = Period(result)
        date, work_time = test_period.get_period()
        print(date)
        print(work_time)


    if __name__=='__main__':
        main()

