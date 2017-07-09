import time
import unittest
from phrase import Phrase

class Test_TypingGame(unittest.TestCase):

    def test_init(self):
        sentence1 = "This is a phrase."
        self.phrase = Phrase(sentence1)
        self.assertIsNotNone(self.phrase)
        self.assertEquals(self.phrase.phrase, sentence1)

    def test_attempt(self):
        phrase = Phrase("This is a test sentence")
        phrase.attempt("This is a test sentence")

    def test_time(self):
        phrase = Phrase("This is a test sentence")
        now = time.time()
        phrase.start_time()
        self.assertAlmostEqual(phrase.start_time, now, 20)
        total_time = time.time() - now
        phrase.stop_time()
        self.assertAlmostEqual(phrase.total_time, total_time, 20)

    def test_count_number_of_words(self):
        phrase1 = Phrase("This sentence has 5 words")
        phrase1.count_words()
        self.assertEquals(phrase1.number_of_words, 5)
        phrase2 = Phrase("This is a really long sentence that has a bit more words than 5 words, "
                         "in fact this sentence has around 30 words.")
        phrase2.count_words()
        self.assertEquals(phrase2.number_of_words, 23)

    def test_calculate_wpm(self):
        phrase = Phrase("This is yet another test sentence with just 10 words")
        phrase.total_time = 60
        phrase.calculate_wpm()
        self.assertEquals(phrase.wpm, 10)
        phrase2 = Phrase("This is yet another test sentence with just 10 words")
        phrase2.total_time = 120
        phrase2.calculate_wpm()
        self.assertEquals(phrase2.wpm, 5)
        phrase3 = Phrase("This is yet another test sentence with just 10 words")
        phrase3.total_time = 10
        phrase3.calculate_wpm()
        self.assertEquals(phrase3.wpm, 60)

    def test_passed(self):
        phrase = Phrase("This is a test sentence")
        phrase.start_attempt("This is a test sentence")
        phrase.get_passed()

