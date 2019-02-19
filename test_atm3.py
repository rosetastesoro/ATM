import unittest
from my_money import *


class Test_atm(unittest.TestCase):


    def test_attempt1(self):
        attempt1 = terminal.enter_pin(111)

    def test_count_attempts_1(self):
        self.assertEqual(terminal.attempts, 1)

    def test_enter_pin(self):
        self.assertTrue(terminal.enter_pin(777))

    def test_attempt0(self):
        attempt2 = terminal.enter_pin(777)

    def test_get_money(self):
        self.assertEqual(terminal.get_money(300), 300)

    def test_check_balance(self):
        self.assertEqual(terminal.check_balance(), 9700)

    def test_get_money2(self):
        self.assertEqual(terminal.get_money(9600), 9600)
