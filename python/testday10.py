import unittest
from . import day10

class TestDay10(unittest.TestCase):
    def test_oneOneIsRepresentedCorrectly(self):
        self.assertEqual(day10.lookAndSay('1'), '11')
    def test_twoOnesBecomeTwoOne(self):
        self.assertEqual(day10.lookAndSay('11'), '21')
    def test_21Becomes1211(self):
        self.assertEqual(day10.lookAndSay('21'), '1211')
    def test_1211Becomes111221(self):
        self.assertEqual(day10.lookAndSay('1211'), '111221')
    def test_111221Becomes312211(self):
        self.assertEqual(day10.lookAndSay('111221'), '312211')


if __name__ == "__main__":
    unittest.main()
