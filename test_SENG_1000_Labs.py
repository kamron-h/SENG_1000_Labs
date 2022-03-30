import unittest
from main import commission_revenue, interest_revenue, revenue


class MyTestCase(unittest.TestCase):
    def test_commission_revenue(self):
        self.assertEqual(commission_revenue(1_000_000), 50000.0)  # add assertion here

    def test_interest_revenue(self):
        self.assertEqual(interest_revenue(1_000_000), 20000.0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
