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
