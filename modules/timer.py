#! /usr/bin/python3

import time


class TimerModule:

    
    """
    "Takes time" until user gives input to pause, continue or stop
    """
    def time_it(self):
        start_time = time.time()
        elapsed_time = 0
        state = True
        print("Timer started!")
        self.print_instructions()
        while True:
            str = input()

            if (str == "0" or str == "h" or str == "help"):
                self.print_instructions()
            if (str == "1" or str == "p" or str == "pause"):
                state = False
                self.print_timer_state("paused")
                end_time = time.time()
                elapsed_time += end_time - start_time
            if ((str == "2" or str == "c" or str == "continue") and state == False):
                state = True
                self.print_timer_state("continued")
                start_time = time.time()
            if (str == "3" or str == "s" or str == "stop"):
                self.print_timer_state("stopped")
                end_time = time.time()
                break
            
        if not state:
            return elapsed_time
        return end_time - start_time + elapsed_time


    def print_instructions(self):
        print("=" * 33)
        print("| Help:\t\t0|h|help\t|")
        print("| Pause:\t1|p|pause\t|")
        print("| Continue:\t2|c|continue\t|")
        print("| Stop:\t\t3|s|stop\t|")
        print("=" * 33)


    def print_timer_state(self, status):
        print("Timer " + status)
