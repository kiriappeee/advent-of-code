import sys

def solve_part_one(puzzle_input):
  pass

def solve_part_two(puzzle_input):
  pass

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputdayXX.txt") as f:
    puzzle_input = [x for x in f.readlines() if x.strip != ""]
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
