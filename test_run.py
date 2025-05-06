import datediff
import pathlib
from dateutil.parser import parse

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

        self.delete_input_file()

    def delete_input_file(self):
        pathlib.Path(datediff.DateDiff.INPUT_FILE).unlink(missing_ok=True)

    def delete_output_file(self):
        pathlib.Path(datediff.DateDiff.OUTPUT_FILE).unlink(missing_ok=True)
