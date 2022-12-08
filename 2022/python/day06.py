import sys

def solve_part_one(puzzle_input):
  current_index = 0
  seen = []
  while current_index < len(puzzle_input)-1:
    if puzzle_input[current_index] not in seen:
      seen.append(puzzle_input[current_index])
      current_index += 1
    else:
      current_index = current_index - len(seen) + 1
      seen = []
    if len(seen) == 4:
      break
  return current_index

def solve_part_two(puzzle_input):
  current_index = 0
  seen = []
  while current_index < len(puzzle_input)-1:
    if puzzle_input[current_index] not in seen:
      seen.append(puzzle_input[current_index])
      current_index += 1
    else:
      current_index = current_index - len(seen) + 1
      seen = []
    if len(seen) == 14:
      break
  return current_index

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday06.txt") as f:
    puzzle_input = f.read().rstrip()
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
