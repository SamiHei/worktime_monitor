#! /usr/bin/python3

from ui.header_text import header
import curses


class MainMenuBuilder:


    """
    Method to print menu items to screen

    stdscr : curses.stdscr, screen which is used to build view
    menu : string list, list of menu items
    menu_header : string, ascii graphic header
    current_row_idx : int, Selected row index
    """
    @staticmethod
    def print_main_menu(stdscr, menu, current_row_idx):

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        h, w = stdscr.getmaxyx()
        menu_y = h//2 - len(menu)//2
        x = w//2
        
        MainMenuBuilder.print_header(stdscr, header, menu_y)

        for idx, row in enumerate(menu):
            y = menu_y + idx
            if (idx == current_row_idx):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

        stdscr.refresh()


    """
    Method to print ascii graphic header to menu

    stdscr : curses.stdscr, screen which is used to build view
    menu_header : string, ascii graphic header
    menu_y : int, given height from the calling funtion
    """
    @staticmethod
    def print_header(stdscr, menu_header, menu_y):
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

        h, w = stdscr.getmaxyx()

        width = w//2 - 23
        height = menu_y - 9

        stdscr.attron(curses.color_pair(2))
        for y, line in enumerate(menu_header.splitlines(), height):
            stdscr.addstr(y, width, line)
        stdscr.attroff(curses.color_pair(2))
