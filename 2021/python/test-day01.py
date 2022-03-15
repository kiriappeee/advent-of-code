import unittest
from . import day01

class TestDay1(unittest.TestCase):
    def test_measurement_increase_count_can_be_found(self):
        test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        answer = day01.count_measurement_increase(test_list)
        self.assertEqual(answer, 7)

    def test_window_sums_can_be_retrieved(self):
        test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        answer = day01.break_into_window_sums(test_list)
        self.assertEqual(answer[0], 607)
        self.assertEqual(answer[1], 618)
        self.assertEqual(answer[4], 647)
        self.assertEqual(answer[-1], 792)

    def test_measurement_window_increment_count_can_be_found(self):
        test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        answer = day01.count_measurement_increase_by_windows(test_list)
        self.assertEqual(answer, 5)
  
if __name__ == "__main__":
    unittest.main()

