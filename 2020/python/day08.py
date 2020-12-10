import sys

def execute_single_instruction(instruction_list, current_instruction_index, current_accumulator_value, visited):
  if current_instruction_index in visited:
    print(f"{current_instruction_index} was already visited")
    return [-1, current_accumulator_value]
  visited.append(current_instruction_index)
  current_instruction = instruction_list[current_instruction_index]
  operation = current_instruction.split(' ')[0]
  argument = int(current_instruction.split(' ')[1])
  if operation == 'nop':
    return [current_instruction_index+1, current_accumulator_value]
  elif operation == 'acc':
    return [current_instruction_index+1, current_accumulator_value+argument]
  elif operation == 'jmp':
    return [current_instruction_index+argument, current_accumulator_value]

def escape_infinite_loop(instruction_set, attempted_changes):
  old_instruction_set = instruction_set.copy()
  accumulator_value = 0
  current_instruction = 0
  visited = []
  change_attempted = False
  while current_instruction != -1 and current_instruction < len(instruction_set):

    if 'jmp' in instruction_set[current_instruction] and current_instruction not in attempted_changes and not change_attempted:
      print(instruction_set[current_instruction])
      print(f'Attempting to change {current_instruction}')
      attempted_changes.append(current_instruction)
      change_attempted = True
      instruction_set[current_instruction] = instruction_set[current_instruction].replace('jmp', 'nop')
      print(instruction_set[current_instruction])

    elif 'nop' in instruction_set[current_instruction] and current_instruction not in attempted_changes and not change_attempted:
      print(instruction_set[current_instruction])
      print(f'Attempting to change {current_instruction}')
      change_attempted = True
      attempted_changes.append(current_instruction)
      instruction_set[current_instruction] = instruction_set[current_instruction].replace('nop', 'jmp')
      print(instruction_set[current_instruction])

    current_instruction, accumulator_value = execute_single_instruction(instruction_set, current_instruction, accumulator_value, visited)

  if current_instruction == -1:
    print(f'Change failed. Trying again.')
    print(attempted_changes)
    return escape_infinite_loop(old_instruction_set, attempted_changes)
  else:
    return accumulator_value


if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday08.txt') as f:
    instruction_set = [x.strip() for x in f.readlines() if x.strip() != ""]
  if args[1] == "1":
    accumulator_value = 0
    current_instruction = 0
    visited = []
    while current_instruction != -1:
      current_instruction, accumulator_value = execute_single_instruction(instruction_set, current_instruction, accumulator_value, visited)
    print(accumulator_value)
  if args[1] == "2":
    print(escape_infinite_loop(instruction_set, []))
