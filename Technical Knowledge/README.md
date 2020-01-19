# Setup

## Prerequisites (Windows):

1. Install Python 3 https://www.python.org/downloads/

2. Clone repository `git clone git@github.com:ExarGD/mytheresa_task.git`

3. Download ChromeDriver from here https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Place ChromeDriver executable in root folder (if it's not there)

5. Install pipenv `pip3 install pipenv`

6. Execute `$env:PIPENV_VENV_IN_PROJECT="enabled"` for Powershell or `set PIPENV_VENV_IN_PROJECT="enabled"` for CMD (this is needed to create virtualenv directory locally for easier deletion)

7. Go to repository folder

8. `pipenv install`

## Gucci bags task

Run in shell this command:

`pipenv run pytest '.\Technical Knowledge\test_search.py' -vs`

## REST API task

Site https://www.food2fork.com/ isn't working so API is unavailable

## Problem solving task

Run in shell this command:

 `pipenv run python '.\Technical Knowledge\problem_solving.py'`