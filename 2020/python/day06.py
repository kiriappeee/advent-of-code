import sys
from collections import Counter

if __name__ == "__main__":
  args = sys.argv
  answer_groups = []
  with open('python/inputday06.txt') as f:
    puzzle_input = [x.strip() for x in f.readlines()]
    current_group = []
    for l in puzzle_input:
      if l == '':
        answer_groups.append(current_group)
        current_group = []
      else:
        current_group.append(l)
    if current_group != []:
      answer_groups.append(current_group)
  if args[1] == "1":
    total_yes_count = 0
    for answer_group in answer_groups:
      print(set(''.join(answer_group)))
      total_yes_count += len(set(''.join(answer_group)))
    print(total_yes_count)
  if args[1] == "2":
    total_yes_count = 0
    for answer_group in answer_groups:
      c = Counter(''.join(answer_group))
      for i in c:
        if c[i] == len(answer_group):
          total_yes_count += 1
    print(total_yes_count)
