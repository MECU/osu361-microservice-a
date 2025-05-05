import csv
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import time
import json


# Need: pip install python-dateutil
print('********************************************************************************')
print('Starting DateDiff microservice')
print('CTRL-C to stop')
print('********************************************************************************')

distance_date = False

class DateDiff:
    INPUT_FILE = 'rundifference.csv'
    OUTPUT_FILE = 'datadifference.json'

    def read_file():
        try:
            with open(DateDiff.INPUT_FILE, "r+") as f:
                contents = csv.reader(f, delimiter=',')
                for row in contents:
                    if (row[0] != 'run'):
                        return False

                    distance_date = row[1]

                f.seek(0)
                f.truncate()
                f.close()
            return distance_date
        except:
            return False


    # d2 is a string
    # return {days: <days>, months: <months>, years: <years>}
    def today_diff(d2):
        today = datetime.today()
        d0 = parse(distance_date, dayfirst=True, yearfirst=True)

        delta = today - d0
        difference = relativedelta(today, d0)

        response = {
            'days': delta.days,
            'months': difference.months + 12 * difference.years,
            'years': difference.years
        }

        return response

    # calc is a Dict, the response from today_diff
    def write_response(calc):
        with open(DateDiff.OUTPUT_FILE, 'w') as o:
            try:
                json.dump(calc, o, ensure_ascii=False, indent=4)
            finally:
                o.close()

while (True):
    while (not distance_date):
        distance_date = DateDiff.read_file()
        print('Nothing to do - sleeping')
        time.sleep(1)

    print('Time to work!')
    calc = DateDiff.today_diff(distance_date)
    distance_date = False

    DateDiff.write_response(calc)


