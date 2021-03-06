# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" width="24"> cit-assoc-exam
Project folder for advanced python programming course

Instead of using Google Drive, we now will be using Github to keep track of the current state of our project folder.
You can see what we've been working on without downloading anything by looking through this repository.

## Install
Here are the basic steps to download our project to your computer.

A line like `$ cd src` means you should type `cd src` into your terminal/command prompt.

1. If you don't have Git installed, I suggest
[gitforwindows](https://github.com/git-for-windows/git/releases/download/v2.29.0.windows.1/Git-2.29.0-64-bit.exe).
This will allow you to use "git" from your terminal/command prompt.
2. `$ git clone https://github.com/Starchery/cit-assoc-exam.git`
3. `$ cd cit-assoc-exam`
4. `$ pip install poetry`
5. `$ poetry install`
6. (Optional) Read the notes we've taken so far. They're in the [docs](docs/) folder.

## Running the code
For poetry, you have two options.
1. ### Activate a virtual environment

    You can activate the venv created for this project
    by running `$ poetry shell`.
    This will put you inside the venv so you have access
    to any packages/dependencies we have installed.

    From there, you can just run `$ python pcap/day2`
    to run the code for day 2.

    You can exit the shell by simply typing `$ exit`.

2. ### Using `poetry run`

    Instead of activating the venv, you can run
    any command inside the venv by prefixing
    it with `$ poetry run`.

    Thus, the example from option 1 becomes
    `$ poetry run python pcap/day2`.

    This way, you don't have to enter and exit
    a shell whenever you want to run the project code.

## Staying up to date
We'll be adding to this project almost every day.
To make sure you have the most recent version of the project,
you should run `$ git pull` periodically.
This will update your local copy of the project
to reflect whatever changes I've pushed to this repository.

---

<p align="center">
  <img src="https://citinstitute.tech/wp-content/uploads/2019/12/New-CODEIT-LOGO-TRANSPARENT-1.png" height="64">
</p>
