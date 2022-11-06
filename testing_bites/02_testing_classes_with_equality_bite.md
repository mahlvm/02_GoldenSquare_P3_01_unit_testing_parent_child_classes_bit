# Testing Classes with Equality

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test classes with equality using pytest.

## Introduction

Testing classes is fundamentally similar to testing functions. However, classes
perform a different job to functions. Instead of taking some arguments and
giving a return value like a function, classes look after some data (state) with
a common group of methods (behaviour).

So we need to adapt our approach. Here is an example:

```python
# File: lib/reminder.py

class Reminder:
    def __init__(self, name):
        self.name = name

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        return f"{self.task}, {self.name}!"
```

```python
# File: tests/test_reminder.py

from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# We would typically have a number of these examples.
```

Rather than our example being to call one method and check the return value, our
example involves calling a number of methods that exercise the intended
behaviour of the class.

## Demonstration

[Demonstration Video](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=1605s)

## Exercise

### One

Add this file into your `lib/` directory.

```python
# File: lib/counter.py

class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."
```

Write some tests for this class.

### Two

Add this file into your `lib/` directory.

```python
# File: lib/string_builder.py

class StringBuilder:
    def __init__(self):
        self.str = ""

    def add(self, str):
        self.str += str

    def size(self):
        return len(self.str)

    def output(self):
        return self.str
```

Write some tests for this class.

### Example Solutions

[Example Solution](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=1991s)

## Challenge

Add this file into your `lib/` directory.

```python
# File: lib/gratitudes.py

class Gratitudes:
    def __init__(self):
        self.gratitudes = []

    def add(self, gratitude):
        self.gratitudes.append(gratitude)

    def format(self):
        formatted = "Be grateful for: "
        formatted += ", ".join(self.gratitudes)
        return formatted
```

Write some tests for this class.


[Next Challenge](03_testing_for_errors_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F02_testing_classes_with_equality_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F02_testing_classes_with_equality_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F02_testing_classes_with_equality_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F02_testing_classes_with_equality_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F02_testing_classes_with_equality_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
