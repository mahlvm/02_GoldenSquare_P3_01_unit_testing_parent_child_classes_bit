# Test-drive a Multi-Class Program

_**This is a Makers Vine.** Vines are designed to gradually build up sophisticated skills. They contain a mixture of text and video, and may contain some challenge exercises without proposed solutions. [Read more about how to use Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to test-drive a multi-class program.

## Introduction

[This is a bit easier to follow on the video.](https://www.youtube.com/watch?v=eRniAN07Eow&t=0s)

In these challenges we started off test-driving a single method. Then we moved
to test-driving a class, which incorporated multiple methods. Now we will move
again to test-driving a system involving multiple classes.

This presents us with some new design challenges. We will cover those in the
next challenge. For now, we will focus on test-driving.

The principle here is similar jumping from methods to classes. We still need to
generate examples and encode these as tests, followed up by implementing
behaviour to match those examples.

Consider the following design for a music library.

```python
# File: lib/music_library.py

class MusicLibrary():
  def __init__():
    # ...

  def add(track): # track is an instance of Track
    # Track gets added to the library
    # Returns nothing


  def all():
    # Returns a list of track objects

  
  def search_by_title(keyword): # keyword is a string
    # Returns a list of tracks with titles that include the keyword

```

```python
# File: lib/track.py

class Track():
  def __init__(title, artist): # title and artist are both strings
  

  def title():
    # Returns the title as a string
  

  def format():
    # Returns a string of the form "TITLE by ARTIST"
  

```

Based on this, we might come up with the following examples:

```python
# 1 - gets all tracks
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.all() # => [track_1, track_2]

# 2 - searches by keyword
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("Higher") # => [track_2]

# 3 - searches by substring too
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("lace") # => [track_2]

# 4 - if no results, search yields empty list
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("zzz") # => []

# 5 - formats individual tracks
track_2 = Track("Higher Place", "Malevolence")
track.format() # => "Higher Place by Malevolence"
```

When encoding these into tests, we are left with a surprising decision — which
test suite do they go in? They test both `MusicPlayer` and `Track` — so which is
it? What do we call the tests?

Tests for multiple classes acting together are called **integration tests** or
sometimes **feature tests**. Tests for a single class or method are called
**unit tests**.

We create integration tests like this:

```python
# File: tests/test_music_player_integration.py

def test_music_player_integration():
  library = MusicLibrary()
  track_1 = Track("Always The Hard Way", "Terror")
  track_2 = Track("Higher Place", "Malevolence")
  library.add(track_1)
  library.add(track_2)
  assert library.search_by_title("Always") == [track_1]
  # ...

```

However, this is quite a bit to test-drive in one go, so we comment out all but
one line:

```python
# File: tests/test_music_player_integration.py
def test_music_player_integration():
  library = MusicLibrary()
  # track_1 = Track("Always The Hard Way", "Terror")
  # track_2 = Track("Higher Place", "Malevolence")
  # library.add(track_1)
  # library.add(track_2)
  # assert library.search_by_title("Always") == [track_1]
  
  
  # ...

```

And then focus on our `MusicLibrary` class. We create a unit test for that
class:

```python
# File: tests/test_unit_music_player.py

def test_music_library():
    library = MusicLibrary()
  
  # ...

```

Implement it:

```python
# File: lib/music_player.py

class MusicPlayer():
  pass

```

And then back to the integration test to uncomment the next line:

```python
# File: spec/music_player_integration_spec.rb

def test_music_player_integration():
  library = MusicLibrary()
  track_1 = Track("Always The Hard Way", "Terror")
  # track_2 = Track("Higher Place", "Malevolence")
  # library.add(track_1)
  # library.add(track_2)
  # assert library.search_by_title("Always") == [track_1]
  
  # ...

```

And so on. This is demonstrated through to finish in the video.

At some point you will come across another problem. How do you unit test
`MusicLibrary` without relying on `Track` and inadvertently making it an
integration test?

We are going to leave that subject alone for now and come back to it later. For
now, if you feel yourself about to write a unit test that should exist in the
integration tests — put it in the integration tests and leave it out of the unit
tests. This may make some of your unit tests quite small, which is OK.

## Exercise

Test-drive a class system based on this design.

This is quite a bit to think about — so I suggest making a list of examples for
your integration tests first in a text file, before you start on test-driving,
to make sure you've thought through the full system.

```python
# File: lib/diary.py
class Diary():
  def __init__(self):
    pass
  

  def add(entry): # entry is an instance of DiaryEntry
    # Returns nothing
  

  def all():
    # Returns a list of instances of DiaryEntry
  

  def count_words():
    # Returns the number of words in all diary entries
    # HINT: This method should make use of the `count_words` method on DiaryEntry.
  

  def reading_time(wpm): # wpm is an integer representing
                        # the number of words the user can read per minute
    # Returns an integer representing an estimate of the reading time in minutes
    # if the user were to read all entries in the diary.
  

  def find_best_entry_for_reading_time(wpm, minutes):
        # `wpm` is an integer representing the number of words the user can read
        # per minute.
        # `minutes` is an integer representing the number of minutes the user
        # has to read.
    # Returns an instance of diary entry representing the entry that is closest 
    # to, but not over, the length that the user could read in the minutes they
    # have available given their reading speed.
  


# File: lib/diary_entry.py
class DiaryEntry():
  def initialize(self, title, contents): # title, contents are strings
    # ...
  

  def title():
    # Returns the title as a string
  

  def contents():
    # Returns the contents as a string
  

  def count_words():
    # Returns the number of words in the contents as an integer
  

  def reading_time(wpm): # wpm is an integer representing
                        # the number of words the user can read per minute
    # Returns an integer representing an estimate of the reading time in minutes
    # for the contents at the given wpm.
  

  def reading_chunk(wpm, minutes): # `wpm` is an integer representing the number
                                  # of words the user can read per minute
                                  # `minutes` is an integer representing the
                                  # number of minutes the user has to read
    # Returns a string with a chunk of the contents that the user could read
    # in the given number of minutes.
    # If called again, `reading_chunk` should return the next chunk, skipping
    # what has already been read, until the contents is fully read.
    # The next call after that it should restart from the beginning.
  

```

**#TODO** NOT DONE IN PYTHON[Example solution.](https://www.youtube.com/watch?v=eRniAN07Eow&t=1400s)

## Challenge

Test-drive a class system based on this design:

```python
# File: lib/todo_list.py
class TodoList():
  def __init__(self):
  

  def add(todo): # todo is an instance of Todo
    # Returns nothing
  

  def incomplete():
    # Returns all non-done todos
  

  def complete():
    # Returns all complete todos
  

  def give_up():
    # Marks all todos as complete
  


# File: lib/todo.py
class Todo():
  def initialize(task): # task is a string
    # ...
  

  def task():
    # Returns the task as a string
  

  def mark_done():
    # Marks the todo as done
    # Returns nothing
  

  def done():
    # Returns true if the task is done
    # Otherwise, false
  

```


[Next Challenge](09_design_a_class_system.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
