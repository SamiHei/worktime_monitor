#! /usr/bin/python3

#from common_variables import header
from data_structures.period import Period
from modules.periods import Periods
from modules.timer import TimerModule
from ui.ui_builder import UiBuilder
from db.database import DatabaseModule
import sqlite3
import curses
import os
import time # For testing


'''
Monitor is the base of the program which controls everything
'''
class Monitor:

    
    def __init__(self):
        self.stdscr = curses.initscr()
        self.timer = None
        self.periods = Periods()
        self.db_name = "database.db"
        self.db = DatabaseModule(self.db_name)


    def main(self):
        try:
            # db = DatabaseModule(self.db_name)
            if not (os.path.isfile(self.db_name)):
                con = self.db.create_connection()
                self.db.create_database(con)
            self.set_start_settings()
            curses.wrapper(self.main_menu)
        except sqlite3.Error as e:
            print(e)
        finally:
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

            
        UiBuilder.print_main_menu(self.stdscr, menu, current_row_idx)
        
        while 1:

            key = self.stdscr.getch()

            self.stdscr.clear()

            if (key == curses.KEY_UP and current_row_idx == 0):
                current_row_idx = len(menu) - 1
            elif (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx == (len(menu) - 1)):
                current_row_idx = 0
            elif (key == curses.KEY_DOWN and current_row_idx < (len(menu) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                if (current_row_idx == (len(menu) - 1)):
                    break
                elif (current_row_idx == 0):
                    self.timer_menu(current_row_idx)


            self.stdscr.clear()
            UiBuilder.print_main_menu(self.stdscr, menu, current_row_idx)
            self.stdscr.refresh()


    '''
    Timer view which uses Timer Module
    '''
    def timer_menu(self, current_row_idx):

        self.timer = TimerModule()
        period = Period()

        while 1:
            period.set_name(UiBuilder.print_ask_period_name(self.stdscr))
            break

        timer_menu = ["Start timer", "Pause timer", "Continue timer", "Exit"]

        self.stdscr.clear()

        UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx,
                                   self.timer.get_state(), self.timer.get_elapsed_time())

        while 1:
                
            key = self.stdscr.getch()
                
            self.stdscr.clear()

            if (key == curses.KEY_UP and current_row_idx == 0):
                current_row_idx = len(timer_menu) - 1
            elif (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx == (len(timer_menu) - 1)):
                current_row_idx = 0
            elif (key == curses.KEY_DOWN and current_row_idx < (len(timer_menu) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                if (current_row_idx == (len(timer_menu) - 1)):
                    period.set_work_time(self.timer.stop_timer())
                    break
                elif (current_row_idx == 0):
                    self.stdscr.clear()
                    self.timer.start_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx,
                                               self.timer.get_state(), self.timer.get_elapsed_time())
                elif (current_row_idx == 1):
                    self.stdscr.clear()
                    self.timer.pause_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx,
                                               self.timer.get_state(), self.timer.get_elapsed_time())
                elif (current_row_idx == 2):
                    self.stdscr.clear()
                    self.timer.continue_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx,
                                               self.timer.get_state(), self.timer.get_elapsed_time())

            self.stdscr.clear()
            UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx,
                                       self.timer.get_state(), self.timer.get_elapsed_time())

            self.stdscr.refresh()

        # Saves the data to database
        self.db.insert_period_name(period)
        period_name_id = self.db.get_period_name_id(period)
        try:
            self.db.insert_period(period, period_name_id[0])
        except sqlite3.Error:
            self.db.update_period(period, period_name_id[0])


    '''
    Will contain menu to scroll years/months/dates and see your saved time periods
    '''
    def build_month_menu(self):
        print("Month menu")


if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

