import unittest
from . import day07 as solution


class TestDay7(unittest.TestCase):
  def setUp(self):
    self.test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

  def test_input_can_be_converted_to_directory(self):
    answer = solution.convert_commands_to_directory(self.test_input)
    print(answer)
    # self.assertEqual(answer["/"]["size"], 48381165)
    # self.assertEqual(answer["/"]["dirs"]["a"]["size"], 94853)
    # self.assertEqual(answer["/"]["dirs"]["d"]["size"], 24933642)
    # self.assertEqual(answer["/"]["dirs"]["a"]["dirs"]["e"]["size"], 584)
    # self.assertEqual(answer["/"]["dirs"]["a"]["dirs"]["e"]["files"]["i"], 584)
    # self.assertEqual(answer["/"]["dirs"]["d"]["files"]["k"], 7214296)
    self.assertEqual(answer["/"]["size"], 48381165)
    self.assertEqual(answer["/a"]["size"], 94853)
    self.assertEqual(answer["/d"]["size"], 24933642)
    self.assertEqual(answer["/a/e"]["size"], 584)
    self.assertEqual(answer["/a/e"]["files"]["i"], 584)
    self.assertEqual(answer["/d"]["files"]["k"], 7214296)

  def test_solution_one(self):
    answer = solution.solve_part_one(self.test_input)
    self.assertEqual(answer, 95437)
  
  def test_solution_two(self):
    answer = solution.solve_part_two(self.test_input)
    self.assertEqual(answer, 24933642)

if __name__ == "__main__":
  unittest.main()

