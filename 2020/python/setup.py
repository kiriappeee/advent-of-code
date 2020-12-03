import sys
solution_template = """import sys

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday{day_number}.txt') as f:
    puzzle_input = [x for x in f.readlines() if x.strip() != ""]

  if args[1] == "1":
    pass
  if args[1] == "2":
    pass
"""

test_template = """import unittest
from . import day{day_number}

class TestDay{day_number}(unittest.TestCase):
  def test_simple(self):
    self.assertTrue(True)

if __name__ == "__main__":
  unittest.main()
"""

args = sys.argv
day_number = args[1]

with open(f'python/day{day_number}.py', 'w') as f:
  f.write(solution_template.format(day_number=day_number))

with open(f'python/test-day{day_number}.py', 'w') as f:
  f.write(test_template.format(day_number=day_number))

with open(f'python/inputday{day_number}.txt', 'w') as f:
  pass
