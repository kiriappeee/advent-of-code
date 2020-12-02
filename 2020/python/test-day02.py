import unittest
from . import day02

class TestDay1(unittest.TestCase):
  def test_input_can_be_broken_correctly(self):
    test_input = '1-3 a: abcde'
    output = day02.break_input_into_rules(test_input)
    expected_output = {
      'min_times': 1,
      'max_times': 3,
      'test_letter': 'a',
      'password': 'abcde'
    }
    self.assertEqual(output, expected_output)
  def test_password_can_be_validated(self):
    test_rule = {
      'min_times': 1,
      'max_times': 3,
      'test_letter': 'a',
      'password': 'abcde'
    }
    self.assertTrue(day02.validate_password(test_rule))
    test_rule = {
      'min_times': 1,
      'max_times': 3,
      'test_letter': 'b',
      'password': 'cdefg'
    }
    self.assertFalse(day02.validate_password(test_rule))
    test_rule = {
      'min_times': 2,
      'max_times': 9,
      'test_letter': 'c',
      'password': 'ccccccccc'
    }
    self.assertTrue(day02.validate_password(test_rule))
  
if __name__ == "__main__":
  unittest.main()