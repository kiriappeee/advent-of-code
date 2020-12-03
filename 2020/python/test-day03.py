import unittest
from . import day03

class TestDay03(unittest.TestCase):
  def test_can_get_correct_coord_from_instruction(self):
    starting_coord = [0,0]
    instruction = {
      'r': 3,
      'd': 1
    }
    result = day03.get_coords_after_instruction(starting_coord, instruction)
    expected_result = [3, 1]
    self.assertEqual(result, expected_result)
  
  def test_can_generate_chunk(self):
    hill_map = [
      '..#..#..#..#',
      '#..#..#..#..'
    ]
    final_coord = [15, 1]
    expected_result = [
      '..#..#..#..#',
      '#..#..#..#..#..#..#..#..'
    ]
    day03.refresh_map(hill_map, final_coord)
    self.assertEqual(hill_map, expected_result)

  def test_can_detect_if_tree_or_not(self):
    hill_map = [
      '..#..#..#..#',
      '#..#..#..#..'
    ]
    final_coord = [3, 1]
    self.assertTrue(day03.is_coord_at_tree(hill_map, final_coord))
    final_coord = [4, 1]
    self.assertFalse(day03.is_coord_at_tree(hill_map, final_coord))

  def test_can_count_how_many_trees_in_run(self):
    final_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()
    repeating_instruction = {
      'r': 3,
      'd': 1
    }
    self.assertEqual(day03.count_number_of_trees_on_run(final_map, repeating_instruction), 7)


if __name__ == "__main__":
  unittest.main()
