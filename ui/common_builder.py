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

        if (len(menu_items) > 3 and current_row_idx >= 2):
            stdscr.addstr(first_row-1, x, ' ▲')

        if (len(menu_items) > 3 and current_row_idx < len(menu_items) - 3):
            stdscr.addstr(first_row+4, x, ' ▼')

        i = 2
        j = 0
        # TODO: Write again
        for idx, row in enumerate(menu_items):
           
            if (idx == current_row_idx == 0):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(first_row, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            elif (current_row_idx == 0 and idx > 0 and idx < 4):
                stdscr.addstr(first_row+idx, x, row)
                continue

            if (idx != current_row_idx == len(menu_items)-1 and idx >= current_row_idx - 3):
                stdscr.addstr(first_row+j, x, row)
                j += 1
                continue

            elif (idx == current_row_idx == len(menu_items)-1):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+3, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            if (idx != current_row_idx == len(menu_items)-2 and idx >= current_row_idx - 2 and j < 2):
                stdscr.addstr(first_row+j, x, row)
                j += 1
                continue

            elif (idx == current_row_idx == len(menu_items)-2):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+2, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            elif (idx == len(menu_items)-1):
                stdscr.addstr(menu_y+3, x, row)
                continue

            if (idx == current_row_idx == 1):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+idx, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            elif (current_row_idx == 1 and idx == 0):
                stdscr.addstr(first_row, x, row)
                continue

            elif (idx != current_row_idx == 1 and idx < 4):
                stdscr.addstr(menu_y+idx, x, row)
                continue
            
            if (idx != current_row_idx >= 2 and idx == current_row_idx-1 and current_row_idx < len(menu_items)-3):
                stdscr.addstr(menu_y, x, row)
                continue

            elif (idx == current_row_idx >= 2  and current_row_idx < len(menu_items)-3):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+1, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            elif (idx != current_row_idx >= 2 and idx > current_row_idx and idx < current_row_idx+2 and current_row_idx < len(menu_items)-3):
                stdscr.addstr(menu_y+2, x, row)
                continue

            elif (idx != current_row_idx >= 2 and idx > current_row_idx and idx < current_row_idx+3  and current_row_idx < len(menu_items)-3):
                stdscr.addstr(menu_y+3, x, row)
                continue

            if (idx != current_row_idx >= len(menu_items) - 3 and idx == current_row_idx - 1):
                stdscr.addstr(first_row, x, row)
                continue

            elif (idx == current_row_idx >= len(menu_items) - 3):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+1, x, row)
                stdscr.attroff(curses.color_pair(1))
                continue

            elif (idx != current_row_idx >= len(menu_items) - 3 and idx >= current_row_idx + 1):
                stdscr.addstr(menu_y+i, x, row)
                i += 1
                continue

        stdscr.refresh()
