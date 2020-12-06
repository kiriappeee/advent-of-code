import sys

if __name__ == "__main__":
  args = sys.argv
  answer_groups = []
  with open('python/inputday06.txt') as f:
    puzzle_input = [x.strip() for x in f.readlines()]
    current_group = ''
    for l in puzzle_input:
      current_group += l
      if l == '':
        answer_groups.append(current_group)
        current_group = ''
    if current_group != '':
      answer_groups.append(current_group)
  if args[1] == "1":
    total_yes_count = 0
    for answer_group in answer_groups:
      print(set(answer_group))
      total_yes_count += len(set(answer_group))
    print(total_yes_count)
  if args[1] == "2":
    pass
