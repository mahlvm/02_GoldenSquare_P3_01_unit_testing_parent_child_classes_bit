# Testing Functions with Equality

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test functions using pytest.

## Introduction

_To follow along, [set up a pytest project using this
guide.](../pills/setting_up_a_pytest_project.md)_

We can use `assert` to test whether a function returns the right value. Here's
an example:

```python
# File: lib/add_five.py
def add_five(num):
    return num + 5
```

```python
# File: tests/test_add_five.py
from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8
```

```shell
# To run the tests
; pipenv run pytest
======================= test session starts ========================
platform darwin -- Python 3.8.2, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/simo/code/python-scratch
collected 1 item

tests/test_add_five.py .                                     [100%]

======================== 1 passed in 0.01s ========================
```

<details>
  <summary>:confused: My `pytest` says `ERROR collecting tests/test_add_five.py` or `ModuleNotFoundError: No module named 'lib'`</summary>

---

Have you put empty `__init__.py` files into both the `lib/` and `test`
directories? That's necessary for `pytest` to find your code. Your project
structure should look something like this:

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init__.py
  │   └── add_five.py
  └── tests
      ├── __init__.py
      └── test_add_five.py
  ```

---
</details>

<details>
  <summary>:confused: My `pytest` says `collected 0 items or `no tests ran`</summary>

---

Have you prefixed the name of your test file with `test`, like this:
`test_add_five.py`? That's necessary for `pytest` to find your tests. Your
project structure should look something like this: 

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init__.py
  │   └── add_five.py
  └── tests
      ├── __init__.py
      └── test_add_five.py
  ```

Also check that you've prefixed the names of your test methods with `test`, as
this is necessary for `pytest` to find your tests.

---
</details>

Then, if the function is broken in some way, the test fails.

```python
# File: lib/add_five.py
def add_five(num):
    return num + 4 # Oh no!!
```

```shell
# To run the tests
; pipenv run pytest
======================= test session starts ========================
platform darwin -- Python 3.8.2, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/simo/code/python-scratch
collected 1 item

tests/test_add_five.py F                                     [100%]

============================= FAILURES =============================
______________ test_add_five_returns_eight_for_three _______________

    def test_add_five_returns_eight_for_three():
      result = add_five(3)
>     assert result == 8
E     assert 7 == 8

tests/test_add_five.py:6: AssertionError
===================== short test summary info ======================
FAILED tests/test_add_five.py::test_add_five_returns_eight_for_three
======================== 1 failed in 0.05s =========================
```

Let's break down the contents of the `test_add_five.py` file:

```python
# File: tests/test_add_five.py

# We have to import the function we want to test first.
from lib.add_five import *

# Next, we create a single test example.
# The function name must start with `test_` for pytest to find it.
# The rest of the function should describe what the test verifies.
def test_add_five_returns_eight_for_three():
    # We run the function with an example argument 3.
    result = add_five(3)

    # And then assert that in this example it should return 8.
    assert result == 8

    # pytest will run this example, and if this example doesn't work like you
    # said it would, the test will fail.

# We can put more test examples here...
```

## Demonstration

[Demonstration Video](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=0s)

## Exercise

[To set up a pytest project for these exercises, follow this
guide.](../pills/setting_up_a_pytest_project.md)

### One

Add this file into your `lib/` directory.

```python
# File: lib/greet.py

def greet(name):
    return f"Hello, {name}!"
```

Write a test for this function.

<details>
  <summary>:confused: My `pytest` says `collected 0 items` or `no tests ran`</summary>

  ---

  This means `pytest` can't find your tests.

  Check that you have:

  * prefixed the name of your test file with `test`, e.g. `test_greet.py`?
  * prefixed the name of your test function with `test`, e.g.
    ```
    # File: "tests/test_greet.py"
    def test_greet():
      ...
    ```
  
  These things are necessary for `pytest` to find your tests. Your project
  structure should look something like this: 

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init_.py
  │   └── greet.py
  └── tests
      ├── __init__.py
      └── test_greet.py
  ```

  ---
</details>

### Two

Add this file into your `lib/` directory.

```python
# File: lib/check_codeword.py

def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"
```

Write some tests for this function.

### Example Solutions

[Example Solutions](https://www.youtube.com/watch?v=XT30ee3ZfGE&t=597s)

## Challenge

Add this file into your `lib/` directory.

```python
# File: lib/report_length.py

def report_length(str):
    length = len(str)
    return f"This string was {length} characters long."
```

Write some tests for this function.


[Next Challenge](02_testing_classes_with_equality_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_functions_with_equality_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_functions_with_equality_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_functions_with_equality_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_functions_with_equality_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_functions_with_equality_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
