import time

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase

    def count_words(self):
        words = self.phrase.split(" ")
        self.number_of_words = len(words)

    def start_attempt(self, attempt = ""):
        if attempt == "":
            self.start_time()
            self.attempt = input()
            self.stop_time()
        else:
            self.attempt = attempt

    def start_time(self):
        self.start_time = time.time()

    def stop_time(self):
        self.total_time = time.time() - self.start_time

    def calculate_wpm(self):
        self.count_words()
        self.wpm = round(self.number_of_words * (60/self.total_time), 0)

    def get_passed(self):
        if self.attempt == self.phrase:
            print("You got it right!")
            return True
        else:
            print("You got it wrong...")
            return False

