import unittest
from . import dayXX


class TestDayX(unittest.TestCase):
  def test_puzzle_one(self):
    test_list = []
    answer = dayXX.solve_part_one(test_list)
    self.assertIsNotNone(answer)


if __name__ == "__main__":
  unittest.main()

