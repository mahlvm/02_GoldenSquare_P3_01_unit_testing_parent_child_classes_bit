# Unit Testing Parent-Child Classes

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to unit test parent-child classes.

## Introduction

[This is a bit easier to follow on the video.](https://youtu.be/LgWgIzbOBxg?t=0s)

A parent-child relationship between classes is one where there is a single class
that looks after a list of other classes. For example, a `Diary` having many
`Entries`.

Consider the following design:

```python
# File: lib/diary.py

class Diary:
    # Public properties:
    #   entries: a list of instances of DiaryEntry

    def __init__(self):
        pass

    def add(self, entry):
        # entry is an instance of DiaryEntry
        pass

    def count_words(self):
        # Returns the number of words in all entries
        pass
```

```python
# File: lib/diary_entry.py

class DiaryEntry:
    # Public properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # title, contents are both strings
        pass

    def count_words(self):
        # Returns the number of words in the contents
        pass
```

And let's suppose we wanted to integration test the word counting behaviour.

```python
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_counts_words_in_all_entries():
    diary = Diary()
    diary.add(DiaryEntry("title1", "one two"))
    diary.add(DiaryEntry("title2", "three four five"))
    assert diary.count_words() == 5
```

That's OK. However, for reasons that will come up later in these bites, we
sometimes want to be able to **unit test** `Diary`, so that we can have a test
suite that will fully test the behaviour of `Diary` without relying on any other
classes. 

Then, if the tests for `Diary` fail, we can be _certain_ that `Diary` is broken.
This can be very useful when debugging in a vast codebase.

To do that, we need to change our tests so that `DiaryEntry` is never used. In
theory, we should be able to totally delete `DiaryEntry` and still know that
`Diary` works.

How can we do this?

Firstly, we need to determine how `Diary` will use `DiaryEntry` in this example.
This is a little tricky because we haven't yet written the code, so we might
need to shift back into the design phase for a bit.

Let's say that `Diary#count_words` will call the `#count_words` method on every
`DiaryEntry` instance that it has been asked to store.

Secondly, we need to create fake versions of `DiaryEntry` that will live totally
within our tests. They will behave similarly to a real diary entry, but return
fixed values. Then we pass that to `Diary` instead.

```python
def test_diary_counts_words_in_all_entries_with_fakes():
    diary = Diary()
    diary.add(FakeTwoWordDiaryEntry())
    diary.add(FakeThreeWordDiaryEntry())
    assert diary.count_words() == 5


class FakeTwoWordDiaryEntry:
    def count_words(self):
        return 2


class FakeThreeWordDiaryEntry:
    def count_words(self):
        return 3
```

Now the `Diary` class can be tested in isolation. No matter what mistakes we
make elsewhere in the application, the tests for `Diary` will prove that it
still works as it was designed.

To save us typing, Python also provides a way to easily create those fake objects and define how they should behave:

```python
# We need to import a new tool from the unittest library
from unittest.mock import Mock

def test_diary_counts_words_in_all_entries_with_mocks():
    diary = Diary()

    fake_two_word_diary_entry = Mock()
    fake_two_word_diary_entry.count_words.return_value = 2

    fake_three_word_diary_entry = Mock()
    fake_three_word_diary_entry.count_words.return_value = 3

    diary.add(fake_two_word_diary_entry)
    diary.add(fake_three_word_diary_entry)

    assert diary.count_words() == 5
```

This technique of creating fake classes for testing purposes is called **mocking**.

## Exercise

Consider these class designs:

```python
# File: lib/music_library.py

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        pass

    def add(self, track):
        # track is an instance of Track
        # Track gets added to the library
        # Returns nothing
        pass

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        pass
```

```python
# File: lib/track.py

class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        pass

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        pass
```

Test-drive these classes. Include:

1. Integration tests
2. Unit tests, exercising _all_ of the class's functionality, _without_ using or
   referring to the other class.

[Example Solution](https://youtu.be/LgWgIzbOBxg?t=1562s)

## Challenge

There is a codebase in [`codebases/mocking_bites`](../codebases/mocking_bites).

Clone this repository and open the `codebases/mocking_bites` directory in your
editor.

There are some classes and tests in there representing a `TaskList` program.
There are some unit tests for `TaskList` in `tests/test_task_list.py`. They
currently avoid testing any behaviour that might use the `Task` class.

Use mocking techniques to add some tests that fully test the behaviour of
`TaskList`.


[Next Challenge](02_crafting_mocks_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
