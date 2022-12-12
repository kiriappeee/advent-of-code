import sys

def convert_input_to_grid(test_list):
  rows = [row.strip() for row in test_list.split("\n") if row.strip() != ""]
  row_grid = []
  column_grid = []
  row_count = 0
  for row_count in range(0, len(rows)):
    row_grid.append([])
    for column_count in range(0, len(rows[0])):
      row_grid[row_count].append(int(rows[row_count][column_count]))
  for column_count in range(0, len(rows[0])):
    column_grid.append([])
    for row_count in range(0, len(rows)):
      column_grid[column_count].append(int(rows[row_count][column_count]))
  return row_grid, column_grid

def solve_part_one(puzzle_input):
  row_grid, column_grid = convert_input_to_grid(puzzle_input)
  number_of_rows = len(row_grid)
  number_of_columns = len(column_grid)
  # visible_trees = number_of_rows*number_of_columns
  visible_trees = 0
  row_count = column_count = 1
  tallest_tree_dict = {}
  # for row_count in range(0,number_of_rows):
  #   tallest_tree_dict[f"rowLeft${row_count}"]=(0,0)
  #   tallest_tree_dict[f"rowRightt${row_count}"]=(0,0)
  #   for column_count in range(0, number_of_columns):
  #     tallest_tree_dict[f"columnTop${column_count}"]=(0,0)
  #     tallest_tree_dict[f"columnBottom${column_count}"]=(0,0)
  # find tallest tree in each row on left and right
  visible = None
  for row_count in range(0, number_of_rows):
    for column_count in range(0, number_of_columns):
      print(row_count, column_count, row_grid[row_count][column_count])
      visible = True
      #test left to right
      if column_count < number_of_columns-1:
        for column_check in range(column_count+1, number_of_columns):
          if row_grid[row_count][column_check] >= row_grid[row_count][column_count]:
            visible = False
            break
      else:
        visible = True
      if visible:
        print(visible)
        visible_trees += 1
        continue

      visible = True
      # test right to left
      if column_count > 0:
        for column_check in sorted(range(0, column_count), reverse=True):
          if row_grid[row_count][column_check] >= row_grid[row_count][column_count]:
            visible = False
            break
      else:
        visible = True
      
      if visible:
        print(visible)
        visible_trees += 1
        continue

      visible = True
      # test up to down
      if row_count < number_of_rows-1:
        for row_check in range(row_count+1, number_of_rows):
          if row_grid[row_check][column_count] >= row_grid[row_count][column_count]:
            visible = False
            break
      else:
        visible = True

      if visible:
        print(visible)
        visible_trees += 1
        continue

      visible = True
      # test down to up
      if row_count > 0:
        for row_check in sorted(range(0, row_count), reverse=True):
          if row_grid[row_check][column_count] >= row_grid[row_count][column_count]:
            visible = False
            break
      else:
        visible = True

      if visible:
        print(visible)
        visible_trees += 1
        continue
    
  return visible_trees


  
      

def solve_part_two(puzzle_input):
  pass

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday08.txt") as f:
    puzzle_input = f.read()
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
