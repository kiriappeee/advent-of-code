import unittest
from . import day01


class TestDayX(unittest.TestCase):
    def test_puzzle_input_can_be_broken_down(self):
      raw_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
      """
      expected_output = [
        [1000,2000,3000],
        [4000],
        [5000,6000],
        [7000,8000,9000],
        [10000]
      ]
      answer = day01.break_down_raw_input(raw_input)
      self.assertEqual(answer, expected_output)

    def test_highest_calorie_count_is_found(self):
      test_input = [
        [1000,2000,3000],
        [4000],
        [5000,6000],
        [7000,8000,9000],
        [10000]
      ]
      answer = day01.get_highest_calorie_count(test_input)
      self.assertEqual(answer, 24000)

    def test_top_three_highest_calorie_counts_can_be_found(self):
      test_input = [
        [1000,2000,3000],
        [4000],
        [5000,6000],
        [7000,8000,9000],
        [10000]
      ]
      answer = day01.get_three_highest_calorie_counts(test_input)
      self.assertEqual(answer, [24000,11000,10000])


if __name__ == "__main__":
    unittest.main()

