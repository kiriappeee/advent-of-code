import unittest
from . import day02

class TestDay2Part1Solution(unittest.TestCase):
    def test_solution_returns_correct_checksum(self):
        array_to_test = [[5, 1, 9, 5],
                        [7, 5, 3],
                        [2, 4, 6, 8]]
        self.assertEqual(day02.get_checksum(array_to_test), 18)

class TestDay2Part2Solution(unittest.TestCase):
    def test_evenly_divisible_values_can_be_found(self):
        self.assertEqual(day02.find_evenly_divisible_values([5,9,2,8]), (8, 2))
        self.assertEqual(day02.find_evenly_divisible_values([9,4,7,3]), (9, 3))
        self.assertEqual(day02.find_evenly_divisible_values([3,8,6,5]), (6, 3))

    def test_final_sum_of_values_is_calculated_correctly(self):
        array_to_test = [[5,9,2,8],
                        [9,4,7,3],
                        [3,8,6,5]]
        self.assertEqual(day02.get_checksum_using_evenly_divisible_values(array_to_test), 9)
        

if __name__ == "__main__":
    unittest.main()