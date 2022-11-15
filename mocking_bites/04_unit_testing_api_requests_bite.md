# Unit Testing API Requests

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test API requests using Pythons mocks. 

## Introduction

> **Note**: To run the examples in this Bite and complete the challenge, you
> will need to install a Python library called `requests`.
> 
> To install it, [create a new pytest
> project](../pills/setting_up_a_pytest_project.md) and then run this:
> 
> ```shell
> ; pipenv install requests
> ```
> 
> To check you've done this correctly, then run:
> 
> ```shell
> ; pipenv run python -c "import requests"
> # If this command runs with no output and no errors, you're good!
> ```
> 
> To activate the virtual environment, i.e. before running pytest, then run:
> 
> ```shell
> ; pipenv shell
> ; pytest
> ================================ test session starts ================================
> platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
> rootdir: .../your-project-directory
> collected 0 items
> 
> =============================== no tests ran in 0.01s ===============================
> ```
> 
> If you have any trouble, please consult a coach.

So far this has been a bit theoretical. Now we will show you a realistic
use-case for this technique.

Many applications request data from the internet. That data is regularly
updated, which is great, but it makes it hard to test. Consider:

```python
# File: lib/activity_suggester.py
import requests

class ActivitySuggester:
    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    # This method calls an 'API' on the internet to get a random activity.
    # An API is a way of allowing programs to request data from other programs.
    def _make_request_to_api(self):
        response = requests.get("http://www.boredapi.com/api/activity")
        return response.json()

# Usage
# =====
activity_suggester = ActivitySuggester()
# activity_suggester.suggest() will return a different value every time

print(activity_suggester.suggest())
# Why not: Learn how to use a french press

print(activity_suggester.suggest())
# Why not: Hold a video game tournament with some friends
```

This is really wonderful, but how do we test it?

The answer is to replace `requests` — the Python library we're using to make the
request — with a mock. That way we can control what it returns.

Here's how we do that:

```python
# File: lib/activity_suggester.py

class ActivitySuggester:
    def __init__(self, requester):  # requester is usually `requests`
        self.requester = requester

    def suggest(self):
        response = self._make_request_to_api()
        return f"Why not: {response['activity']}"

    def _make_request_to_api(self):
        # We use 'self.requester' rather than 'requests'
        response = self.requester.get("http://www.boredapi.com/api/activity")
        return response.json()

# Usage
# =====
# import requests
# activity_suggester = ActivitySuggester(requests)
# activity_suggester.suggest() # => "Why not: Learn how to use a french press"
# activity_suggester.suggest() # => "Why not: Hold a video game tournament with some friends"
```

```python
# File: tests/test_activity_suggester.py
from unittest.mock import Mock
from lib.activity_suggester import ActivitySuggester

def test_calls_api_to_provide_suggested_activity():
    requester_mock = Mock(name="requester") # This name is just for readability
    response_mock = Mock(name="response")

    # We tell `requester_mock` to return `response_mock` 
    # when we call `get()` on it.
    requester_mock.get.return_value = response_mock

    # We tell `response_mock` to return a sample output of the API when
    # we call `json()` on it.
    # I got this sample using `curl "https://www.boredapi.com/api/activity"`.
    response_mock.json.return_value = {
        "activity": "Write a short story",
        "type": "recreational",
        "participants": 1,
        "price": 0,
        "link": "",
        "key": "6301585",
        "accessibility": 0.1
    }

    activity_suggester = ActivitySuggester(requester_mock)
    result = activity_suggester.suggest()
    assert result == "Why not: Write a short story"
```

By crafting a mock that acts just like `requests`, at least as far as
`ActivitySuggester` wants to use it, you can make this untestable code testable.

## Demonstration

[Demonstration Video](https://youtu.be/LgWgIzbOBxg?t=5256s)

## Exercise

Unit test this class.

```python
import time
import requests

class TimeError:
    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def error(self):
        return self._get_server_time() - time.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = requests.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]

```

To make this testable, you will need to create a mock for `requests` and also
deal with the behaviour of `time.time()` which is also non-deterministic.

[Example Solution](https://youtu.be/LgWgIzbOBxg?t=6395s)

<!-- OMITTED -->

## Challenge

Unit test this class.

```python
import requests


class CatFacts:
    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = requests.get("https://catfact.ninja/fact")
        return response.json()
```

## Moving On

You've now completed all of the core challenges for this module.

[Head back to the main sequence to take on the project.](../README.md)


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
