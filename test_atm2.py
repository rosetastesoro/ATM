import unittest
from my_money import *


class Test_atm(unittest.TestCase):

    def test_attempt1(self):
        attempt1 = terminal.enter_pin(111)

    def test_attempt2(self):
        attempt2 = terminal.enter_pin(222)

    def test_count_attempts_1(self):
        self.assertEqual(terminal.attempts, 0)

    def test_count_attempts_2(self):
        self.assertEqual(terminal.client_can_get_money, False)
