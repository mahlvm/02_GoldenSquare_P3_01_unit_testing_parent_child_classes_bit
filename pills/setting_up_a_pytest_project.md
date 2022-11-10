# Setting Up Pytest

_[A video demonstration is here.](https://youtu.be/zM-YTFlo1pI?t=0s)_

Learn to set up a new pytest project.

## What is pytest?

Pytest is a kind of programming tool called a test framework. It is written for
use with the programming language Python. We can use it to test that our systems
do what they are supposed to do. We can also use it to build our test-driving
practice.

## Prerequisites

Before we start you will need a few prerequisites. You may have installed these
before, but we'll check that they are all there to be sure you are set up well.

```shell
# Let's install pyenv, a tool to manage different versions of Python.
# This will ensure we have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now we'll install the latest Python.
; pyenv install 3.11

# And let's check to see if it is properly installed
; pipenv --version
# If you see "pipenv, version ..." then you can skip the rest of this
# code block and go to the next one.

# Otherwise, run these:
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version
pipenv, version ...

# If you run into trouble here, contact your coach.
```

## Setting up a new project

To set up a new pytest project:

```shell
# First, create a directory for your project
; mkdir your-project-directory
; cd your-project-directory

# Next, install pytest using pipenv
; pipenv install pytest --python 3.11
# This may take a few minutes

# Create a folder for your testing files
; mkdir tests
; mkdir lib

# Create module init files in both `tests/` and `lib/` directories
; touch tests/__init__.py
; touch lib/__init__.py
# These might seem pointless, but they're important for Python to find
# all of your files.

# Verify your setup by running pytest
; pipenv run pytest
================================ test session starts ================================
platform darwin -- Python 3.1, pytest-7.2.0, pluggy-1.0.0
rootdir: .../your-project-directory
collected 0 items

=============================== no tests ran in 0.01s ===============================

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
```

<details>
  <summary>:speech_balloon: Running `pipenv run ...` all the time is annoying.</summary>

  If you like, you can run `pipenv shell` at the start. This will enter you into
  a special terminal environment where pipenv will make all of your dependencies
  available.

  ```shell
  ; pipenv shell
  Launching subshell in virtual environment...
  . /.../virtualenvs/.../bin/activate
  (pyv) ;  . /.../virtualenvs/.../bin/activate
  (pyv) ; 
  
  # Now you can run `pytest` without `pipenv run` on the start.

  (pyv) ; pytest
  # ...
  ```
</details>


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=pills%2Fsetting_up_a_pytest_project.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
