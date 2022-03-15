from multiprocessing import connection
import sys


def parse_input(input_to_parse):
    lines = [line.strip() for line in input_to_parse.split("\n")]
    numbers = lines[0].split(",")
    boards = []
    current_board = []
    for line in lines[2:]:
        if not line:
            boards.append(
                {
                    "board": current_board,
                    "filled_per_row": [0] * 5,
                    "filled_per_column": [0] * 5,
                    "called_values": [],
                }
            )
            current_board = []
        else:
            current_board.append([x.strip() for x in line.split(" ") if x.strip()])
    boards.append(
        {
            "board": current_board,
            "filled_per_row": [0] * 5,
            "filled_per_column": [0] * 5,
            "called_values": [],
        }
    )
    return numbers, boards


def mark_boards(boards_to_mark, value_to_search_for):
    for board_to_mark in boards_to_mark:
        row_check = 0
        for row in board_to_mark["board"]:
            if value_to_search_for in row and value_to_search_for not in board_to_mark["called_values"]:
                value_column = row.index(value_to_search_for)
                board_to_mark["filled_per_row"][row_check] += 1
                board_to_mark["filled_per_column"][value_column] += 1
                board_to_mark["called_values"].append(value_to_search_for)
                break
            row_check += 1
    return boards_to_mark

def get_bingo_boards(boards_to_check):
    boards_bingoed = []
    index_check = 0
    for board_to_check in boards_to_check:
        if 5 in board_to_check["filled_per_row"] or 5 in board_to_check["filled_per_column"]:
            boards_bingoed.append(index_check)
        index_check += 1
    return boards_bingoed

def find_winning_board_score(boards, calls):
    for call in calls:
        mark_boards(boards, call)
        bingo_boards = get_bingo_boards(boards)
        if bingo_boards:
            winning_board = boards[bingo_boards[0]]
            all_values = []
            for x in winning_board["board"]:
                all_values.extend(x)
            for called_value in winning_board["called_values"]:
                if called_value in all_values:
                    all_values.remove(called_value)
            all_values = [int(v) for v in all_values]
            return sum(all_values)*int(call)

def find_last_winning_board_score(boards, calls):
    bingo_boards_in_winning_order = []
    for call in calls:
        mark_boards(boards, call)
        bingo_boards = get_bingo_boards(boards)
        for bingo_board_index in bingo_boards:
            if bingo_board_index not in bingo_boards_in_winning_order:
                bingo_boards_in_winning_order.append(bingo_board_index)
        if len(bingo_boards_in_winning_order) == len(boards):
            winning_board = boards[bingo_boards_in_winning_order[-1]]
            all_values = []
            for x in winning_board["board"]:
                all_values.extend(x)
            for called_value in winning_board["called_values"]:
                if called_value in all_values:
                    all_values.remove(called_value)
            all_values = [int(v) for v in all_values]
            print(sum(all_values))
            print(int(call))
            return sum(all_values)*int(call)



if __name__ == "__main__":
    args = sys.argv
    with open('python/inputday04.txt', 'r') as f:
        puzzle_input = f.read()
    calls, boards = parse_input(puzzle_input)
    if args[1] == "1":
        print(find_winning_board_score(boards,calls))
    elif args[1] == "2":
        print(find_last_winning_board_score(boards, calls))