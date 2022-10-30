# Setting Up Pytest

_[A video demonstration is
here. MISSING]()_ **If you follow this
directly, make sure you create a new directory and run the commands in that
directory.**

_[Here is a workshop demonstration of the pairing
flow](https://youtu.be/uLbPGE6pRdc)_

<!-- OMITTED -->

Learn to set up a new pytest project.

## Guidance

Pytest is a kind of programming tool called a test framework. It is written for
use with the programming language Python. We can use it to test that our systems
do what they are supposed to do. We can also use it to build our test-driving
practice.

To set up a new Pytest project:

```shell
# This assumes you have Python installed. If you don't, visit:
# https://python.org/ to install the latest version of Python.

# First, create a directory for your project
; mkdir your-project-directory
; cd your-project-directory

# Next we are going to use pipenv to set up a virtual environment and store our libraries in
; pipenv install pytest
; pipenv run pytest

# If things are running correctly we should be able to run pytest and the command be recognised. It should look like this:
; pytest
================================================== test session starts ==================================================
platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/williamoconnell/Documents/Sandbox/folder_for_foldering_in/pytest_folder
collected 0 items

# If you're running into problems you can double check by running pipenv shell, then pytest again.
; pipenv shell
(pipenv); pytest

# If you do not have pipenv installed, we can use pip to download and install it. 
; pip install pipenv

# If you don't have pip installed, we're going to get you the latest version of Pip with:
; curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
; python3 get-pip.py

# Next, we can install pytest, which handles testing
; pipenv install pytest

# You will need to activate/deactivate your venv if you run pipenv shell. 

# Running pipenv lock will generate a Pipfile that stores the libraries in

; pipenv lock

# Pytest will only run if either the virtual environment is activated or you use pipenv run pipenv!

# Create a folder for your testing files
; mkdir tests

# And create a repository for your changes
; git init .
; git add .
; git commit -m "Project setup"

# Then go and create a repository on github.com
# On the next screen after you have created the repository,
# follow the "Push an existing repository from the command line" section
# To push your project to your github repository
# It will look something like this...
; git remote add origin YOUR_REMOTE_ADDRESS
; git branch -M main
; git push -u origin main

# If you have the GitHub CLI installed you can run everything from the terminal

; gh repo new
> Push an existing local repository to GitHub
> Path to local repository (.) 

```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
