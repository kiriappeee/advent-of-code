import sys


def find_duplicate_item(rucksack_items):
  compartment_1 = set(rucksack_items[0:len(rucksack_items)//2])
  compartment_2 = set(rucksack_items[len(rucksack_items)//2:])
  return compartment_1.intersection(compartment_2).pop()

def find_badge(rucksacks):
  rucksack_1 = set(rucksacks[0])
  rucksack_2 = set(rucksacks[1])
  rucksack_3 = set(rucksacks[2])
  return set.intersection(rucksack_1, rucksack_2, rucksack_3).pop()

def get_priority_score(item):
    if item.isupper():
      return ord(item) - 38
    else:
      return ord(item) - 96

def solve_part_one(puzzle_input):
  priority_score = 0
  for rucksack in puzzle_input:
    duplicate_item = find_duplicate_item(rucksack)
    if duplicate_item.isupper():
      priority_score += get_priority_score(duplicate_item)
    else:
      priority_score += get_priority_score(duplicate_item)
  return priority_score


def solve_part_two(puzzle_input):
  count = 0
  badge_priority_score = 0
  while count < len(puzzle_input):
    # print(count)
    # print(puzzle_input[count:count+3])
    # print(find_badge(puzzle_input[count:count+3]))
    badge_priority_score += get_priority_score(find_badge(puzzle_input[count:count+3]))
    count += 3
  return badge_priority_score

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday03.txt") as f:
    puzzle_input = [x.strip() for x in f.readlines() if x.strip() != ""]
  if args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
  else:
    solve_part_one(puzzle_input)
    solve_part_two(puzzle_input)
