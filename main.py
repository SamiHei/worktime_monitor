#! /usr/bin/python3

from common_variables import header
from data_structure.period import Period
from modules.periods import Periods
from modules.timer import TimerModule
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
        curses.wrapper(self.build_main_menu)


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


    '''
    Base menu of the program contains all the other menus and functions
    '''
    def build_main_menu(self, stdscr):

        current_row_idx = 0
        menu = ["Timer", "Months", "Exit"]

        self.set_start_settings()
        
        self.print_main_menu(menu, header, current_row_idx)

        while 1:

            key = self.stdscr.getch()
            
            self.stdscr.clear()
            
            if (key == curses.KEY_UP and current_row_idx > 0):
                current_row_idx -= 1
            elif (key == curses.KEY_DOWN and current_row_idx < (len(menu) - 1)):
                current_row_idx += 1
            elif (key == curses.KEY_ENTER or key in [10, 13]):
                self.stdscr.addstr(0,0, "You pressed {}".format(menu[current_row_idx]))
                self.stdscr.refresh()
                self.stdscr.getch()
                if (current_row_idx == (len(menu) - 1)):
                    self.end_program()
                    break

            self.print_main_menu(menu, header, current_row_idx)

            self.stdscr.refresh()


    '''
    Method to print menu items to screen
        menu = Array of menu items
        menu_header = ascii graphic header
        current_row_idx = Selected row index
    '''
    def print_main_menu(self, menu, menu_header, current_row_idx):

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        h, w = self.stdscr.getmaxyx()
        menu_y = h//2 - len(menu)//2
        
        self.print_header(menu_header, menu_y)

        for idx, row in enumerate(menu):
            x = w//2
            y = menu_y + idx
            if (idx == current_row_idx):
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, row)

        self.stdscr.refresh()


    '''
    Method to print ascii graphic header to menu
    '''
    def print_header(self, menu_header, menu_y):
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

        h, w = self.stdscr.getmaxyx()

        width = w//2 - 23
        height = menu_y - 10

        self.stdscr.attron(curses.color_pair(2))
        for y, line in enumerate(menu_header.splitlines(), height):
            self.stdscr.addstr(y, width, line)
        self.stdscr.attroff(curses.color_pair(2))
        

    '''
    Will contain menu to scroll years/months/dates and see your saved time periods
    '''
    def build_month_menu(self):
        print("Month menu")


    '''
    Timer view which uses Timer Module
    '''
    def build_timer_view(self):
        print("Timer view")
   

if __name__ == '__main__':
    monitor = Monitor()
    monitor.main()

