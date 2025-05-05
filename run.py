import datediff
import time

# Need: pip install python-dateutil
print('********************************************************************************')
print('Starting DateDiff microservice')
print('CTRL-C to stop')
print('********************************************************************************')

distance_date = False

while (True):
    while (not distance_date):
        distance_date = datediff.DateDiff.read_file()
        print('Nothing to do - sleeping')
        time.sleep(3)

    print('Time to work!')
    calc = datediff.DateDiff.today_diff(distance_date)
    distance_date = False

    datediff.DateDiff.write_response(calc)
