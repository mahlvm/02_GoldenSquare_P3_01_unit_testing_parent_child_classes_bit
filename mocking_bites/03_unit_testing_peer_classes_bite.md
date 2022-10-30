# Unit Testing peer Classes

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to unit test peer classes.

## Introduction

A peer relationship between classes is one where a class is associated with
another class one-to-one.

The principle of unit testing peer classes is very similar to testing
parent-child classes. Consider this example:

```python
# File: lib/diary_entry.py

class DiaryEntry:
  def __init__(self, title, contents): # title, contents are both strings
    ...

  def title(self):
    # Returns the title as a string
    ...

  def contents(self):
    # Returns the contents as a string
    ...
```

```python
# File: lib/diary_reader.py

class DiaryEntryFormatter:
  def __init__(self, diary_entry): # diary_entry is an instance of DiaryEntry
    ...

  def format(self):
    # Returns a nicely formatted diary entry
    ...
```

In this case, instead of creating a mock and passing it into a method, we pass
it into the class' `__init__` method.

```python
# File: spec/test_diary_entry_formatter.py
from unittest.mock import Mock

def test_formats_a_diary_entry():
  fake_diary_entry = Mock()
  fake_diary_entry.title.return_value = "Hello"
  fake_diary_entry.contents.return_value = "Hello, world!"
  formatter = DiaryEntryFormatter(fake_diary_entry)
  assert formatter.format() == "Hello: Hello, world!"
```

## Demonstration

[Demonstration Video](<!-- OMITTED -->)

## Exercise

Consider these class designs:

```python
# File: lib/secret_diary.py

class SecretDiary:
  def __init__(self, diary): # diary is an instance of Diary
    ...

  def read(self):
    # Raises the error "Go away!" if the diary is locked
    # Returns the diary's contents if the diary is unlocked
    # The diary starts off locked
    ...

  def lock(self):
    # Locks the diary
    # Returns nothing
    ...

  def unlock(self):
    # Unlocks the diary
    # Returns nothing
    ...
```

```python
# File: lib/diary.py

class Diary
  def __init__(self, contents): # contents is a string
    ...

  def read(self):
    # Returns the contents of the diary
    ...
```

Test-drive these classes. Include:

1. Integration tests
2. Unit tests, exercising _all_ of the class's functionality, _without_ using or
   referring to the other class.

[Example Solution](<!-- OMITTED -->)

## Challenge

Add this class design to your `01_mocking_bite_exercise` codebase from the
previous exercise.

```python
class TaskFormatter:
  def __init__(self, task): # task is an instance of Task
    ...

  def format(self):
    # Returns the task formatted as a string.
    # If the task is not complete, the format is:
    # - [ ] Task title
    # If the task is complete, the format is:
    # - [x] Task title
    ...
```

Test-drive this class using unit tests and mocking. 

You can also add some integration tests if you want some more practice of that.


[Next Challenge](04_unit_testing_api_requests_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F03_unit_testing_peer_classes_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F03_unit_testing_peer_classes_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F03_unit_testing_peer_classes_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F03_unit_testing_peer_classes_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F03_unit_testing_peer_classes_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
