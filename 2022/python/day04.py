import sys

def convert_raw_input(puzzle_input):
  tasks = []
  for line in puzzle_input:
    task_a, task_b = line.split(",")
    task_a_range = [int(x) for x in task_a.split("-")]
    task_b_range = [int(x) for x in task_b.split("-")]
    tasks.append([task_a_range, task_b_range])
  return tasks

def solve_part_one(puzzle_input):
  number_of_overlapping_pairs = 0
  for task in puzzle_input:
    taskA = set(range(task[0][0],task[0][1]+1))
    taskB = set(range(task[1][0],task[1][1]+1))
    if taskA.issuperset(taskB) or taskB.issuperset(taskA):
      number_of_overlapping_pairs += 1
  return number_of_overlapping_pairs


def solve_part_two(puzzle_input):
  number_of_overlapping_pairs = 0
  for task in puzzle_input:
    taskA = set(range(task[0][0],task[0][1]+1))
    taskB = set(range(task[1][0],task[1][1]+1))
    if len(taskA.intersection(taskB)):
      number_of_overlapping_pairs += 1
  return number_of_overlapping_pairs

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday04.txt") as f:
    puzzle_input = convert_raw_input([x.strip() for x in f.readlines() if x.strip() != ""])
  # print(len(puzzle_input))
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
