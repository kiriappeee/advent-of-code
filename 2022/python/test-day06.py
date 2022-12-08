import unittest
from . import day06 as solution


class TestDay6(unittest.TestCase):
  def setUp(self):
    self.test_inputs = [
      "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
      "bvwbjplbgvbhsrlpgdmjqwftvncz",
      "nppdvjthqldpwncqszvftbrmjlhg",
      "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
      "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    ]
  def test_solution_for_part_one_is_found(self):
    self.assertEqual(solution.solve_part_one(self.test_inputs[0]), 7)
    self.assertEqual(solution.solve_part_one(self.test_inputs[1]), 5)
    self.assertEqual(solution.solve_part_one(self.test_inputs[2]), 6)
    self.assertEqual(solution.solve_part_one(self.test_inputs[3]), 10)
    self.assertEqual(solution.solve_part_one(self.test_inputs[4]), 11)

  def test_solution_for_part_two_is_found(self):
    self.assertEqual(solution.solve_part_two(self.test_inputs[0]), 19)
    self.assertEqual(solution.solve_part_two(self.test_inputs[1]), 23)
    self.assertEqual(solution.solve_part_two(self.test_inputs[2]), 23)
    self.assertEqual(solution.solve_part_two(self.test_inputs[3]), 29)
    self.assertEqual(solution.solve_part_two(self.test_inputs[4]), 26)

if __name__ == "__main__":
  unittest.main()

