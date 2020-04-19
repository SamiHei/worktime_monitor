#! /usr/bin/python3

import time


'''
Timer module uses Python3 time standard library

     state = Stopped/Running/Paused
     start_time = takes time in seconds since the epoch
     elapsed_time = saves measured time if timer is paused
     end_time = takes new time in seconds since the epoch

'''
class TimerModule:


    def __init__(self):
        self.state = "Stopped"
        self.start_time = 0
        self.elapsed_time = 0
        self.end_time = 0


    def get_state(self):
        return self.state


    '''
    Takes time in seconds since the epoch and uses that as the start time
    '''
    def start_timer(self):
        if (self.start_time == 0):
            self.start_time = time.time()
            self.state = "Running"


    '''
    "Pauses" the running timer
    '''
    def pause_timer(self):
        if (self.state == "Running"):
            self.state = "Paused"
            self.elapsed_time += (time.time() - self.start_time)


    '''
    "Continues" the running timer if the state is paused
    '''        
    def continue_timer(self):
        if (self.state == "Paused"):
            self.state = "Running"
            self.start_time = time.time()


    '''
    Stops the timer and returns the measured time according if the timer was running or stopped
    '''
    def stop_timer(self):
        if (self.state == "Paused"):
            return self.elapsed_time
        else:
            self.state = "Stopped"
            return (self.end_time - self.start_time + self.elapsed_time)


    def print_timer_state(self, status):
        print("Timer " + status)
