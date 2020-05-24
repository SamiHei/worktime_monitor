#! /usr/bin/python3


class PeriodsViewBuilder:


    '''
    Method to print periods data view

        stdscr = screen which is used in the program
        year = Year of the data which is shown
        month = Month of the data which is shown
        current_row_idx = Selected row index
    '''
    @staticmethod
    def print_period_data(current_row_idx, stdscr, year, month, periods):
        h, w = stdscr.getmaxyx()

        periods_list = periods.get_periods_by_year_and_month(int(year), month)

        data_sets_shown = (h-1)//4

        if (len(periods_list) > data_sets_shown):
            loop_i = data_sets_shown
        else:
            loop_i = len(periods_list)

        if (current_row_idx >= 1):
            stdscr.addstr(0, 15, '/\\')

        for x in range(0, loop_i):
            
            work_time = periods_list[x].get_work_time()
            minutes = work_time/60
            hours = minutes//60
            final_minutes = minutes - (60 * hours)
            
            stdscr.addstr(1 + (x * 4), 0, "Period date: {}".format(periods_list[x].get_date()))
            stdscr.addstr(2 + (x * 4), 0, "Period name: " + periods_list[x].get_name().decode("utf-8").capitalize())
            stdscr.addstr(3 + (x * 4), 0, "Period time: {} hour and {:.0f} minute".format(hours, final_minutes))
            stdscr.addstr(4 + (x * 4), 0, "=" * (w//3))
            
            last_row = x

        if (data_sets_shown < len(periods_list)):
            stdscr.addstr(5 + (last_row * 4), 15, '\/')

        stdscr.refresh()

