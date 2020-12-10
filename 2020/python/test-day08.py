import unittest
from . import day08

class TestDay08(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.test_instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')

  def test_accumulator_value_and_instruction_are_set_correctly(self):
    current_instruction = 0
    current_accumulator = 0
    visited = []
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, current_instruction, current_accumulator, visited), [1,0])
    self.assertEqual(visited, [0])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 1, 0, visited), [2,1])
    self.assertEqual(visited, [0, 1])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 2, 1, visited), [6,1])
    self.assertEqual(visited, [0, 1, 2])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 6, 1, visited), [7,2])
    self.assertEqual(visited, [0, 1, 2, 6])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 7, 2, visited), [3,2])
    self.assertEqual(visited, [0, 1, 2, 6, 7])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 3, 2, visited), [4,5])
    self.assertEqual(visited, [0, 1, 2, 6, 7, 3])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 4, 5, visited), [1,5])
    self.assertEqual(visited, [0, 1, 2, 6, 7, 3, 4])
    self.assertEqual(day08.execute_single_instruction(self.test_instructions, 1, 5, visited), [-1,5])
    self.assertEqual(visited, [0, 1, 2, 6, 7, 3, 4])

  def test_can_find_instruction_to_change(self):
    self.assertEqual(day08.escape_infinite_loop(self.test_instructions, []), 8)
if __name__ == "__main__":
  unittest.main()
