#! /usr/bin/python3

from common_variables import header
from data_structure.period import Period
from modules.periods import Periods
from modules.timer import TimerModule
from ui.ui_builder import UiBuilder
import curses


'''
Monitor is the base of the program which controls everything
'''
class Monitor:

    
    def __init__(self):
        self.stdscr = curses.initscr()
        self.timer = TimerModule()
        self.periods = Periods()


    def main(self):
        self.set_start_settings()
        curses.wrapper(self.main_menu)
        self.end_program()


    '''
    Basic settings at start
    '''
    def set_start_settings(self):
        self.stdscr.clear()
        curses.curs_set(0)
        curses.noecho()
        self.stdscr.keypad(True)
        curses.start_color()


    '''
    Will be called at the end of the program
    '''
    def end_program(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


    def main_menu(self, stdscr):

        current_row_idx = 0
        menu = ["Timer", "Months", "Exit"]

            
        UiBuilder.print_main_menu(self.stdscr, menu, header, current_row_idx)
        
        while 1:
                
            key = self.stdscr.getch()
                
            self.stdscr.clear()
                
            if (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx < (len(menu) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                # self.stdscr.addstr(0,0, "You pressed {}".format(menu[current_row_idx]))
                # self.stdscr.addstr(0,2, "You pressed {}".format(current_row_idx))
                # self.stdscr.refresh()
                # self.stdscr.getch()
                if (current_row_idx == (len(menu) - 1)):
                    break
                elif (current_row_idx == 0):
                    self.stdscr.clear()
                    self.timer_menu(current_row_idx)
                    # UiBuilder.print_main_menu(self.stdscr, timer_menu, "", current_row_idx)
                    self.stdscr.refresh()
                    self.stdscr.getch()

            self.stdscr.clear()
            UiBuilder.print_main_menu(self.stdscr, menu, header, current_row_idx)
                    
            self.stdscr.refresh()


    '''
    Timer view which uses Timer Module
    '''
    def timer_menu(self, current_row):

        timer_menu = ["Start timer", "Pause timer", "Continue timer", "Stop timer"]

        UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row)


    '''
    Will contain menu to scroll years/months/dates and see your saved time periods
    '''
    def build_month_menu(self):
        print("Month menu")


if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

