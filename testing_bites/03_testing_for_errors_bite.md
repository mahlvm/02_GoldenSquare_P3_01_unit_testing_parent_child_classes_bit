# Testing For Errors

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test for errors using pytest.

## Introduction

Sometimes you want your code to throw an error. For example:

```python
# File: lib/reminder.py

class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"
```

But if we take the naïve approach to testing this:

```python
# File: tests/test_reminder.py

from lib.reminder import *


def test_reminder():
    reminder = Reminder("Kay")
    result = reminder.remind()
    assert result == "No reminder set!"
```

This will not work. Here's the error:

```plain
tests/test_reminder.py F                                              [100%]

================================= FAILURES ==================================
_______________________________ test_reminder _______________________________

    def test_reminder():
        reminder = Reminder("Kay")
>       result = reminder.remind()

tests/test_reminder.py:7:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <lib.reminder.Reminder object at 0x101b3de90>

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
>           raise Exception("No reminder set!")
E           Exception: No reminder set!

lib/reminder.py:14: Exception
========================== short test summary info ==========================
FAILED tests/test_reminder.py::test_reminder - Exception: No reminder set!
============================= 1 failed in 0.04s =============================
```

This is because errors behave in an unusual way. They stop the program
immediately, so the method doesn't return anything any more — it doesn't even
get that far!

To test that errors are thrown properly, we have to adapt our approach:

```python
# File: tests/test_reminder.py

import pytest # <-- New code
from lib.reminder import *


def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"
```

There are three key differences:

1. We import `pytest` so we can use it to check for errors.
2. We use `with pytest.raises(Exception) as e:` to set up a section of the code
   where we expect an error to happen and then be caught by pytest.
3. We use `str(e.value)` to get the error message that was generated, and then
   assert that it is the correct one.

This syntax may be feel unusual. For example, what is `with` or `as`. These are
more advanced topics which you are welcome to research. In the interests of
focus, we will use them purely to test for errors in this module.

All you need to remember for now is that when you are testing for errors, you
can use the above syntax.

## Demonstration

[Demonstration Video](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=2852s)

## Exercise

Add this file into your `lib/` directory.

```python
# File: lib/present.py

class Present:
    def __init__(self):
        self.contents = None

    def wrap(self, contents):
        if self.contents is not None:
            raise Exception("A contents has already been wrapped.")
        self.contents = contents

    def unwrap(self):
        if self.contents is None:
            raise Exception("No contents have been wrapped.")
        return self.contents
```

Write some tests for this class.

[Example Solution](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=3317s)

## Challenge

Add this file into your `lib/` directory.

```python
# File: lib/password_checker.py

class PasswordChecker:
    def check(self, password):
        if len(password) >= 8:
            return True
        else:
            raise Exception("Invalid password, must be 8+ characters.")
```

Write some tests for this class.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F03_testing_for_errors_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F03_testing_for_errors_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F03_testing_for_errors_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F03_testing_for_errors_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F03_testing_for_errors_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
