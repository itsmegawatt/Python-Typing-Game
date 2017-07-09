import unittest
from typinggame import *

class Test_TypingGame(unittest.TestCase):

    def test_init(self):
        self.phrase = Phrase("This is a phrase.");
        self.assertIsNotNone(self.phrase);
