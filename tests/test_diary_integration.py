from lib.diary import *
from lib.diary_entry import *


"""
When we add two diary entries
List all entries
"""

def test_list_added_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents one")
    entry_2 = DiaryEntry("Title 2", "This is contents two")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
When we add two diary entries
Return number of words in all entries
"""

def test_count_words_returns_total_words_of_all_contents_entries():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents one")
    entry_2 = DiaryEntry("Title 2", "This is contents two")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 6

"""
When we add two diary entries
Return total reading time of all entries
"""    
def test_total_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents one")
    entry_2 = DiaryEntry("Title 2", "This is contents two")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3


"""
When we add two diary entries
return entry that best matches the time we have to read
"""

def test_return_entry_to_match_time_we_have_to_read():
    diary = Diary()
    entry_1 = DiaryEntry("Title 1", "Contents one")
    entry_2 = DiaryEntry("Title 2", "This is contents two")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(1, 2) == entry_1

"""
^^^^^^
var = we need to calculate how many words we can read
for loop - look at stored entries list and run count_words
    if entry word count == var return entry
    elif entry word count < var
    store entry and word count in dict
if dict == {} return None 
else sort dict
return highest
"""