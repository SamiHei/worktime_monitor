#! /usr/bin/python3


import time


class TimerModule:


    state = False


    """
    Takes time until user gives string "stop" and pauses the timer when user gives "pause"
    """
    def time_it(self):
        start_time = time.time()
        elapsed_time = 0
        str = "start"
        state = True
        while True:
            str = input()
            if str == "pause":
                state = False
                print("Timer paused")
                end_time = time.time()
                elapsed_time += end_time - start_time
                print(elapsed_time)
            if str == "continue":
                state = True
                print("Timer continued")
                print(elapsed_time)
                start_time = time.time()
            if str == "stop":
                print("Timer stopped")
                print(elapsed_time)
                end_time = time.time()
                break
        if not state:
            return elapsed_time
        return end_time - start_time + elapsed_time

