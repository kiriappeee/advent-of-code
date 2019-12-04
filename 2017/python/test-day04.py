import unittest
from . import day04

class TestDay4(unittest.TestCase):
    def test_valid_passphrase_is_recognised(self):
        self.assertTrue(day04.is_passphrase_valid('aa bb cc dd ee'))
        self.assertTrue(day04.is_passphrase_valid('aa bb cc dd aaa'))
    def test_invalid_passphrase_is_recognised(self):
        self.assertFalse(day04.is_passphrase_valid('aa bb cc dd aa'))

    def test_invalid_passphrase_under_new_rules_is_recognised(self):
        self.assertFalse(day04.is_passphrase_valid_with_new_rules('abcde xyz ecdab'))
if __name__ == "__main__":
    unittest.main()