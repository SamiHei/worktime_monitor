#! /usr/bin/python3


import csv
import json


'''
Module which can export periods to .csv and .json format
'''
class ExportModule:


    def __init__(self, periods):
        self.periods = periods


    def export_csv(self):
        with open('periods.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for x in range(0, len(self.periods)):
                writer.writerow(['Period {}'.format(x)])
                writer.writerow(['Date', self.periods[x].get_date()])
                writer.writerow(['Name', self.periods[x].get_name().decode('utf-8')])
                writer.writerow(['Work time', self.periods[x].get_work_time()])
                

    def export_json(self):

        data = {}

        for x in range(0, len(self.periods)):
            data['Period {}'.format(x)] = {}
            data['Period {}'.format(x)].update({
                "Date":self.periods[x].get_date(),
                "Name":self.periods[x].get_name().decode('utf-8'),
                "Work time":self.periods[x].get_work_time()
            })

        with open('periods.json', 'w') as f:
            json.dump(data, f)
