#! /usr/bin/python3

import time


class PeriodsViewBuilder:


    '''
    Method to print periods data view

        stdscr = screen which is used in the program
        year = Year of the data which is shown
        month = Month of the data which is shown
        current_row_idx = Selected row index
    '''
    @staticmethod
    def print_period_data(stdscr, year, month, periods, current_row_idx):
        h, w = stdscr.getmaxyx()

        show_periods = []

        for period in periods.get_periods_list():
            temp_time = time.strptime(period.get_date(), "%d.%m.%Y")
            if (temp_time.tm_year == year and temp_time.tm_mon == month):
                show_periods.append(period)

        data_sets_shown = (h-1)//4

        # TODO: Make scalable view from this!!

        if (len(show_periods) > data_sets_shown):
            loop_i = data_sets_shown
        else:
            loop_i = len(show_periods)

        for x in range(0, loop_i):
            stdscr.addstr(1 + (x * 4), 0, "Period date: {}".format(show_periods[x].get_date()))
            stdscr.addstr(2 + (x * 4), 0, "Period name: " + show_periods[x].get_name().decode("utf-8").capitalize())
            work_time = show_periods[x].get_work_time()
            minutes = work_time/60
            hours = minutes//60
            final_minutes = minutes - (60 * hours)
            stdscr.addstr(3 + (x * 4), 0, "Period time: {} hour and {:.0f} minute".format(hours, final_minutes))
            stdscr.addstr(4 + (x * 4), 0, "=" * (w//2))
        
        stdscr.refresh()
