import sys


def get_position_after_instruction(instruction, position):
    position_x, position_y = position[0], position[1]
    print(instruction)
    direction = instruction.split(" ")[0]
    distance = int(instruction.split(" ")[1])
    if direction == "forward":
        position_x += distance
    elif direction == "down":
        position_y += distance
    elif direction == "up":
        position_y -= distance
    return [position_x, position_y]


def get_position_after_instruction_with_aim(instruction, position, aim):
    position_x, position_y = position[0], position[1]
    new_aim = aim
    print(instruction)
    direction = instruction.split(" ")[0]
    distance = int(instruction.split(" ")[1])
    if direction == "forward":
        position_x += distance
        position_y += distance * aim
    elif direction == "down":
        new_aim += distance
    elif direction == "up":
        new_aim -= distance
    return [position_x, position_y], new_aim


def get_final_position(instructions):
    current_position = [0, 0]
    for instruction in instructions:
        current_position = get_position_after_instruction(instruction, current_position)
    return current_position


def get_final_position_with_aim(instructions):
    current_position = [0, 0]
    current_aim = 0
    for instruction in instructions:
        current_position, current_aim = get_position_after_instruction_with_aim(
            instruction, current_position, current_aim
        )
    return current_position


if __name__ == "__main__":
    args = sys.argv
    with open("python/inputday02.txt") as f:
        puzzle_input = [x for x in f.readlines() if x.strip() != ""]

    if args[1] == "1":
        final_position = get_final_position(puzzle_input)
        print(final_position)
        print(final_position[0] * final_position[1])
    if args[1] == "2":
        final_position = get_final_position_with_aim(puzzle_input)
        print(final_position)
        print(final_position[0] * final_position[1])
