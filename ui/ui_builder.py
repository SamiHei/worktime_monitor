#! /usr/bin/python3

from ui.main_menu_builder import MainMenuBuilder
from ui.timer_menu_builder import TimerMenuBuilder
from ui.common_builder import CommonBuilder
from ui.periods_view_builder import PeriodsViewBuilder


'''
This is Builder to collect all Builders in a single class to be called in Monitor
'''
class UiBuilder(MainMenuBuilder, TimerMenuBuilder, CommonBuilder, PeriodsViewBuilder):

    def empty():
        print("Empty")
