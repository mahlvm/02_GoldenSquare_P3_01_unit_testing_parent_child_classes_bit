# Unit Testing API Requests

_**This is a Makers Bite.** Bites are designed to train specific skills or
tools. They contain an intro, a demonstration video, some exercises with an
example solution video, and a challenge without a solution video for you to test
your learning. [Read more about how to use Makers
Bites.](https://github.com/makersacademy/course/blob/main/labels/bites.md)_

Learn to test API requests using Pythons mocks. 

> **Note**: To run the examples in this Bite and complete the challenge, you will need to install a Python library called `requests`.
> To install it, run `pipenv install requests` in your `mocking_bites` project directory. Do all your work for this Bite within your `mocking_bites` project.

## Introduction

So far this has been a bit theoretical. Now we will show you a realistic
use-case for this technique.


Many applications request data from the internet. That data is regularly
updated, which is great, but it makes it hard to test. Consider:

```python
import json
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
# activity_suggester = ActivitySuggester()
# activity_suggester.suggest() # => "Why not: Learn how to use a french press"
# activity_suggester.suggest() # => "Why not: Hold a video game tournament with some friends"
```

This is really wonderful, but how do we test it?

The answer is to replace `requests` — the Python library we're using to make the
request — with a mock. That way we can control what it returns.

Here's how we do that:

```python
import json
import requests

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


# To test this
from unittest.mock import Mock

def test_calls_api_to_provide_suggested_activity():
  requester_mock = Mock(name="requester")
  response_mock = Mock(name="response")
  # We set up `requester_mock` to return `response_mock` when called with
  # `.get()`.
  requester_mock.get.return_value = response_mock
  # And we set up `response_mock` to return a sample output of the API when
  # called with `.json()`.
  # I got this using `curl "https://www.boredapi.com/api/activity"`.
  response_mock.json.return_value =  {
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

By crafting a mock that acts just like `requests`, at least as far as `ActivitySuggester` wants to use it, you can make this untestable code testable.

## Demonstration

[Demonstration Video](<!-- OMITTED -->)

## Exercise

Unit test this class.

```python
 import json
 import time
 import requests
 
 class TimeError:
  # Returns difference in seconds between server time
  # and the time on this computer
  def error(self):
    return self._get_server_time() - time.time()

  def _get_server_time(self):
    response = requests.get("https://worldtimeapi.org/api/ip")
    json = response.json()
    return json["unixtime"]
```

To make this testable, you will need to create a mock for `requests` and also
deal with the behaviour of `time.time()` which is also non-deterministic.

[Example Solution](<!-- OMITTED -->)

<!-- OMITTED -->


## Challenge

Unit test this class.

```python
import json
import requests

class CatFacts:
 def provide(self):
   return f"Cat fact: {self._get_cat_fact()['fact']}"

 def _get_cat_fact(self):
   response = requests.get("https://catfact.ninja/fact")
   return response.json()
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=mocking_bites%2F04_unit_testing_api_requests_bite.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
