import unittest
from . import day02


class TestDay2(unittest.TestCase):
    def test_single_round_score_can_be_calculated(self):
      test_input = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z")
      ]
      answer = day02.get_round_result(test_input[0])
      self.assertEqual(answer, 8)
      answer = day02.get_round_result(test_input[1])
      self.assertEqual(answer, 1)
      answer = day02.get_round_result(test_input[2])
      self.assertEqual(answer, 6)

    def test_total_score_is_calculated(self):
      test_input = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z")
      ]
      answer = day02.solve_part_one(test_input)
      self.assertEqual(answer, 15)

    def test_correct_response_can_be_given(self):
      test_input = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z")
      ]
      answer = day02.get_response(test_input[0])
      self.assertEqual(answer, "A")
      answer = day02.get_response(test_input[1])
      self.assertEqual(answer, "A")
      answer = day02.get_response(test_input[2])
      self.assertEqual(answer, "A")

    def test_total_score_is_calculated_with_new_instructions(self):
      test_input = [
        ("A", "Y"),
        ("B", "X"),
        ("C", "Z")
      ]
      answer = day02.solve_part_two(test_input)
      self.assertEqual(answer, 12)


if __name__ == "__main__":
    unittest.main()

