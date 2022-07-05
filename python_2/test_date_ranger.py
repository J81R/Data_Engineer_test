import unittest
import date_ranger
from datetime import datetime
from datetime import timedelta

class TestDateRanger(unittest.TestCase):

    def setUp(self):
        self.drange = date_ranger.DateRanger('2022-06-24')
        self.drange_today = date_ranger.DateRanger(datetime.now().strftime('%Y-%m-%d'))

    def test_constructor(self):
        self.assertIsInstance(self.drange,date_ranger.DateRanger)

    def test_bad_formats(self):
        self.assertRaises(ValueError,date_ranger.DateRanger,'28-06-2022')
        self.assertRaises(ValueError,date_ranger.DateRanger,'20220628')
        self.assertRaises(ValueError,date_ranger.DateRanger,'just a text')
        self.assertRaises(ValueError,date_ranger.DateRanger,'2022-06-28 08:08:08')

    def test_greater_date(self):
        self.assertRaises(ValueError,date_ranger.DateRanger,(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'))

    def test_next(self):
        date1 = next(self.drange.next_date)
        date2 = next(self.drange.next_date)
        date3 = next(self.drange.next_date)

        self.assertEqual(date1,datetime.strptime('2022-06-24', '%Y-%m-%d').date())
        self.assertEqual(date2,datetime.strptime('2022-06-25', '%Y-%m-%d').date())
        self.assertEqual(date3,datetime.strptime('2022-06-26', '%Y-%m-%d').date())

    def test_end(self):
        next(self.drange_today.next_date)
        with self.assertRaises(StopIteration):
            next(self.drange_today.next_date)



if __name__=='__main__':
    unittest.main()


