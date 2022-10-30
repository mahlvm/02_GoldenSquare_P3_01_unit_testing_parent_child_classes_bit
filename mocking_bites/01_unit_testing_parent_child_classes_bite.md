# Unit Testing Parent-Child Classes

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to unit test parent-child classes.

## Introduction

[This is a bit easier to follow on the video.](<!-- OMITTED -->)

A parent-child relationship between classes is one where there is a single class
that looks after a list of other classes. For example, a `Diary` having many
`Entries`.

Consider the following design:

```python
class Diary:
  def add(self, entry): # entry is an instance of DiaryEntry
    ...

  def entries(self):
    # Returns a list of DiaryEntries
    ...

  def count_words(self):
    # Returns the number of words in all entries
    ...

class DiaryEntry:
  def __init__(self, title, contents): # title, contents are both strings
    ...

  def title(self):
    # Returns title as a string
    ...

  def contents(self):
    # Returns contents as a string
    ...

  def count_words(self):
    # Returns the number of words in the contents
    ...
```

And let's suppose we wanted to integration test the word counting behaviour.

```python
from lib.diary import Diary, DiaryEntry

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

Let's say that `Diary.count_words` will call the `count_words` method on every
`DiaryEntry` instance that it has been asked to store.

Secondly, we need to create fake versions of `DiaryEntry` that will live totally
within our tests. They will behave similarly to a real diary entry, but return
fixed values. Then we pass that to `Diary` instead.

```ruby
def test_diary_counts_words_in_all_entries():
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
def test_diary_counts_words_in_all_entries_mocks():
  diary = Diary()

  fake_two_word_diary_entry = Mock()
  fake_two_word_diary_entry.count_words.return_value = 2

  fake_three_word_diary_entry = Mock()
  fake_three_word_diary_entry.count_words.return_value = 3

  Diary.add(fake_two_word_diary_entry)
  Diary.add(fake_three_word_diary_entry)

  assert diary.count_words() == 5
```

This technique of creating fake classes for testing purposes is called **mocking**.

## Exercise

Consider these class designs:

```python
# File: lib/music_library.py

class MusicLibrary:
  def __init__(self):
    ...

  def add(self, track): # track is an instance of Track
    # Track gets added to the library
    # Returns nothing
    ...

  def all(self):
    # Returns a list of track objects
    ...
  
  def search(self, keyword): # keyword is a string
    # Returns a list of tracks that match the keyword
    ...
```

```python
# File: lib/track.py

class Track:
  def __init__(self, title, artist): # title and artist are both strings
    ...

  def matches(self, keyword): # keyword is a string
    # Returns true if the keyword matches either the title or artist
    ...
```

Test-drive these classes. Include:

1. Integration tests
2. Unit tests, exercising _all_ of the class's functionality, _without_ using or referring to the other class.

[Example Solution](<!-- OMITTED -->)

## Challenge

There is a codebase in [`codebases/mocking_bites`](../codebases/mocking_bites).

Clone this repository and open the `codebases/mocking_bites` directory in your editor.

There are some classes and tests in there representing a `TaskList` program.
There are some unit tests for `TaskList` in `tests/test_task_list.rb`.
They currently avoid testing any behaviour that might use the `Task` class.

Use mocking techniques to add some tests that fully test the behaviour of `TaskList`.


[Next Challenge](02_crafting_mocks_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F01_unit_testing_parent_child_classes_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
