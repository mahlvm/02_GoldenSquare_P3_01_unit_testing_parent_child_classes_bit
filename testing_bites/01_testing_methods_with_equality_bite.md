# Testing Methods with Equality

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test methods using `pytest`.

## Introduction

_To follow along, [set up an `pytest` project using this
guide.](../pills/setting_up_a_pytest_project.md)_

<!-- OMITTED -->

We can use the in-built python keyword `assert` to test whether a method returns the right value. Here's an example:

```python
# File: lib/add_five.py
def add_five(num):
  return num + 5
```

```python
# File: tests/test_add_five.py
from lib.add_five import add_five

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
  <summary>My `pytest` says <code>ERROR collecting tests/test_add_five.py</code> or <code>ModuleNotFoundError: No module named 'lib'</code> :confused: </summary>
<p>

  Have you put empty `__init__.py` files into both the `lib/` and `test` directories?
  That's necessary for `pytest` to find your code.
  Your project structure should look something like this:

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init_.py
  │   └── add_five.py
  └── tests
      ├── __init__.py
      └── test_add_five.py
  ```
</p>
</details>


<details>
  <summary>My `pytest` says <code>collected 0 items</code> or <code>no tests ran</code> :confused: </summary>
<p>

  Have you prefixed the name of your test file with `test`, like this: `test_add_five.py`? 
  That's necessary for `pytest` to find your tests.
  Your project structure should look something like this: 

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init_.py
  │   └── add_five.py
  └── tests
      ├── __init__.py
      └── test_add_five.py
  ```
</p>
</details>

Then, if the method is broken in some way, the test fails.

```python
# File: lib/add_five.py
def add_five(num):
  return num + 4 # Oh no!!
```

```shell
# To run the tests
; pipenv run tests
======================= test session starts ========================
platform darwin -- Python 3.8.2, pytest-7.1.3, pluggy-1.0.0
rootdir: /Users/simo/code/python-scratch
collected 1 item

tests/test_add_five.py F                                     [100%]

============================= FAILURES =============================
______________ test_add_five_returns_eight_for_three _______________

    def test_add_five_returns_eight_for_three():
      """adds 5 to 3 to return 8"""
      result = add_five(3)
>     assert result == 8
E     assert 7 == 8

tests/test_add_five.py:6: AssertionError
===================== short test summary info ======================
FAILED tests/test_add_five.py::test_add_five_returns_eight_for_three
======================== 1 failed in 0.05s =========================
```

Let's break down the contents of the `test_add_five.py` file:

<!-- OMITTED -->

```python
# File: tests/test_add_five.py

# We have to import the method we want to test first.
# The method is called `add_five` and it lives inside the lib.add_five module.
from lib.add_five import add_five

# We create a single test example by creating a function that starts with the
# word "test". pytest only runs functions that start with this word. 
# It is good practice to use the rest of the function name to describe what the
# test example is testing.
def test_add_five_returns_eight_for_three():
  # We run the method with an example argument 3.
  result = add_five(3)
  # And then assert that in this example it should return 8.
  assert result == 8

  # pytest will run this example, and if this example doesn't work like you
  # said it would, the test will fail.

# We can put more test examples here by creating more functions prefixed with
# "test".
```

## Demonstration

[Demonstration Video](<!-- OMITTED -->)

## Exercise

[To set up a `pytest` project for these exercises, follow this guide.](../pills/setting_up_a_pytest_project.md)

<!-- OMITTED -->

### One

Add this file into your `lib/` directory.

```python
# File: lib/greet.py
def greet(name):
  return f"Hello, {name}!"
```

Write a test for this function.

<details>
  <summary>My `pytest` says <code>collected 0 items</code> or <code>no tests ran</code> :confused: </summary>
<p>

  Have you 
  - prefixed the name of your test file with `test`, e.g. `test_greet.py`? 
  - prefixed the name of your test function with `test`, e.g.
    ```
    # File: "tests/test_greet.py"
    def test_greet():
      ...
    ```
  
  These things are necessary for `pytest` to find your tests.
  Your project structure should look something like this: 

  ```
  .
  ├── Pipfile
  ├── Pipfile.lock
  ├── lib
  │   ├── __init_.py
  │   └── greet.py
  └── tests
      ├── __init__.py
      └── test_greet.py
  ```
</p>
</details>

### Two

Add this file into your `lib/` directory.

```python
# File: lib/check_codeword.rb

def check_codeword(codeword):
  if codeword == "horse":
    return "Correct! Come in."
  elif codeword[0] == "h" and codeword[-1] == "e":
    return "Close, but nope."
  else:
    return "WRONG!"
```

Write a test for this method.

### Example Solutions

[Example Solutions](<!-- OMITTED -->)

## Challenge

Add this file into your `lib/` directory.

```python
# File: lib/report_length.py

def report_length(str)
  length = str.length
  return "This string was #{length} characters long."
end
```

Write some tests for this method.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_methods_with_equality_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_methods_with_equality_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_methods_with_equality_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_methods_with_equality_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=testing_bites%2F01_testing_methods_with_equality_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
