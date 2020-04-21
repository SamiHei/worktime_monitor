#! /usr/bin/python3

import curses
from ui.common_builder import CommonBuilder

class TimerMenuBuilder:

    @staticmethod
    def print_timer_menu(stdscr, menu_items, current_row_idx, timer_state, elapsed_time):
        TimerMenuBuilder.print_timer_state_and_elapsed_time(stdscr, timer_state, elapsed_time)
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

        stdscr.refresh()


    @staticmethod
    def print_timer_state_and_elapsed_time(stdscr, timer_state, elapsed_time):

        state_string = "Timer state: {}".format(timer_state)
        elapsed_time_string = "Elapsed time at pause: {} minutes".format(round(elapsed_time/60, 2))
        h, w = stdscr.getmaxyx()

        x = w//2 - len(state_string)//2
        y = h//4
        x_e = w//2 - len(elapsed_time_string)//2
        y_e = h//4 + 1

        stdscr.addstr(y, x, state_string)
        stdscr.addstr(y_e, x_e, elapsed_time_string)


    @staticmethod
    def print_ask_period_name(stdscr):
        h, w = stdscr.getmaxyx()

        ask_period_name = "Give name for the to be timed period> "
        
        x = w//3 - len(ask_period_name)//2
        y = h//2

        period_name = CommonBuilder.take_user_input(stdscr, y, x, ask_period_name)
        return period_name

