#! /usr/bin/python3

from ui.main_menu_builder import MainMenuBuilder
from ui.timer_menu_builder import TimerMenuBuilder

class UiBuilder(MainMenuBuilder, TimerMenuBuilder):

    def empty():
        print("Empty")
