import unittest
from . import day11

class TestDay11(unittest.TestCase):
    def test_passwordStringIsIncrementedCorrectly(self):
        self.assertEqual(day11.generateNextPassword('abcdefgg'), 'abcdefgh')
        self.assertEqual(day11.generateNextPassword('abcdefgz'), 'abcdefha')
        self.assertEqual(day11.generateNextPassword('abcdefzz'), 'abcdegaa')
    def test_validPasswordCannotContainIOL(self):
        self.assertFalse(day11.isPasswordValid('hijklmmn'))
    def test_passwordWithoutTwoDistrinctPairsIsInvalid(self):
        self.assertFalse(day11.isPasswordValid('abbcegjk'))
        self.assertFalse(day11.isPasswordValid('aabcbaak'))
        self.assertFalse(day11.isPasswordValid('abcegjkm'))
    def test_passwordMustIncludeIncreasingStraightOfCharactersOfAtleast3Letters(self):
        self.assertFalse(day11.isPasswordValid('abdffaam'))
    def test_validPasswords(self):
        self.assertTrue(day11.isPasswordValid('abcdffaa'))
        self.assertTrue(day11.isPasswordValid('ghjaabcc'))

    def test_iolCharactersAreSkipped(self):
        self.assertEqual(day11.generateNextPassword('ghijklmn'),'ghjaaaaa')
    def test_newPasswordIsGeneratedCorrectly(self):
        self.assertEqual(day11.generateNewPassword('abcdefgh'),'abcdffaa')
        self.assertEqual(day11.generateNewPassword('ghijklmn'),'ghjaabcc')


if __name__ == "__main__":
    unittest.main()
