import sys

def find_two_numbers_that_sum_up_to_expected(numbers=[], expected_sum=0):
  for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
      if(sum([numbers[i], numbers[j]])) == 2020:
        return [numbers[i], numbers[j]]

def find_three_numbers_that_sum_up_to_expected(numbers=[], expected_sum=0):
  for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
      for k in range(j+1, len(numbers)):
        if(sum([numbers[i], numbers[j], numbers[k]])) == 2020:
          return [numbers[i], numbers[j], numbers[k]]

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday01.txt') as f:
    puzzle_input = sorted([int(x) for x in f.readlines() if x.strip() != ""])

  if args[1] == "1":
    output = find_two_numbers_that_sum_up_to_expected(numbers=puzzle_input, expected_sum=2020)
    print(output)
    print(output[0]*output[1])
  if args[1] == "2":
    output = find_three_numbers_that_sum_up_to_expected(numbers=puzzle_input, expected_sum=2020)
    print(output)
    print(output[0]*output[1]*output[2])