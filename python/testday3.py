import unittest
from . import day3

class TestDay3(unittest.TestCase):
    def test_moveRecordsCorrectly(self):
        self.assertEqual(day3.move('>', 0,0), (0,1))

    def test_firstMoveDeliversToTwoHouses(self):
        self.assertEqual(day3.howManyHouses('>'), 2)

    def test_aMoveToUniquePlaceIsRecorded(self):
        self.assertEqual(day3.howManyHouses('>>'), 3)

    def test_aMoveToNonUniquePlaceIsNotRecorded(self):
        self.assertEqual(day3.howManyHouses('><>'), 2)
        self.assertEqual(day3.howManyHouses('>><>'), 3)

    def test_aSetOfMoves(self):
        self.assertEqual(day3.howManyHouses('><>vv^><>>'), 6)

    def test_roboSantaMovesWithSanth(self):
        self.assertEqual(day3.howManyHousesWithRoboSanta('>'), 2)
        self.assertEqual(day3.howManyHousesWithRoboSanta('^v'), 3)
        self.assertEqual(day3.howManyHousesWithRoboSanta('>>>'), 3)

if __name__ == "__main__":
    unittest.main()
