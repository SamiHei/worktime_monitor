#! /usr/bin/python3


from data_structures.period import Period
from modules.periods import PeriodsModule
from modules.timer import TimerModule
from modules.export import ExportModule
from ui.ui_builder import UiBuilder
from db.database import DatabaseModule
from common_variables import list_of_months
import sqlite3
import curses
import os
import time


'''
Monitor is the base of the program which controls everything
'''
class Monitor:

    
    def __init__(self):
        self.stdscr = curses.initscr()
        self.timer = None
        self.exporter = None
        self.periods_module = PeriodsModule()
        self.db_name = "database.db"
        self.db = DatabaseModule(self.db_name)


    def main(self):
        try:
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
        # self.stdscr.clear()
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
        menu = ["Timer", "Periods", "Export", "About", "Exit"]


        UiBuilder.print_main_menu(self.stdscr, menu, current_row_idx)
        
        while 1:

            key = self.stdscr.getch()

            # self.stdscr.clear()

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
                    self.timer_menu(0)
                elif (current_row_idx == 1):
                    self.periods_menu_years(0)
                elif (current_row_idx == 2):
                    self.export_menu(0)


            self.stdscr.clear()
            UiBuilder.print_main_menu(self.stdscr, menu, current_row_idx)
            self.stdscr.refresh()


    '''
    Timer view which uses Timer Module
    '''
    def timer_menu(self, current_row_idx):

        self.timer = TimerModule()
        period = Period()

        self.stdscr.clear()
        period.set_name(UiBuilder.print_ask_period_name(self.stdscr))

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

        # Saves the period to database
        # Should I get periods and insert/update or update via error
        if (period.get_work_time() > 0):
            self.db.insert_period_name(period)
            period_name_id = self.db.get_period_name_id(period)
            try:
                self.db.insert_period(period, period_name_id[0])
            except sqlite3.Error:
                self.db.update_period(period, period_name_id[0])


    '''
    Menu to scroll years of your saved periods
    '''
    def periods_menu_years(self, current_row_idx):

        # Fetch periods
        period_years = []
        db_periods = self.db.get_periods()
        for x in range(0, len(db_periods)):
            temp_period = Period()
            period_name = self.db.get_period_name_by_id(db_periods[x][1])[0]
            temp_period.create_period_from_db(db_periods[x], period_name)
            self.periods_module.add_period(temp_period)
            temp_time = time.strptime(self.periods_module.get_periods()[x].get_date(), "%d.%m.%Y")
            if (str(temp_time.tm_year) not in period_years):
                period_years.append(str(temp_time.tm_year))

        self.stdscr.clear()
        UiBuilder.scrollable_menu_list_items(self.stdscr, period_years, current_row_idx)
        self.stdscr.refresh()
        
        while 1:

            key = self.stdscr.getch()

            if (key == curses.KEY_UP and current_row_idx == 0):
                current_row_idx = 0
            elif (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx == (len(period_years) - 1)):
                current_row_idx = len(period_years) - 1
            elif (key == curses.KEY_DOWN and current_row_idx < (len(period_years) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                self.periods_menu_months(0, period_years[current_row_idx])
            elif (key == curses.KEY_BACKSPACE):
                break

            self.stdscr.clear()
            UiBuilder.scrollable_menu_list_items(self.stdscr, period_years, current_row_idx)
            self.stdscr.refresh()


    '''
    Menu to scroll months of your saved periods
    '''
    def periods_menu_months(self, current_row_idx, selected_year):
        months_list = []
        months_num = []
        for x in range(0, len(self.periods_module.get_periods())):
            temp_time = time.strptime(self.periods_module.get_periods()[x].get_date(), "%d.%m.%Y")
            if (list_of_months[temp_time.tm_mon] not in months_list):
                months_list.append(list_of_months[temp_time.tm_mon])
                months_num.append(temp_time.tm_mon)

        self.stdscr.clear()
        UiBuilder.scrollable_menu_list_items(self.stdscr, months_list, current_row_idx)
        self.stdscr.refresh()

        while 1:

            key = self.stdscr.getch()

            if (key == curses.KEY_UP and current_row_idx == 0):
                current_row_idx = 0
            elif (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx == (len(months_list) - 1)):
                current_row_idx = len(months_list) - 1
            elif (key == curses.KEY_DOWN and current_row_idx < (len(months_list) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                self.stdscr.clear()
                self.periods_view(0, selected_year, months_num[current_row_idx])
            elif (key == curses.KEY_BACKSPACE):
                break

            self.stdscr.clear()
            UiBuilder.scrollable_menu_list_items(self.stdscr, months_list, current_row_idx)
            self.stdscr.refresh()


    '''
    Scrollable periods data view
    '''
    def periods_view(self, current_row_idx, selected_year, selected_month):

        periods_list = self.periods_module.get_periods_by_year_and_month(int(selected_year), selected_month)

        self.stdscr.clear()
        UiBuilder.print_period_data(current_row_idx, self.stdscr, selected_year, selected_month, periods_list)
        self.stdscr.refresh()

        while 1:

            h, w = self.stdscr.getmaxyx()
            data_sets_shown = (h-1)//4

            key = self.stdscr.getch()

            if (key == curses.KEY_UP and current_row_idx == 0):
                current_row_idx = 0
            elif (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx == (len(periods_list) - 1)):
                current_row_idx = len(periods_list) - 1
            elif (key == curses.KEY_DOWN and current_row_idx < (len(periods_list) - data_sets_shown)):
                current_row_idx += 1

            elif (key == curses.KEY_BACKSPACE):
                break

            self.stdscr.clear()
            UiBuilder.print_period_data(current_row_idx, self.stdscr, selected_year, selected_month, periods_list)
            self.stdscr.refresh()


    '''
    View to export period data to csv or json file
    '''
    def export_menu(self, current_row_idx):

        export_menu_items = ['Csv', 'Json']

        self.stdscr.clear()
        UiBuilder.scrollable_menu_list_items(self.stdscr, export_menu_items, current_row_idx)
        self.stdscr.refresh()

        while 1:

            key = self.stdscr.getch()

            if (key == curses.KEY_BACKSPACE):
                break


if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

