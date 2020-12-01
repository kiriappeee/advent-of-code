import unittest
from . import day01

class TestDay1(unittest.TestCase):
  def test_basic(self):
    self.assertEqual('hello', 'hello')
  def test_can_find_two_integers_that_add_up_to_2020(self):
    test_list = [1721,979,366,299,675,1456]
    answer = day01.find_numbers_that_sum_up_to_expected(numbers=test_list, expected_sum=2020)
    self.assertEqual(sum(answer), 2020)
    
if __name__ == "__main__":
  unittest.main()