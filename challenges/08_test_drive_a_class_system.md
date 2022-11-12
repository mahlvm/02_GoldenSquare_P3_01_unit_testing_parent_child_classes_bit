# Test-drive a Multi-Class Program

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to test-drive a multi-class program.

## Introduction

[This is a bit easier to follow on the video.](https://youtu.be/CGOETBVIaPQ?t=0s)

In these challenges we started off test-driving a single method. Then we moved
to test-driving a class, which incorporated multiple methods. Now we will move
again to test-driving a system involving multiple classes.

This presents us with some new design challenges. We will cover those in the
next challenge. For now, we will focus on test-driving.

The principle here is similar to jumping from methods to classes. We still need
to generate examples and encode these as tests, followed up by implementing
behaviour to match those examples.

Consider the following design for a music library.

```python
# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        pass

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        pass
    
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        pass
```

```python
# File: lib/track.py

class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        # Parameters:
        #   title: a string
        #   artist: a string
        # Side-effects:
        #   Sets the title and artist properties
        pass

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        pass

```

Based on this, we might come up with the following examples:

```python
"""
When we add two tracks
We get the tracks back in the track list
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("Way") # => [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("lace") # => [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
library = MusicLibrary()
track_1 = Track("Always The Hard Way", "Terror")
track_2 = Track("Higher Place", "Malevolence")
library.add(track_1)
library.add(track_2)
library.search_by_title("zzz") # => []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
track = Track("Higher Place", "Malevolence")
track.format() # => "Higher Place by Malevolence"
```

When encoding these into tests, we are left with a surprising decision — which
test suite do they go in? They test both `MusicLibrary` and `Track` — so which
is it? What do we call the tests?

Tests for multiple classes acting together are called **integration tests** or
sometimes **feature tests**. Tests for a single class or method are called
**unit tests**.

We create integration tests like this:

```python
# File: tests/test_music_library_integration.py
from lib.music_library import MusicLibrary
from lib.track import Track


def test_music_library_integration():
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
# File: tests/test_music_library_integration.py
def test_music_library_integration():
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
# File: tests/test_unit_music_library.py

def test_music_library():
    library = MusicLibrary()
  
  # ...

```

Implement it:

```python
# File: lib/music_library.py

class MusicLibrary:
  pass

```

And then back to the integration test to uncomment the next line:

```python
# File: tests/test_music_library_integration_spec.py

def test_music_library_integration():
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

class Diary:
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

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
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass
```

[Example solution.](https://youtu.be/CGOETBVIaPQ?t=1738s)

## Challenge

Test-drive a class system based on this design:

```python
# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
```


[Next Challenge](09_design_a_class_system.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F08_test_drive_a_class_system.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
