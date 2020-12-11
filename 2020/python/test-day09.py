import unittest
from . import day09

class TestDay09(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.test_input = [int(x.strip()) for x in """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")]

  def test_invalid_number_can_be_found(self):
    self.assertEqual(day09.find_invalid_number(self.test_input, preamble=5), [127,14])

  def test_encryption_weakness_can_be_found(self):
    self.assertEqual(day09.find_encryption_weakness(self.test_input, preamble=5), 62)
if __name__ == "__main__":
  unittest.main()
