import unittest
from . import day08 as solution


class TestDay08(unittest.TestCase):
  def setUp(self):
    self.test_input = """30373
25512
65332
33549
35390"""

  def test_input_is_converted(self):
    answer_rows, answer_columns = solution.convert_input_to_grid(self.test_input)
    # print(answer_rows)
    # print(answer_columns)
    self.assertEqual(answer_rows[0][0],3)
    self.assertEqual(answer_rows[1][0],2)
    self.assertEqual(answer_columns[0][0],3)
    self.assertEqual(answer_columns[0][1],2)
    self.assertEqual(answer_columns[3][1],1)

  # def test_a_trees_visibility_can_be_detected(self):
  #   pass

  def test_part_one(self):
    answer = solution.solve_part_one(self.test_input)
    print(answer)
    self.assertEqual(answer, 21)


if __name__ == "__main__":
  unittest.main()

