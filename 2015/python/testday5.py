import unittest
from . import day5

class TestDay5PartOne(unittest.TestCase):
    def test_niceStringIsNice(self):
        self.assertTrue(day5.isStringNicePartOne('aaei'))
        self.assertTrue(day5.isStringNicePartOne('aaa'))
        self.assertTrue(day5.isStringNicePartOne('aeizz'))
    def test_naughtyStringIsNaughty(self):
        self.assertFalse(day5.isStringNicePartOne('aa'))
        self.assertFalse(day5.isStringNicePartOne('abaeezxx'))
        self.assertFalse(day5.isStringNicePartOne('cdaeezxx'))
        self.assertFalse(day5.isStringNicePartOne('pqaeezxx'))
        self.assertFalse(day5.isStringNicePartOne('xyaeezxx'))

class TestDay5PartTwo(unittest.TestCase):
    def test_niceStringIsNice(self):
        self.assertTrue(day5.isStringNicePartTwo('qjhvhtzxzqqjkmpb'))
        self.assertTrue(day5.isStringNicePartTwo('xxyxx'))
        #self.assertTrue(day5.isStringNicePartTwo('aeizz'))
    def test_naughtyStringIsNaughty(self):
        self.assertFalse(day5.isStringNicePartTwo('uurcxstgmygtbstg'))
        self.assertFalse(day5.isStringNicePartTwo('ieodomkazucvgmuy'))

if __name__ == "__main__":
    unittest.main()
