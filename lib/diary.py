from lib.diary_entry import *

class Diary:
    def __init__(self):
        self.entries_list = []

    def add(self, entry):
        self.entries_list.append(entry)

    def all(self):
        return self.entries_list

    def count_words(self):
        word_count = 0
        for entry in self.entries_list:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        reading_time = 0
        for entry in self.entries_list:
            reading_time += entry.reading_time(wpm)
        return reading_time

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        best_entry = None
        min_reading_time = 9999999
        for entry in self.entries_list :
            entry_word_count = entry.count_words()
            entry_reading_time = entry_word_count / wpm
            

            if entry_reading_time <= minutes and minutes - entry_reading_time < min_reading_time :
                best_entry = entry
                min_reading_time = minutes - entry_reading_time
        return best_entry