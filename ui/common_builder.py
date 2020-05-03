#! /usr/bin/python3

import curses


'''
Common builder for UI components used possibly in multiple locations and not related to specific UI builder
'''
class CommonBuilder:


    '''
    Takes user input until given input is longer than 0
    '''
    @staticmethod
    def take_user_input(stdscr, y, x, input_question):
        curses.echo() 
        stdscr.addstr(y, x, input_question)
        stdscr.refresh()
        input = stdscr.getstr(y, (x + len(input_question)), 20)

        while 1:
            if (len(input) == 0):
                input = stdscr.getstr(y, (x + len(input_question)), 20)
            else:
                return input


    '''
    Creates scrollable menu from menu_items and shows indicators when it is possible to scroll
    '''
    @staticmethod
    def scrollable_menu_list_items(stdscr, menu_items, current_row_idx):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        h, w = stdscr.getmaxyx()
        menu_y = h//2 - len(menu_items)//2
        first_row = menu_y
        x = w//2

        if (len(menu_items) > 3 and current_row_idx > 2):
            stdscr.addstr(first_row, x, ' ▲')

        if (len(menu_items) > 3 and current_row_idx < len(menu_items) - 2):
            stdscr.addstr(first_row+5, x, ' ▼')
        
        for idx, row in enumerate(menu_items):
            y = menu_y + idx - 1

            if (current_row_idx > 2 and idx < 2):
                continue

            if (idx == current_row_idx):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))

            elif (idx <= current_row_idx + 2):
                stdscr.addstr(y, x, row)

        stdscr.refresh()
