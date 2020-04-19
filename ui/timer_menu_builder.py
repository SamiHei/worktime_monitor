#! /usr/bin/python3

import curses

class TimerMenuBuilder:

    @staticmethod
    def print_timer_menu(stdscr, menu_items, current_row_idx):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        h, w = stdscr.getmaxyx()
        menu_y = h//2 - len(menu_items)//2
        
        for idx, row in enumerate(menu_items):
            x = w//2 - (len(row))//2 # Here maybe some fix so text is left aligned!
            y = menu_y + idx
            if (idx == current_row_idx):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

