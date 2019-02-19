import unittest
from my_money import *


class Test_atm(unittest.TestCase):

    def test_atm_balance(self):
        self.assertEqual(terminal.atm_balance, 10000)

    def test_atm_balance_2(self):
        self.assertEqual(terminal.atm_balance, 10001)

    def test_atm_balance_3(self):
        self.assertEqual(terminal.atm_balance, 9999)

    def test_atm_attempts(self):
        self.assertEqual(terminal.attempts, 2)

    def test_rise_money(self):
        self.assertEqual(terminal.rise_money(100), 10100)

    def test_rise_money_2(self):
        self.assertEqual(terminal.rise_money(-10), 10010)

    def test_attempt0(self):
        attempt2 = terminal.enter_pin(777)

    def test_count_attempts_0(self):
        self.assertEqual(terminal.client_can_get_money, True)

    def test_check_balance(self):
        self.assertEqual(terminal.atm_balance, 10000)

    def test_enter_wrong_pin(self):
        self.assertEqual(terminal.enter_pin(301), 777)

    def test_enter_right_pin(self):
        self.assertTrue(terminal.enter_pin(777))
