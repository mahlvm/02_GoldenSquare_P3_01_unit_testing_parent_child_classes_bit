# Crafting Mocks

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to craft mocks for specific purposes.

## Introduction

In the last bite we introduced mocks. Mocks are a tool that we use when we
want to test that one class interacts with another in the correct way. We create
a mock that acts the same as the collaborator class, and then verify that the
class we're trying to test does its job correctly.

To do this we have to create a mock whose public interface matches the public
interface of the class we're trying to test. In this bite we will zoom in on how
to create mocks with specific requirements.

Below are some examples of how you can use mocks. Each example shows you how
the mock might be created as a class first, and then how it can be created
using a mock. Going forward you will usually use the mocking techniques only.

### An Object

```python
# As a class
class FakeObject:
    pass

fake_object = FakeObject()

# As a mock
from unittest.mock import Mock
fake_object = Mock()
```

### An Object With Methods

```python
# As a class
class FakeObject:
    def greet(self):
        return "Hello, world!"

fake_object = FakeObject()
fake_object.greet() # => 'Hello, world!'

# As a mock
from unittest.mock import Mock

# This creates the mock
fake_object = Mock()

# This tells the mock to return 'Hello, world!' when the greet method is called
fake_object.greet.return_value = "Hello, world!"   

# This is just to show you what it can now do
assert fake_object.greet() == "Hello, world!"
```

### To Verify Methods Are Called With Given Arguments

```python
# As a class
class FakeObject:
    def __init__(self):
        self.greet_has_been_called = False

    def greet(self, name):
        self.greet_has_been_called = True
        assert name == "Kay"
        return "Hello, Kay!"

fake_object = FakeObject()

assert fake_object.greet_has_been_called == False
assert fake_object.greet("Kay") == "Hello, Kay!"
assert fake_object.greet_has_been_called == True
fake_object.greet("Henry") # Raises an error

# As a mock
from unittest.mock import Mock

# This creates the mock
fake_object = Mock()

# This tells the mock to return 'Hello, Kay!' when the greet method is called
fake_object.greet.return_value = "Hello, Kay!"

# Now let's call greet
assert fake_object.greet("Kay") == "Hello, Kay!"

# We can use the mock to assert that greet was called
fake_object.greet.assert_called() # This will pass
fake_object.greet.assert_called_with("Henry") # This will throw an error
```

<detail>
  <summary>What happens if we call a method that hasn't been set up?</summary>

  ```python
  from unittest.mock import Mock

  fake_object = Mock()
  fake_object.greet("Kay")
  fake_object.greet.assert_called()
  fake_object.greet.assert_called_with("Kay")
  ```

  Mocking libraries vary on this point, but `unittest.mock` mocks will quietly
  accept any method you might call on it. You can take this to extremes even:

  ```python
  from unittest.mock import Mock

  fake_object = Mock()
  fake_object.greet("Kay").wave_goodbye("Jim").wave_hello("Henry")
  fake_object.greet.assert_called_with("Kay")
  fake_object.greet().wave_goodbye.assert_called_with("Jim")
  fake_object.greet().wave_goodbye().wave_hello.assert_called_with("Henry")
  ```

  You probably won't need to do that very often though, so don't worry if it
  seems confusing right now.

</detail>

## Demonstration

[Demonstration Video](https://youtu.be/LgWgIzbOBxg?t=2657s)

## Exercise

Create mocks to pass these tests.

```python
import pytest
from unittest.mock import Mock

# Delete the lines starting with `@pytest.mark.skip` one by one as you work through.

@pytest.mark.skip(reason="not yet implemented")
def test_set_up_blank_mock():
    # Uncomment and set up your mocks here
    # fake_object = ...

    # Don't edit below
    assert fake_object is not None


@pytest.mark.skip(reason="not yet implemented")
def test_set_up_mock_with_methods():
    # Uncomment and set up your mocks here
    # fake_object = ...

    # Don't edit below
    assert fake_object.speak("Jess") == "Meow, Jess"
    assert fake_object.count_ears() == 2
    assert fake_object.count_legs() == 4


@pytest.mark.skip(reason="not yet implemented")
def test_assert_that_mock_was_called():
    fake_object = Mock()

    # Don't edit this next line
    fake_object.speak("Steve")

    # Write an assertion below that the method "speak" was called with
    # the argument "Steve"


@pytest.mark.skip(reason="not yet implemented")
def test_creates_mock_for_specific_case():
    fake_diary = Mock()

    # Set up this mock to pass the tests below
    # ...

    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add(Mock())
    assert fake_diary.count_entries() == 2

```

[Example Solution](https://youtu.be/LgWgIzbOBxg?t=3390s)

## Challenge

Create mocks to pass this test.

```python
def test_creates_a_sophisticated_mock():
    # Uncomment and set up your mocks here
    # task_list = 
    # task = 

    # Don't edit below
    task_list.add(task)
    assert task_list.list() == [task]
    assert task_list.count() == 1
    assert task_list.clear() == "success"
```


[Next Challenge](03_unit_testing_peer_classes_bite.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F02_crafting_mocks_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F02_crafting_mocks_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F02_crafting_mocks_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F02_crafting_mocks_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F02_crafting_mocks_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
