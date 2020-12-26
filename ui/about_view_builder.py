#! /usr/bin/python3


class AboutViewBuilder:


    '''
    This builds the about view
    '''
    @staticmethod
    def about_view(stdscr):
        h, w = stdscr.getmaxyx()
        mid_h = h//2
        mid_w = w//2

        message_program_name = "Time It Monitor"
        message_description = "'Program to keep track of your time usage'"
        message_first_release = "First release date: 26.05.2020"
        message_version = "Version 1.2"
        message_latest_release = "Latest update date: 26.12.2020"
        message_author = "Author: SamiHei"
        message_documentation = "Documentation: https://github.com/SamiHei/worktime_monitor"

        stdscr.addstr(mid_h-9, mid_w-(len(message_program_name)//2), message_program_name)

        stdscr.addstr(mid_h-7, mid_w-(len(message_description)//2), message_description)

        stdscr.addstr(mid_h-5, mid_w-(len(message_version)//2), message_version)
        stdscr.addstr(mid_h-3, mid_w-(len(message_first_release)//2), message_first_release)
        stdscr.addstr(mid_h-1, mid_w-(len(message_latest_release)//2), message_latest_release)
        stdscr.addstr(mid_h+1, mid_w-(len(message_author)//2), message_author)
        stdscr.addstr(mid_h+3, mid_w-(len(message_documentation)//2), message_documentation)

