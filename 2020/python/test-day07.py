import unittest
from . import day07

class TestDay07(unittest.TestCase):
  def test_lines_can_be_broken_down_into_definition_correctly(self):
    test_input = [
      "light red bags contain 1 bright white bag, 2 muted yellow bags.",
      "dark orange bags contain 3 bright white bags, 4 muted yellow bags."
    ]
    expected_output = {
      "light red": {
        "bright white": 1,
        "muted yellow": 2
      },
      "dark orange": {
        "bright white": 3,
        "muted yellow": 4
      }
    }
    self.assertEqual(day07.get_colour_map(test_input), expected_output)
  def test_lines_without_further_colours_are_broken_down_correctly(self):
    test_input = [
      "light red bags contain 1 bright white bag, 2 muted yellow bags.",
      "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
      "faded blue bags contain no other bags.",
      "dotted black bags contain no other bags."
    ]
    expected_output = {
      "light red": {
        "bright white": 1,
        "muted yellow": 2
      },
      "dark orange": {
        "bright white": 3,
        "muted yellow": 4
      },
      "faded blue": {},
      "dotted black": {}
    }
    self.assertEqual(day07.get_colour_map(test_input), expected_output)
  
    test_input = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".split('\n')

    expected_output = {
      "light red": {
        "bright white": 1,
        "muted yellow": 2
      },
      "dark orange": {
        "bright white": 3,
        "muted yellow": 4
      },
      "bright white": {
        "shiny gold": 1
      },
      "muted yellow": {
        "shiny gold": 2,
        "faded blue": 9
      },
      "shiny gold": {
        "dark olive": 1,
        "vibrant plum": 2
      },
      "dark olive": {
        "faded blue": 3,
        "dotted black": 4
      },
      "vibrant plum": {
        "faded blue": 5,
        "dotted black": 6,
      },
      "faded blue": {},
      "dotted black": {}
    }

    self.assertEqual(day07.get_colour_map(test_input), expected_output)

  def test_number_of_bags_that_eventuall_contain_a_given_colour_detected_correctly(self):
    test_input = {
      "light red": {
        "bright white": 1,
        "muted yellow": 2
      },
      "dark orange": {
        "bright white": 3,
        "muted yellow": 4
      },
      "bright white": {
        "shiny gold": 1
      },
      "muted yellow": {
        "shiny gold": 2,
        "faded blue": 9
      },
      "shiny gold": {
        "dark olive": 1,
        "vibrant plum": 2
      },
      "dark olive": {
        "faded blue": 3,
        "dotted black": 4
      },
      "vibrant plum": {
        "faded blue": 5,
        "dotted black": 6,
      },
      "faded blue": {},
      "dotted black": {}
    }

    self.assertEqual(day07.get_bags_that_eventually_contain_given_colour("shiny gold", test_input), 4)

if __name__ == "__main__":
  unittest.main()
