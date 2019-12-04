import unittest
from . import day03

class TestDay3(unittest.TestCase):
    def test_spiral_corner_coordinates_can_be_calculated_for_given_ring(self):
        expected_result = {
            'starting_position': (1,0),
            'top_right': (1,1),
            'top_left': (-1,1),
            'bottom_left': (-1,-1),
            'bottom_right': (1,-1)
        }
        self.assertEqual(day03.get_spiral_corners_for_given_ring(ring_counter=1), expected_result)
        expected_result = {
            'starting_position': (3,-2),
            'top_right': (3,3),
            'top_left': (-3,3),
            'bottom_left': (-3,-3),
            'bottom_right': (3,-3)
        }
        self.assertEqual(day03.get_spiral_corners_for_given_ring(ring_counter=3), expected_result)

    def test_coordinates_can_be_calculated_for_one(self):
        self.assertEqual(day03.getCoordinatesForNumber(1), (0,0))
    def test_coordinates_can_be_calculated_for_any_number(self):
        self.assertEqual(day03.getCoordinatesForNumber(2), (1,0))
        self.assertEqual(day03.getCoordinatesForNumber(3), (1,1))
        self.assertEqual(day03.getCoordinatesForNumber(4), (0,1))
        self.assertEqual(day03.getCoordinatesForNumber(5), (-1,1))
        self.assertEqual(day03.getCoordinatesForNumber(6), (-1,0))
        self.assertEqual(day03.getCoordinatesForNumber(7), (-1,-1))
        self.assertEqual(day03.getCoordinatesForNumber(8), (0,-1))
        self.assertEqual(day03.getCoordinatesForNumber(9), (1,-1))
        self.assertEqual(day03.getCoordinatesForNumber(10), (2,-1))
        self.assertEqual(day03.getCoordinatesForNumber(11), (2,0))
        self.assertEqual(day03.getCoordinatesForNumber(23), (0,-2))

    def test_manhattan_distance_calculated_correctly_for_a_given_number(self):
        self.assertEqual(day03.get_manhattan_distance_for_given_number(1), 0)
        self.assertEqual(day03.get_manhattan_distance_for_given_number(12), 3)
        self.assertEqual(day03.get_manhattan_distance_for_given_number(23), 2)
        self.assertEqual(day03.get_manhattan_distance_for_given_number(1024), 31)

    # part two
    def test_can_obtain_adjacent_square_coordinates(self):
        # current_coordinate = (0,0)
        # ring_number = 0
        current_coordinate = (1,0)
        expected_result = [
            (0,0),
            (0,1),
            (1,1),
            (2,1),
            (2,0),
            (2,-1),
            (1,-1),
            (0,-1)
        ]
        self.assertEqual(day03.get_adjacent_square_coordinates(current_coordinate), expected_result)
    def test_can_generate_ring_correctly_given_a_number_of_steps(self):
        expected_result = {
            (0,0): 1,
            (1,0): 1,
            (1,1): 2,
            (0,1): 4,
            (-1,1): 5,
            (-1,0): 10,
        }
        generated_ring, current_coordinates = day03.generate_ring(count = 6)
        self.assertEqual(generated_ring, expected_result)

    def test_can_generate_ring_correctly_given_check_number(self):
        expected_result = (-1,1)
        generated_ring, current_coordinates = day03.generate_ring(number_check=4)
        self.assertEqual(current_coordinates, expected_result)
        expected_result = (0, -2)
        generated_ring, current_coordinates = day03.generate_ring(number_check=748)
        self.assertEqual(current_coordinates, expected_result)
if __name__ == "__main__":
    unittest.main()