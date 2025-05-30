import datediff
import pathlib
from dateutil.parser import parse
import json

# Run cmd: python3 -m pytest

TODAY = parse('2025-05-05', dayfirst=False, yearfirst=True)

class TestDateDiff:
    def test_date_calcs(self):
        assert datediff.DateDiff.today_diff('2025-01-01', TODAY) == {'years': 0, 'months': 4, 'days': 124}
        assert datediff.DateDiff.today_diff('2025-01-02', TODAY) == {'years': 0, 'months': 4, 'days': 123}
        assert datediff.DateDiff.today_diff('2020-01-01', TODAY) == {'years': 5, 'months': 64, 'days': 1951}
        assert datediff.DateDiff.today_diff('2025-05-06', TODAY) == {'years': 0, 'months': 0, 'days': -1}
        assert datediff.DateDiff.today_diff('2025-06-05', TODAY) == {'years': 0, 'months': -1, 'days': -31}
        assert datediff.DateDiff.today_diff('2026-05-05', TODAY) == {'years': -1, 'months': -12, 'days': -365}
        assert datediff.DateDiff.today_diff('2025-05-05', TODAY) == {'years': 0, 'months': 0, 'days': 0}

    def test_read_file(self):
        with open(datediff.DateDiff.INPUT_FILE, 'w') as f:
            f.write('run,2025-05-05')
            f.close

        assert datediff.DateDiff.read_file() == '2025-05-05'

        with open(datediff.DateDiff.INPUT_FILE, 'w') as f:
            f.write('STOP,2025-05-05')
            f.close

        assert datediff.DateDiff.read_file() == False

    def test_full(self):
        # Blank the output file

        with open(datediff.DateDiff.OUTPUT_FILE, "w") as f:
            f.seek(0)
            f.truncate()
            f.close()

        # Create the input file with the right command
        with open(datediff.DateDiff.INPUT_FILE, 'w') as f:
            f.write('run,2000-05-05')
            f.close

        # Simulate the service running via commands
        distance_date = datediff.DateDiff.read_file()
        calc = datediff.DateDiff.today_diff(distance_date)
        datediff.DateDiff.write_response(calc)

        # Look for output file to have the right data
        with open(datediff.DateDiff.OUTPUT_FILE, "r+") as f:
            data = json.load(f)

        # Difficult to test exact values because we don't know what "today" is
        # But safe to assume the file starts empty so if we populated a dict with numbers, we're good
        assert data['days'] > 1
        assert data['months'] > 1
        assert data['years'] > 1
