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
        self.db_name = "database.db"
        self.db = DatabaseModule(self.db_name)
        if (os.path.isfile(self.db_name)):
            self.periods_module = PeriodsModule(self.db)
        else:
            self.periods_module = PeriodsModule(None)


    '''
    Starts the program
    '''
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


    '''
    Main menu of the program
    '''
    def main_menu(self, stdscr):

        current_row_idx = 0
        menu = ["Timer", "Periods", "Export", "About", "Exit"]

        UiBuilder.print_main_menu(self.stdscr, menu, current_row_idx)
        
        while 1:

            key = self.stdscr.getch()

            current_row_idx = self.menu_scroll(key, current_row_idx, menu, 1)

            if (key == curses.KEY_ENTER or key in [10, 13]):
                if (current_row_idx == (len(menu) - 1)):
                    break
                elif (current_row_idx == 0):
                    self.timer_menu(0)
                elif (current_row_idx == 1):
                    self.periods_menu_years(0)
                elif (current_row_idx == 2):
                    self.export_menu(0)
                elif (current_row_idx == 3):
                    self.about_view()

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

        timer_menu = ["Start timer", "Pause timer", "Exit"]

        self.stdscr.clear()

        UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx, period.get_name(),
                                   self.timer.get_state(), self.timer.get_elapsed_time())

        while 1:
                
            key = self.stdscr.getch()

            current_row_idx = self.menu_scroll(key, current_row_idx, timer_menu, 1)

            if (key == curses.KEY_ENTER or key in [10, 13]):
                if (current_row_idx == (len(timer_menu) - 1)):
                    period.set_work_time(self.timer.stop_timer())
                    break
                elif (current_row_idx == 0 and self.timer.get_state() == "Stopped"):
                    self.stdscr.clear()
                    self.timer.start_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx, period.get_name(),
                                               self.timer.get_state(), self.timer.get_elapsed_time())
                    self.stdscr.refresh()
                elif (current_row_idx == 0):
                    self.stdscr.clear()
                    self.timer.continue_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx, period.get_name(),
                                               self.timer.get_state(), self.timer.get_elapsed_time())
                    self.stdscr.refresh()
                elif (current_row_idx == 1):
                    self.stdscr.clear()
                    self.timer.pause_timer()
                    UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx, period.get_name(),
                                               self.timer.get_state(), self.timer.get_elapsed_time())
                    self.stdscr.refresh()

                if (self.timer.get_state() != "Stopped" and timer_menu[0] != "Continue timer"):
                    timer_menu[0] = "Continue timer"

            self.stdscr.clear()
            UiBuilder.print_timer_menu(self.stdscr, timer_menu, current_row_idx, period.get_name(),
                                       self.timer.get_state(), self.timer.get_elapsed_time())

            self.stdscr.refresh()

        # Saves the period to database
        if (period.get_work_time() > 0):
            self.periods_module.add_period(period)
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
        period_years = []

        for x in range(0, len(self.periods_module.get_periods())):
            temp_time = time.strptime(self.periods_module.get_periods()[x].get_date(), "%Y-%m-%d")
            if (str(temp_time.tm_year) not in period_years):
                period_years.append(str(temp_time.tm_year))

        self.stdscr.clear()
        UiBuilder.scrollable_menu_list_items(self.stdscr, period_years, current_row_idx)
        self.stdscr.refresh()
        
        while 1:

            key = self.stdscr.getch()

            current_row_idx = self.menu_scroll(key, current_row_idx, period_years, 1)

            if (key == curses.KEY_ENTER or key in [10, 13]):
                if (len(period_years) != 0):
                    self.periods_menu_months(0, period_years[current_row_idx])
            elif (key in (curses.KEY_BACKSPACE, curses.KEY_LEFT)):
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
            temp_time = time.strptime(self.periods_module.get_periods()[x].get_date(), "%Y-%m-%d")
            if (list_of_months[temp_time.tm_mon] not in months_list):
                months_list.append(list_of_months[temp_time.tm_mon])
                months_num.append(temp_time.tm_mon)

        self.stdscr.clear()
        UiBuilder.scrollable_menu_list_items(self.stdscr, months_list, current_row_idx)
        self.stdscr.refresh()

        while 1:

            key = self.stdscr.getch()

            current_row_idx = self.menu_scroll(key, current_row_idx, months_list, 1)

            if (key == curses.KEY_ENTER or key in [10, 13]):
                self.stdscr.clear()
                self.periods_view(0, selected_year, months_num[current_row_idx])
            elif (key in (curses.KEY_BACKSPACE, curses.KEY_LEFT)):
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

            current_row_idx = self.menu_scroll(key, current_row_idx, periods_list, data_sets_shown)

            if (key in (curses.KEY_BACKSPACE, curses.KEY_LEFT)):
                break

            self.stdscr.clear()
            UiBuilder.print_period_data(current_row_idx, self.stdscr, selected_year, selected_month, periods_list)
            self.stdscr.refresh()


    '''
    View to export period data to csv or json file
    '''
    def export_menu(self, current_row_idx):

        export_menu_items = ['Csv', 'Json']
        periods_amount = len(self.periods_module.get_periods())
        self.exporter = ExportModule(self.periods_module.get_periods())

        self.stdscr.clear()
        if (periods_amount == 0):
            UiBuilder.message_view(self.stdscr, "Nothing to export yet, go back with BACKSPACE or LEFT key")
        else:
            UiBuilder.scrollable_menu_list_items(self.stdscr, export_menu_items, current_row_idx)
        self.stdscr.refresh()

        while 1:

            key = self.stdscr.getch()

            current_row_idx = self.menu_scroll(key, current_row_idx, export_menu_items, 1)

            if (key == curses.KEY_ENTER or key in [10, 13] and periods_amount != 0):
                if (current_row_idx == 0):
                    self.exporter.export_csv()
                    UiBuilder.message_view(self.stdscr, "Csv export was successful!")
                    time.sleep(1)
                    break
                elif (current_row_idx == 1):
                    self.exporter.export_json()
                    UiBuilder.message_view(self.stdscr, "Json export was successful!")
                    time.sleep(1)
                    break

            elif (key in (curses.KEY_BACKSPACE, curses.KEY_LEFT)):
                break

            self.stdscr.clear()
            if (periods_amount == 0):
                UiBuilder.message_view(self.stdscr, "Nothing to export yet, go back with BACKSPACE or LEFT key")
            else:
                UiBuilder.scrollable_menu_list_items(self.stdscr, export_menu_items, current_row_idx)
            self.stdscr.refresh()


    '''
    About view of the program
    '''
    def about_view(self):
        self.stdscr.clear()
        UiBuilder.about_view(self.stdscr)
        self.stdscr.refresh()

        while 1:

            key = self.stdscr.getch()

            if (key in (curses.KEY_BACKSPACE, curses.KEY_LEFT)):
                break


    '''
    Logic to scroll the view
    '''
    def menu_scroll(self, key, current_row_idx, menu_items, remove_menu_items_arr_len):

        if (key == curses.KEY_UP and current_row_idx == 0):
            current_row_idx = 0
        elif (key == curses.KEY_UP and current_row_idx > 0):
            current_row_idx -= 1
        elif (key == curses.KEY_DOWN and current_row_idx == (len(menu_items) - 1)):
            current_row_idx = len(menu_items) - 1
        elif (key == curses.KEY_DOWN and current_row_idx < (len(menu_items) - remove_menu_items_arr_len)):
            current_row_idx += 1

        return current_row_idx


if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

