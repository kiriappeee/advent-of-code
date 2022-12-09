import sys

def convert_commands_to_directory(commands):
  command_index = 0
  count = 0
  currentDir = ""
  allProcessed = False
  dir_structure = {"/": {"size": 0, "parent": None, "files": {}}}
  # dir_structure = {}
  while not allProcessed:
    # Get the index of the next command
    command_index = commands.index("$", command_index)
    # Get the command
    command = commands[command_index:commands.index("\n", command_index)].strip().replace("$ ", "")
    if command.startswith("cd "):
      dirToChangeTo = command.replace("cd ", "")
      if dirToChangeTo == "..":
        currentDir = dir_structure[currentDir]["parent"]
      else:
        if dirToChangeTo == "/":
          currentDir = "/"
        else:
          # ensure the directory is the full path
          currentDir = f"{currentDir}/{dirToChangeTo}".replace("//","/")
      command_index += 3
    elif command.startswith("ls"):
      try:
        directory_details = commands[command_index+5:commands.index("$", command_index+5)].strip().split("\n")
      except ValueError:
        directory_details = commands[command_index+5:].strip().split("\n")
        allProcessed = True
      for directory_item in directory_details:
        if directory_item.startswith("dir "):
          directory_name = directory_item[4:]
          dir_structure[currentDir]["files"][directory_name] = "dir"
          dir_structure[f"{currentDir}/{directory_name}".replace("//","/")] = {
            "size": 0,
            "parent": currentDir,
            "files": {}
          }
        else:
          file_size, file_name = directory_item.split(" ")
          dir_structure[currentDir]["files"][file_name] = int(file_size)
          dir_structure[currentDir]["size"] += int(file_size)
          parent_dir = dir_structure[currentDir]["parent"]
          while parent_dir:
            dir_structure[parent_dir]["size"] += int(file_size)
            parent_dir = dir_structure[parent_dir]["parent"]
      # print(dir_structure)
      command_index += 2


  while not allProcessed:
    count += 1
    command_index = commands.index("$", command_index)
    # print(command_index)
    command = commands[command_index:commands.index("\n", command_index)].strip()
    print(command)
    if command.startswith("$ cd"):
      dirToChangeTo = command.replace("$ cd ", "")
      if dirToChangeTo == "..":
        currentDir = dir_structure[currentDir]["parent"]
      else:
        currentDir = dirToChangeTo
        # print(currentDir)
      command_index += 3
    elif command.startswith("$ ls"):
      try:
        directory_details = commands[command_index+5:commands.index("$", command_index+5)].strip().split("\n")
      except ValueError:
        directory_details = commands[command_index+5:].strip().split("\n")
        allProcessed = True
      # print("Directory details")
      # print(directory_details)
      for directory_item in directory_details:
        if directory_item.startswith("dir "):
          directory_name = directory_item[4:]
          dir_structure[currentDir]["files"][directory_name] = "dir"
          dir_structure[f"{currentDir}{directory_name}"] = {
            "size": 0,
            "parent": currentDir,
            "files": {}
          }
        else:
          file_size, file_name = directory_item.split(" ")
          dir_structure[currentDir]["files"][file_name] = int(file_size)
          dir_structure[currentDir]["size"] += int(file_size)
          parent_dir = dir_structure[currentDir]["parent"]
          while parent_dir:
            dir_structure[parent_dir]["size"] += int(file_size)
            parent_dir = dir_structure[parent_dir]["parent"]
      command_index += 2
  return dir_structure
def solve_part_one(puzzle_input):
  dir_structure = convert_commands_to_directory(puzzle_input)
  sum_of_dirs_under_check_value = 0
  for directory in dir_structure.keys():
    if dir_structure[directory]["size"] <= 100000:
      sum_of_dirs_under_check_value += dir_structure[directory]["size"]
  return sum_of_dirs_under_check_value

def solve_part_two(puzzle_input):
  total_space_available=70000000
  required_free_space=30000000
  dir_structure = convert_commands_to_directory(puzzle_input)
  sorted_by_size = sorted(dir_structure.items(), key=lambda i:i[1]['size'])
  print(dir_structure["/"])
  total_used = dir_structure["/"]["size"]
  print(f"total used: {total_used}")
  actual_free_space = total_space_available - total_used
  minimum_dir_size=required_free_space - actual_free_space
  print(f"minimum dir size: {minimum_dir_size}")
  for item in sorted_by_size:
    # print(item)
    if item[1]["size"] >= minimum_dir_size:
      # print(item)
      return item[1]["size"]
  

if __name__ == "__main__":
  args = sys.argv
  with open("python/inputday07.txt") as f:
    puzzle_input = f.read()
  if len(args) < 2:
    print(solve_part_one(puzzle_input))
    print(solve_part_two(puzzle_input))
  elif args[1] == "1":
    print(solve_part_one(puzzle_input))
  elif args[1] == "2":
    print(solve_part_two(puzzle_input))
