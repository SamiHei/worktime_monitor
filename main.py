#! /usr/bin/python3

from common_variables import header
from data_structure.period import Period
from modules.periods import Periods
from modules.timer import TimerModule
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


# DOCS: https://console-menu.readthedocs.io/en/latest/

"""
  Monitor is the base of the program which controls everything
"""
class Monitor:

    
    def __init__(self):
        self.timer = TimerModule()
        self.menu = ConsoleMenu(header, "=" * 68)
        self.periods = Periods()
    

    # TODO: get value/values from timer.time_it and use it properly
    def main(self):
        # testi = Period()
        # testi.set_work_time(self.build_menu())
        # self.periods.add_period(testi)
        # print(self.periods)
        self.build_menu()
        

    """
    Base menu of the program contains all the other menus and functions
    """
    def build_menu(self):
        date_menu = ConsoleMenu("Here comes list of months")
        # timer_item = FunctionItem("Start the timer", self.timer.time_it)

        # self.menu.append_item(timer_item)
        self.menu.append_item(self.build_timer_view())
        self.menu.append_item(self.build_month_menu())
       
        self.menu.show()
        
        # return timer_item.get_return()


    """
    Will contain menu to scroll years/months/dates and see your saved time periods
    """
    def build_month_menu(self):
        month_menu = ConsoleMenu("Browse months")
        month_menu_item = FunctionItem("List of months", month_menu.show)
        return month_menu_item


    # TODO: functionalities for functions here
    def build_timer_view(self):
        timer_module = TimerModule()
        timer_view = ConsoleMenu("Timer!")
        start_timer = FunctionItem("Start", timer_module.start_timer, menu=timer_view, should_exit=False)
        pause_timer = FunctionItem("Pause", timer_module.pause_timer, menu=timer_view, should_exit=False)
        continue_timer = FunctionItem("Continue", timer_module.continue_timer, menu=timer_view, should_exit=False)
        stop_timer = FunctionItem("Stop", timer_module.stop_timer, menu=timer_view, should_exit=True)
        
        timer_view.append_item(start_timer)
        timer_view.append_item(pause_timer)
        timer_view.append_item(continue_timer)
        timer_view.append_item(stop_timer)
        timer = FunctionItem("Timer", timer_view.show)
        return timer
        
             

if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

