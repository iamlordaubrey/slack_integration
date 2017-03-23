import datetime
import unittest

from freezegun import freeze_time

from common.utils import get_date


class GetDateTest(unittest.TestCase):

    @freeze_time("2017-03-15")
    def test_yesterday(self):
        yesterday = get_date('yesterday')

        self.assertEqual(yesterday, datetime.date(2017, 3, 14))

    @freeze_time("2017-03-15")
    def test_today(self):
        today = get_date('today')

        self.assertEqual(today, datetime.date(2017, 3, 15))

    @freeze_time("2017-03-15")
    def test_tomorrow(self):
        tomorrow = get_date('tomorrow')

        self.assertEqual(tomorrow, datetime.date(2017, 3, 16))
