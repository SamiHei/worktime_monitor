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
        x = w//2
        menu_len = len(menu_items)

        if (menu_len >= 4 and current_row_idx >= 2):
            stdscr.addstr(menu_y-1, x, ' ▲')

        if (menu_len >= 4 and current_row_idx < menu_len - 3):
            stdscr.addstr(menu_y+4, x, ' ▼')

        while 1:

            if (current_row_idx == 0):
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y, x, menu_items[0])
                stdscr.attroff(curses.color_pair(1))

                for i in range(1, menu_len):
                    stdscr.addstr(menu_y+i, x, menu_items[i])

                break

            elif (current_row_idx == 1):
                stdscr.addstr(menu_y, x, menu_items[0])
                
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+1, x, menu_items[1])
                stdscr.attroff(curses.color_pair(1))

                for i in range(2, menu_len):
                    stdscr.addstr(menu_y+i, x, menu_items[i])

                break

            elif (current_row_idx >= 2 and current_row_idx <= menu_len-3):
                stdscr.addstr(menu_y, x, menu_items[current_row_idx-1])
                
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+1, x, menu_items[current_row_idx])
                stdscr.attroff(curses.color_pair(1))

                stdscr.addstr(menu_y+2, x, menu_items[current_row_idx+1])
                stdscr.addstr(menu_y+3, x, menu_items[current_row_idx+2])
                break
                
            elif (current_row_idx == menu_len-1):
                stdscr.addstr(menu_y, x, menu_items[current_row_idx-3])
                stdscr.addstr(menu_y+1, x, menu_items[current_row_idx-2])
                stdscr.addstr(menu_y+2, x, menu_items[current_row_idx-1])
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+3, x, menu_items[current_row_idx])
                stdscr.attroff(curses.color_pair(1))
                break

            elif (current_row_idx == menu_len-2):
                stdscr.addstr(menu_y, x, menu_items[current_row_idx-2])
                stdscr.addstr(menu_y+1, x, menu_items[current_row_idx-1])
                
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(menu_y+2, x, menu_items[current_row_idx])
                stdscr.attroff(curses.color_pair(1))
                
                stdscr.addstr(menu_y+3, x, menu_items[current_row_idx+1])
                break

        stdscr.refresh()
