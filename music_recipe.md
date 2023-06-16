# . Describe the Problem
# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

# 2. Design the Class Interface
# Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.
<!-- Name: MusicList 
<!-- Init: Empty list-->
<!-- Add: To take 2 strings for artist and track, concatenate and append to list. Possibly call the list method to return it, otherwise no return needed  -->
<!-- List: To return the current list. 2 Exceptions - empty string and wrong data type -->


# # EXAMPLE

# class Reminder:
#     # User-facing properties:
#     #   name: string

#     def __init__(self, name):
#         # Parameters:
#         #   name: string
#         # Side effects:
#         #   Sets the name property of the self object
#         pass # No code here yet

#     def remind_me_to(self, task):
#         # Parameters:
#         #   task: string representing a single task
#         # Returns:
#         #   Nothing
#         # Side-effects
#         #   Saves the task to the self object
#         pass # No code here yet

#     def remind(self):
#         # Returns:
#         #   A string reminding the user to do the task
#         # Side-effects:
#         #   Throws an exception if no task is set
#         pass # No code here yet


# 3. Create Examples as Tests
<!-- '' = raise exception 'No text given'-->
<!-- 'an artist', 'a track' = call add method and check list var for concatenation. ['an artist: a track'] -->
<!-- 'an artist', 'a track' then 'second artist', 'second track' = call add method twice then check list. ['an artist: a track', second artist: second track']  -->
<!-- 123 = raise exception 'Not text format' -->
<!-- no input = call list method, empty list. Raise exception 'No tracks added!' -->
# Make a list of examples of how the class will behave in different situations.

# # EXAMPLE

# """
# Given a name and a task
# #remind reminds the user to do the task
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("Walk the dog")
# reminder.remind() # => "Walk the dog, Kay!"

# """
# Given a name and no task
# #remind raises an exception
# """
# reminder = Reminder("Kay")
# reminder.remind() # raises an error with the message "No task set."

# """
# Given a name and an empty task
# #remind still reminds the user to do the task, even though it looks odd
# """
# reminder = Reminder("Kay")
# reminder.remind_me_to("")
# reminder.remind() # => ", Kay!"
# Encode each example as a test. You can add to the above list as you go.

# 4. Implement the Behaviour