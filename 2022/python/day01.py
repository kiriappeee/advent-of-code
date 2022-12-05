import sys

def break_down_raw_input(raw_input):
  broken_down_output = []
  working_list = []
  for line in raw_input.split("\n"):
    if line.strip() == "":
      broken_down_output.append(working_list)
      working_list = []
    else:
      working_list.append(int(line))
  return broken_down_output

def get_highest_calorie_count(elf_food_list):
  calorie_list = []
  for elf_food_listing in elf_food_list:
    calorie_list.append(sum(elf_food_listing))
  return max(calorie_list)

def get_three_highest_calorie_counts(elf_food_list):
  calorie_list = []
  for elf_food_listing in elf_food_list:
    calorie_list.append(sum(elf_food_listing))
  calorie_list.sort(reverse=True)
  return calorie_list[0:3]

def solve_part_one(puzzle_input):
  print(get_highest_calorie_count(puzzle_input))

def solve_part_two(puzzle_input):
  print(sum(get_three_highest_calorie_counts(puzzle_input)))

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday01.txt") as f:
    puzzle_input = break_down_raw_input(f.read())
  print(len(puzzle_input))
  if args[1] == "1":
    solve_part_one(puzzle_input)
  elif args[1] == "2":
    solve_part_two(puzzle_input)
  else:
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)