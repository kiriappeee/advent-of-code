import sys

def find_invalid_number(list_of_numbers, preamble=25):
  current_index = preamble
  for number_to_check in list_of_numbers[preamble:]:
    print(f'Checking {number_to_check}')
    is_valid = False
    list_of_numbers_to_check = list_of_numbers[current_index-25:current_index]
    for number_to_match in list_of_numbers_to_check:
      if number_to_match == number_to_check or number_to_check - number_to_match in list_of_numbers_to_check:
        is_valid = True
        break
    if is_valid:
      current_index += 1
      continue
    else:
      return [number_to_check, current_index]
  return []

def find_encryption_weakness(list_of_numbers, preamble=25):
  invalid_number_to_use, index_of_invalid_number = find_invalid_number(list_of_numbers, preamble=preamble)
  starting_index = 0
  ending_index = 0
  for i in range(0, len(list_of_numbers)):
    checking_sum = 0
    starting_index = i
    found_valid_range = False
    for j in range(i, len(list_of_numbers)):
      checking_sum += list_of_numbers[j]
      if checking_sum == invalid_number_to_use:
        found_valid_range = True
        ending_index = j
        break
      elif checking_sum > invalid_number_to_use:
        break
    if found_valid_range:
      print(starting_index, ending_index)
      valid_range = list_of_numbers[starting_index:ending_index+1]
      return sum([min(valid_range), max(valid_range)])

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday09.txt') as f:
    puzzle_input = [int(x.strip()) for x in f.readlines() if x.strip() != ""]

  if args[1] == "1":
    print(find_invalid_number(puzzle_input, preamble=25))
  if args[1] == "2":
    print(find_encryption_weakness(puzzle_input, preamble=25))
