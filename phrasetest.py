from unittest.mock import patch
import unittest
from phrase import Phrase

class Test_TypingGame(unittest.TestCase):

    def test_init(self):
        sentence1 = "This is a phrase."
        self.phrase = Phrase(sentence1)
        self.assertIsNotNone(self.phrase)
        self.assertEquals(self.phrase.phrase, sentence1)

    # Get input will return 'This is a test sentence' during this test
    def test_attempt_1(self):
        phrase = Phrase("This is a test sentence")
        phrase.getattempt()

