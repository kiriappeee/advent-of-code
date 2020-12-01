import sys

def find_numbers_that_sum_up_to_expected(numbers=[], expected_sum=0):
  for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
      if(sum([numbers[i], numbers[j]])) == 2020:
        return [numbers[i], numbers[j]]

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday01.txt') as f:
    puzzle_input = [int(x) for x in f.readlines() if x.strip() != ""]
  if args[1] == "1":
    print(puzzle_input)
    output = find_numbers_that_sum_up_to_expected(numbers=puzzle_input, expected_sum=2020)
    print(output)
    print(output[0]*output[1])