import sys

def get_coords_after_instruction(starting_coord, instruction):
  x, y = starting_coord
  if instruction.get('r', 0):
    x += instruction['r']
  if instruction.get('d', 0):
    y += instruction['d']
  return [x, y]

def refresh_map(hill_map, final_coord, pattern_size=12):
  if len(hill_map[final_coord[1]]) <= final_coord[0]:
    hill_map[final_coord[1]] = hill_map[final_coord[1]][:pattern_size]*(final_coord[0]//pattern_size + 1)

def is_coord_at_tree(hill_map, current_coord):
  x, y = current_coord
  return hill_map[y][x] == "#"

def count_number_of_trees_on_run(hill_map, repeating_instruction, starting_coord=[0,0], pattern_size=12):
  current_coord = starting_coord
  tree_count = 0
  if is_coord_at_tree(hill_map, current_coord):
    tree_count = 1

  while True:
    current_coord = get_coords_after_instruction(current_coord, repeating_instruction)
    if current_coord[1]>=len(hill_map):
      print('Reached end')
      break
    refresh_map(hill_map, current_coord, pattern_size=pattern_size)
    if is_coord_at_tree(hill_map, current_coord):
      tree_count += 1
  return tree_count
    

if __name__ == "__main__":
  args = sys.argv
  with open('python/inputday03.txt') as f:
    hill_map = [x.strip() for x in f.readlines() if x.strip() != ""]

  if args[1] == "1":
    pattern_size = len(hill_map[0])
    repeating_instruction = {
      'r': 3,
      'd': 1
    }
    tree_count = count_number_of_trees_on_run(hill_map, repeating_instruction, pattern_size=pattern_size)
    print(tree_count)
  if args[1] == "2":
    pass
