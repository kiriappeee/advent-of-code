import unittest
from . import day03


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.test_input = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010",
        ]

    def test_gamma_and_epilson_rate_for_given_position(self):
        gamma_answer, epilson_answer = day03.get_gamma_and_epilson_rate_for_pos(
            self.test_input, 0
        )
        self.assertEqual(gamma_answer, 1)
        self.assertEqual(epilson_answer, 0)
        gamma_answer, epilson_answer = day03.get_gamma_and_epilson_rate_for_pos(
            self.test_input, 1
        )
        self.assertEqual(gamma_answer, 0)
        self.assertEqual(epilson_answer, 1)

    def test_final_power_value_can_be_calculated(self):
        power_answer = day03.get_power_value_from_diagnostics(self.test_input)
        self.assertEqual(power_answer, 198)

    def test_ratings_for_o2_returned_for_given_position(self):
        o2_rating_list = day03.get_o2_rating_list_for_pos(self.test_input, 0)
        self.assertEqual(
            o2_rating_list,
            ["11110", "10110", "10111", "10101", "11100", "10000", "11001"],
        )
        o2_rating_list = day03.get_o2_rating_list_for_pos(o2_rating_list, 1)
        self.assertEqual(o2_rating_list, ["10110", "10111", "10101", "10000"])
        o2_rating_list = ["10110", "10111"]
        o2_rating_list = day03.get_o2_rating_list_for_pos(o2_rating_list, 4)
        self.assertEqual(o2_rating_list, ["10111"])

    def test_ratings_for_co2_returned_for_given_position(self):
        co2_rating_list = day03.get_co2_rating_list_for_pos(self.test_input, 0)
        self.assertEqual(co2_rating_list, ["00100", "01111", "00111", "00010", "01010"])
        co2_rating_list = day03.get_co2_rating_list_for_pos(co2_rating_list, 1)
        self.assertEqual(co2_rating_list, ["01111", "01010"])
        co2_rating_list = day03.get_co2_rating_list_for_pos(co2_rating_list, 2)
        self.assertEqual(co2_rating_list, ["01010"])

    def test_can_get_final_life_rating(self):
        self.assertEqual(day03.get_life_rating(self.test_input), 230)


if __name__ == "__main__":
    unittest.main()
