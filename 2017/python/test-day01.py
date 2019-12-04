import unittest
from . import day01

class TestDay1Part1Solution(unittest.TestCase):
    def test_1122_returns_3(self):
        self.assertEqual(day01.solve_captcha("1122"), 3, "captcha for 1122 should return 3")
    def test_1111_returns_4(self):
        self.assertEqual(day01.solve_captcha("1111"), 4)
    def test_1234_returns_0(self):
        self.assertEqual(day01.solve_captcha("1234"), 0)
    def test_91212129_returns_9(self):
        self.assertEqual(day01.solve_captcha("91212129"), 9)

class TestDay1Part2Solution(unittest.TestCase):
    def test_1212_returns_6(self):
        self.assertEqual(day01.solve_captcha_part_two("1212"), 6)

    def test_1221_returns_0(self):
        self.assertEqual(day01.solve_captcha_part_two("1221"), 0)

    def test_123425_returns_4(self):
        self.assertEqual(day01.solve_captcha_part_two("123425"), 4)

    def test_123123_returns_12(self):
        self.assertEqual(day01.solve_captcha_part_two("123123"), 12)

    def test_12131415_returns_4(self):
        self.assertEqual(day01.solve_captcha_part_two("12131415"), 4)

if __name__ == "__main__":
    unittest.main()