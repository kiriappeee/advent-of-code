import unittest
from . import day9

class TestDay9(unittest.TestCase):
    def setUp(self):
        day9.distances = {}
        instructionSet = [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141"]
        for instruction in instructionSet:
            day9.addDistance(instruction)
    def tearDown(self):
        day9.distances = {}
    def test_distancesAreParsedAndStoredCorrectly(self):
        self.assertEqual(day9.distances, {"London": {"Dublin": 464, "Belfast": 518}, "Dublin": {"London": 464, "Belfast": 141}, "Belfast": {"London":518, "Dublin": 141}})
    def test_shortestPathCanBeFound(self):
        self.assertEqual(day9.getShortestPath(), ['London', 'Dublin', 'Belfast'])
    def test_givenPathDistanceCanBeFound(self):
        self.assertEqual(day9.getDistanceForPath(['London', 'Dublin', 'Belfast']), 605)
    def test_longestPathCanBeFound(self):
        #self.assertEqual(day9.getLongestPath(), ['Dublin', 'London', 'Belfast'])
        self.assertEqual(day9.getDistanceForPath(['Dublin', 'London', 'Belfast']), 982)


if __name__ == "__main__":
    unittest.main()
