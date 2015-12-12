import unittest
from . import day8

class Test_Day8(unittest.TestCase):
    def test_twoDoubleQuotesIsAnEmptyString(self):
        self.assertEqual(day8.numberOfCharacters('""'), 0)
    def test_basicStringCountsOnlyCharactersInBetween(self):
        self.assertEqual(day8.numberOfCharacters('"abc"'), 3)
    def test_escapedQuoteIsCountedAsSingleCharacter(self):
        self.assertEqual(day8.numberOfCharacters('"aaa\\"aaa"'), 7)
    def test_doubleBackslashIsCountedAsSingleCharacter(self):
        self.assertEqual(day8.numberOfCharacters('"aaa\\\\aaa"'), 7)
        self.assertEqual(day8.numberOfCharacters('"hey\\\\"'), 4)
    def test_hexadecimalIsCountedAsSingleCharacter(self):
        self.assertEqual(day8.numberOfCharacters('"\\xae"'), 1)
        self.assertEqual(day8.numberOfCharacters('"\\x27"'), 1)
        self.assertEqual(day8.numberOfCharacters('"aaa\\xaeaaa"'), 7)
        self.assertEqual(day8.numberOfCharacters('"aaa\\xaeaaa\\x93"'), 8)
    def test_numberOfCharactersOfCodeCountedCorrectly(self):
        self.assertEqual(day8.numberOfCharactersOfCode('"abc"'), 5)
        self.assertEqual(day8.numberOfCharactersOfCode('"aaa\\"aaa"'), 10)
        self.assertEqual(day8.numberOfCharactersOfCode('"\\xae"'), 6)
        self.assertEqual(day8.numberOfCharactersOfCode('"\\x27"'), 6)
        print(day8.numberOfCharacters('"uzezxa\\"jgbmojtwyfbfguz"'))
        print(day8.numberOfCharactersOfCode('"uzezxa\\"jgbmojtwyfbfguz"'))

if __name__ == "__main__":
    unittest.main()
