import unittest
from . import day6

class TestDay6PartOne(unittest.TestCase):
    def test_basicGridIsCreated(self):
        expectedArray = [
                [0,0],
                [0,0]
                ]
        self.assertEqual(day6.createBaseGrid(2,2), expectedArray)
        expectedArrayB = [
                [0,0],
                [0,0],
                [0,0],
                ]
        self.assertEqual(day6.createBaseGrid(2,3), expectedArrayB)

    def test_instructionCanBeParsed(self):
        expectedResultA = ("turn on", (0,0), (2,2))
        expectedResultB = ("turn off", (0,0), (2,2))
        expectedResultC = ("toggle", (0,0), (2,2))
        self.assertEqual(day6.parseInstruction("turn on 0,0 through 2,2"), expectedResultA)
        self.assertEqual(day6.parseInstruction("turn off 0,0 through 2,2"), expectedResultB)
        self.assertEqual(day6.parseInstruction("toggle 0,0 through 2,2"), expectedResultC)

    def test_specifiedLightsCanBeTurnedOn(self):
        grid = day6.createBaseGrid(4,4)
        expectedResult = [
                [1,1,1,0],
                [1,1,1,0],
                [1,1,1,0],
                [0,0,0,0],
                ]
        self.assertEqual(day6.executeInstruction("turn on 0,0 through 2,2", grid), expectedResult)
        self.assertNotEqual(grid, expectedResult)

    def test_countSwitchedOnLights(self):
        grid = day6.createBaseGrid(4,4)
        expectedResult = [
                [1,1,1,0],
                [1,1,1,0],
                [1,1,1,0],
                [0,0,0,0],
                ]
        grid = day6.executeInstruction("turn on 0,0 through 2,2", grid)
        self.assertEqual(day6.countSwitchedOnLights(grid), 9)

if __name__ == "__main__":
    unittest.main()
