import unittest
from . import dayXX as solution


class TestDayX(unittest.TestCase):
  def test_puzzle_one(self):
    test_list = []
    answer = solution.solve_part_one(test_list)
    self.assertIsNotNone(answer)


if __name__ == "__main__":
  unittest.main()

