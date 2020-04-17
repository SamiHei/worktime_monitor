#! /usr/bin/python3

import time

'''
Timer module uses Python3 time standard library
     state = True/False - is timer running or paused
     start_time = takes time in seconds since the epoch
     elapsed_time = saves measured time if timer is paused
     end_time = takes new time in seconds since the epoch
'''
class TimerModule:


    def __init__(self):
        self.state = False
        self.start_time = 0
        self.elapsed_time = 0
        self.end_time = 0


    '''
    Takes time in seconds since the epoch and uses that as the start time
    '''
    def start_timer(self):
        if (self.start_time is 0):
            self.start_time = time.time()
            self.state = True
        else:
            print("Timer allready started!")


    '''
    "Pauses" the running timer
    '''
    def pause_timer(self):
        if (self.state is True):
            self.state = False
            elapsed_time += (time.time() - self.start_time)
            print("Timer paused at: ",elapsed_time) # TODO: Bring this to console view
        else:
            print("Timer allready paused!") # TODO: Bring this to console view


    '''
    "Continues" the running timer if the state is paused
    '''        
    def continue_timer(self):
        if (self.state is False):
            self.state = True
            self.start_time = time.time()
        else:
            print("Timer allready running!") # TODO: Bring this to console view


    '''
    Stops the timer and returns the measured time according if the timer was running or stopped
    '''
    def stop_timer(self):
        if (self.state is False):
            return elapsed_time
        else:
            return (self.end_time - self.start_time + self.elapsed_time)


    def print_timer_state(self, status):
        print("Timer " + status)
