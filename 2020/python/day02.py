import sys
from collections import Counter

def break_input_into_rules(password_line_input):
  output = {}
  rules = password_line_input.split(':')[0]
  output['min_times'] = int(rules.split('-')[0])
  output['max_times'] = int(rules.split('-')[1].split(' ')[0])
  output['test_letter'] = rules.split('-')[1].split(' ')[1]
  output['password'] = password_line_input.split(':')[1].strip()
  return output

def break_input_into_new_rules(password_line_input):
  output = {}
  rules = password_line_input.split(':')[0]
  output['first_position'] = int(rules.split('-')[0]) - 1
  output['second_position'] = int(rules.split('-')[1].split(' ')[0]) - 1
  output['test_letter'] = rules.split('-')[1].split(' ')[1]
  output['password'] = password_line_input.split(':')[1].strip()
  return output

def validate_password(password_with_rules):
  c = Counter(password_with_rules['password'])
  return c[password_with_rules['test_letter']] >= password_with_rules['min_times'] and c[password_with_rules['test_letter']] <= password_with_rules['max_times']

def validate_password_with_new_rules(password_with_rules):
  return password_with_rules['password'][password_with_rules['first_position']] == password_with_rules['test_letter'] and password_with_rules['password'][password_with_rules['second_position']] != password_with_rules['test_letter'] or password_with_rules['password'][password_with_rules['first_position']] != password_with_rules['test_letter'] and password_with_rules['password'][password_with_rules['second_position']] == password_with_rules['test_letter']

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday02.txt') as f:
    puzzle_input = [x for x in f.readlines() if x.strip() != ""]

  if args[1] == "1":
    counter = 0
    for pi in puzzle_input:
      rule_set = break_input_into_rules(pi)
      if validate_password(rule_set):
        counter+=1
    print(counter)
  if args[1] == "2":
    counter = 0
    for pi in puzzle_input:
      rule_set = break_input_into_new_rules(pi)
      if validate_password_with_new_rules(rule_set):
        counter+=1
    print(counter)
