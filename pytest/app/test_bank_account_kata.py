import unittest
import BankAccountKata


class TestsUnits(unittest.TestCase):

    def test_deposit(self):
        self.assertEqual(BankAccountKata.deposit(100), 100)
        self.assertEqual(BankAccountKata.withdraw(100), -100)


if __name__ == '__main__':
    unittest.main()