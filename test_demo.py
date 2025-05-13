import datediff
import pathlib
from dateutil.parser import parse
import json
import time

# Run cmd: python3 -m pytest

TODAY = parse('2025-05-05', dayfirst=False, yearfirst=True)

class TestDateDiff:
    # In order for this test to pass, the microservice must be running on the machine
    def test_full(self):
        # Blank the output file

        with open(datediff.DateDiff.OUTPUT_FILE, "w") as f:
            f.seek(0)
            f.truncate()
            f.close()

        # Create the input file with the right command
        with open(datediff.DateDiff.INPUT_FILE, 'w') as f:
            f.write('run,2000-05-05')
            f.close()

        # wait long enough for the service to response
        time.sleep(10)

        # Look for output file to have the right data
        with open(datediff.DateDiff.OUTPUT_FILE, "r+") as f:
            data = json.load(f)
            f.close()

        # Difficult to test exact values because we don't know what "today" is
        # But safe to assume the file starts empty so if we populated a dict with numbers, we're good
        assert data['days'] > 1
        assert data['months'] > 1
        assert data['years'] > 1
