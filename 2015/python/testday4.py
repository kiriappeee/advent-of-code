import unittest
from . import day4

class TestDay4(unittest.TestCase):
    def test_validHashIsValid(self):
        self.assertTrue(day4.isHashValid('000001dbbfa3a5c83a2d506429c7b00e'))
    def test_invalidHashIsInvalid(self):
        self.assertFalse(day4.isHashValid('000021dbbfa3a5c83a2d506429c7b00e'))
    def test_hashIsMadeCorrectly(self):
        self.assertEqual(day4.makeHash('abcdef', day4.isHashValid), (609043,'000001dbbfa3a5c83a2d506429c7b00e'))

if __name__ == "__main__":
    unittest.main()
