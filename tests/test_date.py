from datetime import datetime, timedelta
import os
import time
import unittest

from freezegun import freeze_time

from timestring import Date


@freeze_time('2017-06-16 19:37:22')
class DateTest(unittest.TestCase):
    def assert_date(self, date_str, expected: datetime):
        _date = Date(date_str)

        self.assertEqual(_date,
                         expected,
                         '\n    Text: ' + date_str
                         + '\nExpected: ' + str(expected)
                         + '\n  Actual: ' + str(_date))

    def test_time_formats(self):
        self.assert_date('november 5 @ 10pm', datetime(2017, 11, 5, 22, 0, 0))

        for time_str in ['11am', '11 AM', '11a', "11 o'clock", "11 oclock",
                         ]:
            self.assert_date(time_str, datetime(2017, 6, 16, 11, 0, 0))
            # TODO: at 11
            # TODO: eleven o'clock
            # TODO: 1100 hours
            # TODO: by
            # TODO: dec 31 11pm
            # TODO: dec 31, 11pm
            # TODO: dec 31 11pm
            # TODO: 11pm, dec 31
            # TODO: dec 31 @ 11pm


def main():
    os.environ['TZ'] = 'UTC'
    time.tzset()
    unittest.main()


if __name__ == '__main__':
    main()
