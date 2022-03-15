import unittest
from . import day04


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.numbers_to_call_out = [
            "7",
            "4",
            "9",
            "5",
            "11",
            "17",
            "23",
            "2",
            "0",
            "14",
            "21",
            "24",
            "10",
            "16",
            "13",
            "6",
            "15",
            "25",
            "12",
            "22",
            "18",
            "20",
            "8",
            "19",
            "3",
            "26",
            "1",
        ]
        self.boards = [
            {
                "board": [
                    ["22", "13", "17", "11", "0"],
                    ["8", "2", "23", "4", "24"],
                    ["21", "9", "14", "16", "7"],
                    ["6", "10", "3", "18", "5"],
                    ["1", "12", "20", "15", "19"],
                ],
                "filled_per_row": [0, 0, 0, 0, 0],
                "filled_per_column": [0, 0, 0, 0, 0],
                "called_values": []
            },
            {
                "board": [
                    ["3", "15", "0", "2", "22"],
                    ["9", "18", "13", "17", "5"],
                    ["19", "8", "7", "25", "23"],
                    ["20", "11", "10", "24", "4"],
                    ["14", "21", "16", "12", "6"],
                ],
                "filled_per_row": [0, 0, 0, 0, 0],
                "filled_per_column": [0, 0, 0, 0, 0],
                "called_values": []
            },
            {
                "board": [
                    ["14", "21", "17", "24", "4"],
                    ["10", "16", "15", "9", "19"],
                    ["18", "8", "23", "26", "20"],
                    ["22", "11", "13", "6", "5"],
                    ["2", "0", "12", "3", "7"],
                ],
                "filled_per_row": [0, 0, 0, 0, 0],
                "filled_per_column": [0, 0, 0, 0, 0],
                "called_values": []
            },
        ]

        self.unparsed_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    def test_input_can_be_parsed(self):
        numbers, boards = day04.parse_input(self.unparsed_input)
        self.assertEqual(numbers, self.numbers_to_call_out)
        self.assertEqual(boards, self.boards)

    def test_bingo_board_marked_correctly_on_call(self):
        day04.mark_boards(self.boards, "7")
        day04.mark_boards(self.boards, "7")
        self.assertEqual(self.boards[0]["filled_per_row"], [0,0,1,0,0])
        self.assertEqual(self.boards[0]["filled_per_column"], [0,0,0,0,1])
        self.assertEqual(self.boards[0]["called_values"], ["7"])
        self.assertEqual(self.boards[1]["filled_per_row"], [0,0,1,0,0])
        self.assertEqual(self.boards[1]["filled_per_column"], [0,0,1,0,0])
        self.assertEqual(self.boards[1]["called_values"], ["7"])
        self.assertEqual(self.boards[2]["filled_per_row"], [0,0,0,0,1])
        self.assertEqual(self.boards[2]["filled_per_column"], [0,0,0,0,1])
        self.assertEqual(self.boards[2]["called_values"], ["7"])

    def test_bingo_is_found(self):
        self.boards[1]["filled_per_row"]=[0,4, 3,1,0]
        self.boards[1]["filled_per_column"]=[0,2, 1,3,1]
        self.boards[1]["called_values"] = ["9", "13", "17", "5"]
        self.assertEqual(day04.get_bingo_boards(self.boards), [])
        day04.mark_boards(self.boards, "18")
        self.assertEqual(day04.get_bingo_boards(self.boards), [1])
        self.setUp()
        for call in self.numbers_to_call_out:
            day04.mark_boards(self.boards, call)
            if call == "24":
                break
        self.assertEqual(day04.get_bingo_boards(self.boards), [2])

    def test_winning_board_score_is_found(self):
        self.assertEqual(day04.find_winning_board_score(self.boards, self.numbers_to_call_out), 4512)

    def test_last_winning_board_score_is_found(self):
        self.assertEqual(day04.find_last_winning_board_score(self.boards, self.numbers_to_call_out), 1924)


if __name__ == "__main__":
    unittest.main()
