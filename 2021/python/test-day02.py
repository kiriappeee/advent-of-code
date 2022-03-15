import unittest
from . import day02


class TestDay2(unittest.TestCase):
    def setUp(self):
        self.test_instructions = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2",
        ]

    def test_position_change_is_calculated(self):
        current_position = [0, 0]
        answer = day02.get_position_after_instruction(
            self.test_instructions[0], current_position
        )
        self.assertEqual(answer, [5, 0])
        answer = day02.get_position_after_instruction(self.test_instructions[1], [5, 0])
        self.assertEqual(answer, [5, 5])
        answer = day02.get_position_after_instruction(
            self.test_instructions[3], [13, 5]
        )
        self.assertEqual(answer, [13, 2])

    def test_final_position_is_calculated_correctly(self):
        answer = day02.get_final_position(self.test_instructions)
        self.assertEqual(answer, [15, 10])

    def test_position_and_aim_change_is_calculated(self):
        # test for step 1
        current_position = [0, 0]
        current_aim = 0
        new_position, new_aim = day02.get_position_after_instruction_with_aim(
            self.test_instructions[0], current_position, current_aim
        )
        self.assertEqual(new_position, [5, 0])
        self.assertEqual(new_aim, 0)
        # test for step 2
        current_position = [5, 0]
        current_aim = 0
        new_position, new_aim = day02.get_position_after_instruction_with_aim(
            self.test_instructions[1], current_position, current_aim
        )
        self.assertEqual(new_position, [5, 0])
        self.assertEqual(new_aim, 5)
        # test for step 3
        current_position = [5, 0]
        current_aim = 5
        new_position, new_aim = day02.get_position_after_instruction_with_aim(
            self.test_instructions[2], current_position, current_aim
        )
        self.assertEqual(new_position, [13, 40])
        self.assertEqual(new_aim, 5)
        # test for step 4
        current_position = [13, 40]
        current_aim = 5
        new_position, new_aim = day02.get_position_after_instruction_with_aim(
            self.test_instructions[3], current_position, current_aim
        )
        self.assertEqual(new_position, [13, 40])
        self.assertEqual(new_aim, 2)
        # test for step 6
        current_position = [13, 40]
        current_aim = 10
        new_position, new_aim = day02.get_position_after_instruction_with_aim(
            self.test_instructions[5], current_position, current_aim
        )
        self.assertEqual(new_position, [15, 60])
        self.assertEqual(new_aim, 10)


if __name__ == "__main__":
    unittest.main()
