# Intermezzo: Debugging 2

_**This is a Makers Vine.** Vines are designed to gradually build up
sophisticated skills. They contain a mixture of text and video, and may contain
some challenge exercises without proposed solutions. [Read more about how to use
Makers
Vines.](https://github.com/makersacademy/course/blob/main/labels/vines.md)_

Learn to debug interactively.

## Introduction

Earlier we introduced the idea of **Discovery Debugging** and getting visibility
using `print` to print out values in the program and follow the flow of
execution.

We'll now show you another technique for discovery debugging — an interactive
debugger.

First, install [the Python extension for VS
Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python), if
you haven't already. This will allow you to use the right debugger.

Then, [please follow this video](https://youtu.be/ncadn-fgeHc). There isn't a
text equivalent because this style of debugger is difficult to clearly
demonstrate in that manner.

The below code will be useful if you want to follow along.

```python
# File: lib/factorial.py

def factorial(n):
    product = 1
    while n > 0:
        n -= 1
        product *= n
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24
```

## Exercise

In this exercise, you're going to use discovery debugging again for a more
complex situation.

Create a pytest project for the following two files and confirm that when you do
`pipenv run pytest` the current unit tests are passing:

```python
# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.text

# File: tests/test_vowel_remover.py

from lib.vowel_remover import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."
```

A colleague has done a code review and has advised that the tests should cover
all the vowels.

Add a new unit test to check that the program can remove all the vowels from
"aeiou", returning an empty string, "". If there are any problems reported by
pytest after adding this new test, use the debugger to look into
`vowel_remover.py` to discover where the problem is and make any necessary
changes.

If you're having trouble or aren't sure what to do and want to watch us running
through the exercise using the debugger, here's [our accompanying
video](https://youtu.be/HuLBrTnRAKs) covering this vowel-removing exercise,
where we also use Watch on things like `self.text[:i]` to gain even more
visibility.

## Challenge

Debug the following program:

```python
# File: lib/letter_counter.py

class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {}
        most_common = None
        most_common_count = 1
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 1) + 1
            if counter[char] > most_common_count:
                most_common = char
                most_common_count += counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())
# Intended output:
# [2, "i"]
```


[Next Challenge](08_test_drive_a_class_system.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F07_intermezzo_debugging_2.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F07_intermezzo_debugging_2.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F07_intermezzo_debugging_2.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F07_intermezzo_debugging_2.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=challenges%2F07_intermezzo_debugging_2.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
