import unittest
from . import day05 as solution


class TestDayX(unittest.TestCase):
  def setUp(self):
    self.test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    self.processed_test_input = {
      "stacks": {
        1: ["Z", "N"],
        2: ["M", "C", "D"],
        3: ["P"]
      },
      "instructions": [[1,2,1], [3,1,3], [2,2,1], [1,1,2]]
    }

  def test_can_process_input(self):
    answer = solution.process_input(self.test_input)
    self.assertEqual(answer, self.processed_test_input)

  def test_instruction_can_be_executed(self):
    answer = solution.execute_instructions(self.processed_test_input)
    expected_answer =  {
      "stacks": {
        1: ["C"],
        2: ["M"],
        3: ["P", "D", "N", "Z"]
      },
      "instructions": [[1,2,1], [3,1,3], [2,2,1], [1,1,2]]
    }
    self.assertEqual(answer, expected_answer)

  def test_final_output_for_part_one(self):
    answer = solution.solve_part_one(self.test_input)
    self.assertEqual(answer, "CMZ")

  def test_new_instructions_can_be_executed(self):
    answer = solution.execute_instructions_9001(self.processed_test_input)
    expected_answer =  {
      "stacks": {
        1: ["M"],
        2: ["C"],
        3: ["P", "Z", "N", "D"]
      },
      "instructions": [[1,2,1], [3,1,3], [2,2,1], [1,1,2]]
    }
    self.assertEqual(answer, expected_answer)

  def test_final_output_for_part_two(self):
    answer = solution.solve_part_two(self.test_input)
    self.assertEqual(answer, "MCD")

if __name__ == "__main__":
  unittest.main()

