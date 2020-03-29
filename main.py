#! /usr/bin/python3


from data_structure.period import Period


class Monitor:

    def main():
        test_period = Period("10.10.2010", "5h")
        date, work_time = test_period.get_period()
        print(date)
        print(work_time)


    if __name__=='__main__':
        main()

