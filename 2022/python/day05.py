import sys
import re

def process_input(raw_input):
  lines = raw_input.split("\n")
  break_index = 0
  final_output = {
    "stacks": {},
    "instructions": []
  }
  for line in lines:
    if line.strip() == "":
      break
    break_index += 1
  stacks_text = [s.replace("\n", "") for s in lines[0:break_index] if s.strip() != ""]
  instructions_text = [i.strip() for i in lines[break_index+1:] if i.strip() != ""]
  number_of_stacks = int(stacks_text[-1].strip()[-1])
  for i in range(1, number_of_stacks+1):
    final_output["stacks"][i] = []
  # 1,5,9
  for stack_line in stacks_text[:-1]:
    for i in range(1, number_of_stacks+1):
      stack_item = stack_line[1+((i-1)*4)]
      if stack_item.strip() != "":
        final_output["stacks"][i].insert(0,stack_item)
  
  r = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')
  for instruction_line in instructions_text:
    final_output["instructions"].append([int(n) for n in r.findall(instruction_line)[0]])
  return final_output
      
def execute_instructions(stack_and_instructions):
  for instruction in stack_and_instructions["instructions"]:
    for i in range(0,instruction[0]):
      stack_and_instructions["stacks"][instruction[2]].append(stack_and_instructions["stacks"][instruction[1]].pop())
  return stack_and_instructions

def execute_instructions_9001(stacks_and_instructions):
  for instruction in stacks_and_instructions["instructions"]:
    crates_to_move = []
    for i in range(0,instruction[0]):
      crates_to_move.insert(0, stacks_and_instructions["stacks"][instruction[1]].pop())
    stacks_and_instructions["stacks"][instruction[2]].extend(crates_to_move)
  return stacks_and_instructions

  
def solve_part_one(puzzle_input):
  stacks_and_instructions = process_input(puzzle_input)
  stacks_and_instructions = execute_instructions(stacks_and_instructions)
  final_arrangement = ""
  for stack in stacks_and_instructions["stacks"]:
    final_arrangement += stacks_and_instructions["stacks"][stack][-1]
  return final_arrangement

def solve_part_two(puzzle_input):
  stacks_and_instructions = process_input(puzzle_input)
  stacks_and_instructions = execute_instructions_9001(stacks_and_instructions)
  final_arrangement = ""
  for stack in stacks_and_instructions["stacks"]:
    final_arrangement += stacks_and_instructions["stacks"][stack][-1]
  return final_arrangement

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday05.txt") as f:
    puzzle_input = f.read().rstrip()
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
