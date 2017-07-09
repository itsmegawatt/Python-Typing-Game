# Have to come up with a way to count the number of words from the attempt
# Have to also come up with a way to calculate WPM based on whether or not the attempt == phrase
# Have to come up with a way to get number of correct words from attempt compared to the phrase


from phrase import Phrase

test = Phrase("Try this out")
test.start_attempt()
test.calculate_wpm()
print(test.wpm)