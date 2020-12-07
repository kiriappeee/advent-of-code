import sys

def get_colour_map(colour_input):
  colour_map = {}
  for l in colour_input:
    primary_colour, contained_colour_string = [x.strip() for x in l.replace('.','').split('bags contain')]
    colour_map[primary_colour] = {}
    if 'no other bag' in contained_colour_string:
      continue
    contained_colours = [c.replace(' bags', '').replace(' bag', '').strip() for c in contained_colour_string.split(',')]
    for c in contained_colours:
      number_of_bags = int(c.split(' ')[0].strip())
      secondary_colour = ' '.join(c.split(' ')[1:]).strip()
      colour_map[primary_colour][secondary_colour] = number_of_bags
  return colour_map

def get_bags_that_eventually_contain_given_colour(given_colour, colour_map):
  present_list = []
  for primary_colour in colour_map.keys():
    # print(f"Checking {primary_colour}")
    if find_bags_that_contain_given_colour(given_colour, primary_colour, present_list, colour_map) and primary_colour not in present_list:
      present_list.append(primary_colour)
    # print(present_list)
  # print(present_list)
  return len(present_list)

def find_bags_that_contain_given_colour(given_colour, current_colour_to_check, present_list, colour_map):
  if current_colour_to_check in present_list:
    return True
  secondary_colours = colour_map[current_colour_to_check]
  colour_found = False
  for sc in secondary_colours.keys():
    # print(f'Checking secondary colour {sc}')
    if sc in present_list:
      # print(f'Colour {sc} already present')
      colour_found = True
      continue
    if sc == given_colour:
      colour_found = True
      continue
    if find_bags_that_contain_given_colour(given_colour, sc, present_list, colour_map):
      present_list.append(sc)
      colour_found = True
      continue
  return colour_found


def get_number_of_bags_required(starting_colour, colour_map):
  total = 1
  if colour_map[starting_colour].keys():
    for next_start_colour in colour_map[starting_colour].keys():
      totalToAdd = colour_map[starting_colour][next_start_colour] * get_number_of_bags_required(next_start_colour, colour_map)
      total += totalToAdd
      print(f"{starting_colour} contains {colour_map[starting_colour][next_start_colour]} {next_start_colour} bags which contains {totalToAdd} bags")
  else:
    total = 1
  print(f"{starting_colour} contains a total of {total} bags")
  return total


if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday07.txt') as f:
    puzzle_input = [x.strip() for x in f.readlines() if x.strip() != ""]
  colour_map = get_colour_map(puzzle_input)
  if args[1] == "1":
    print(get_bags_that_eventually_contain_given_colour("shiny gold", colour_map))
  if args[1] == "2":
    print(get_number_of_bags_required("shiny gold", colour_map) - 1)
