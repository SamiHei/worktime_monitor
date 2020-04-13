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
    Base menu of the program contains all the other menus and functions
    '''
    def build_main_menu(self, stdscr):

        current_row_idx = 0
        menu = ["Timer", "Months", "Exit"]

        
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
                    curses.nocbreak()
                    stdscr.keypad(False)
                    curses.echo()
                    curses.endwin()
                    break

            self.print_main_menu(menu, header, current_row_idx)

            self.stdscr.refresh()


    '''
    Commont method to print menu items to screen
        menu = Array of menu items
        current_row_idx = Selected row index
    '''
    def print_main_menu(self, menu, menu_header, current_row_idx):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        curses.curs_set(0)
        curses.noecho()
        self.stdscr.keypad(True)
        
        self.print_header(menu_header)

        for idx, row in enumerate(menu):
            x = w//2
            y = h//2 - len(menu)//2 + idx
            if (idx == current_row_idx):
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))
            else:
                self.stdscr.addstr(y, x, row)
                

        self.stdscr.refresh()


    def print_header(self, menu_header):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        h, w = self.stdscr.getmaxyx()

        x = w//2
        y = h//5

        self.stdscr.attron(curses.color_pair(1))
        self.stdscr.addstr(y, x, menu_header)
        self.stdscr.attroff(curses.color_pair(1))
        

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

