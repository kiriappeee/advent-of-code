def get_checksum(spreadsheet):
    checksum = 0
    for line in spreadsheet:
        checksum += max(line) - min(line)
    return checksum

def find_evenly_divisible_values(spreadsheet_row):
    sorted_row = spreadsheet_row.copy()
    sorted_row.sort()
    max_value_index = len(sorted_row) - 1
    while max_value_index>0:
        min_value_index = 0
        while min_value_index < max_value_index:
            if sorted_row[max_value_index] % sorted_row[min_value_index] == 0:
                return (sorted_row[max_value_index], sorted_row[min_value_index])
            min_value_index += 1
        max_value_index -= 1

def get_checksum_using_evenly_divisible_values(spreadsheet):
    checksum = 0
    for spreadsheet_row in spreadsheet:
        evenly_divisble_values = find_evenly_divisible_values(spreadsheet_row)
        checksum += evenly_divisble_values[0] // evenly_divisble_values[1]
    return checksum


def solve_challenge_part_1():
    print(get_checksum(get_puzzle_input()))

def solve_challenge_part_2():
    print(get_checksum_using_evenly_divisible_values(get_puzzle_input()))

def get_puzzle_input():
    puzzle_input_file = open('python/day2part1input.txt', 'r')
    puzzle_input = []
    for line in puzzle_input_file.read().strip().split('\n'):
        puzzle_input.append([int(number) for number in line.split(' ')  if number != '' ])
    puzzle_input_file.close()
    return puzzle_input

if __name__ == "__main__":
    print("=== Part 1 ===")
    solve_challenge_part_1()
    print("=== Part 2 ===")
    solve_challenge_part_2()
