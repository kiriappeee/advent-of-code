import unittest
from . import day04 as solution


class TestDayX(unittest.TestCase):
  def setUp(self):
    self.test_list = [x.strip() for x in """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")]

  def test_raw_input_is_processed(self):
    answer = solution.convert_raw_input(self.test_list)
    self.assertEqual(answer[0], [[2,4], [6,8]])
    self.assertEqual(answer[1], [[2,3], [4,5]])
    self.assertEqual(answer[2], [[5,7], [7,9]])

  def test_number_of_fully_overlapping_pairs_found(self):
    answer = solution.solve_part_one(solution.convert_raw_input(self.test_list))
    self.assertEqual(answer, 2)

  def test_number_of_partial_overlapping_pairs_found(self):
    answer = solution.solve_part_two(solution.convert_raw_input(self.test_list))
    self.assertEqual(answer, 4)



if __name__ == "__main__":
  unittest.main()

