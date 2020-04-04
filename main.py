#! /usr/bin/python3

from common_variables import header
from data_structure.period import Period
from modules.periods import Periods
from modules.timer import TimerModule
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


# DOCS: https://console-menu.readthedocs.io/en/latest/

class Monitor:

    
    def main():

        timer = TimerModule()

        menu = ConsoleMenu(header, "=" * 68)

        function_item = FunctionItem("Call a function", input, ["Enter some input"])

        menu.append_item(function_item)

        menu.show()

        
        # periods_list = Periods()
        # timer = TimerModule()
        # result = timer.time_it()
        # test_period = Period(result)
        # date, work_time = test_period.get_period()
        # periods_list.add_period(test_period)
        # # print()
        # # print(date)
        # # print(test_period)
        # # print()
        # print("Worktime in minutes: {:.2f}".format(work_time / 60))
        # print("Worktime in hours: {:.2f}".format((work_time/60)/60))
        # # print()
        # print(periods_list)


   #def menu():


    if __name__=='__main__':
        main()

