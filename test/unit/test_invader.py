import unittest
from invader import Invader


class TestInvader(unittest.TestCase):

    def test_invader_is_valid(self):
        invader = Invader(['abc', 'cbd', 'def'])
        self.assertTrue(invader.is_valid())

    def test_invader_is_invalid(self):
        invader = Invader(['abc', 'cd', 'def'])
        self.assertFalse(invader.is_valid())


if __name__ == '__main__':
    unittest.main()
