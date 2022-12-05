import unittest
from . import day03


class TestDay3(unittest.TestCase):
  def setUp(self):
    self.test_list = [
      "vJrwpWtwJgWrhcsFMMfFFhFp",
      "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
      "PmmdzqPrVvPwwTWBwg",
      "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
      "ttgJtRGJQctTZtZT",
      "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
  def test_duplicate_item_can_be_found(self):
    answer = day03.find_duplicate_item(self.test_list[0])
    self.assertEqual(answer, 'p')
    answer = day03.find_duplicate_item(self.test_list[1])
    self.assertEqual(answer, 'L')
    answer = day03.find_duplicate_item(self.test_list[2])
    self.assertEqual(answer, 'P')
    answer = day03.find_duplicate_item(self.test_list[3])
    self.assertEqual(answer, 'v')
    answer = day03.find_duplicate_item(self.test_list[4])
    self.assertEqual(answer, 't')
    answer = day03.find_duplicate_item(self.test_list[5])
    self.assertEqual(answer, 's')

  def test_total_priority_sum_can_be_found(self):
    answer = day03.solve_part_one(self.test_list)
    self.assertEqual(answer, 157)

  def test_badge_can_be_found(self):
    answer = day03.find_badge(self.test_list[0:3])
    self.assertEqual(answer, 'r')

  def test_priority_score_of_badges_is_found(self):
    answer = day03.solve_part_two(self.test_list)
    self.assertEqual(answer, 70)


if __name__ == "__main__":
  unittest.main()

