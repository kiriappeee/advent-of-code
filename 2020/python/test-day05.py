import unittest
from . import day05

class TestDay05(unittest.TestCase):
  def test_row_can_be_found_from_input(self):
    row_input = "FBFBBFF"
    self.assertEqual(day05.get_row(row_input), 44)
    row_input = "FBFBBFB"
    self.assertEqual(day05.get_row(row_input), 45)
    row_input = "BFFFBBF"
    self.assertEqual(day05.get_row(row_input), 70)
    row_input = "FFFBBBF"
    self.assertEqual(day05.get_row(row_input), 14)
    row_input = "BBFFBBF"
    self.assertEqual(day05.get_row(row_input), 102)
    

  def test_column_can_be_found_from_input(self):
    column_input = "RLR"
    self.assertEqual(day05.get_column(column_input), 5)
    column_input = "RLL"
    self.assertEqual(day05.get_column(column_input), 4)
    column_input = "RRR"
    self.assertEqual(day05.get_column(column_input), 7)
    
  def test_seat_id_can_be_found(self):
    seat_position = [44,5]
    self.assertEqual(day05.get_seat_id(seat_position), 357)
    seat_position = [14,7]
    self.assertEqual(day05.get_seat_id(seat_position), 119)
    seat_position = [102,4]
    self.assertEqual(day05.get_seat_id(seat_position), 820)
    seat_position = [70,7]
    self.assertEqual(day05.get_seat_id(seat_position), 567)
    

if __name__ == "__main__":
  unittest.main()
