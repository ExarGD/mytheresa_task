# Setup

## Windows:

1. Install Python 3 https://www.python.org/downloads/

2. Clone repository `git clone git@github.com:ExarGD/mytheresa_task.git`

3. Download ChromeDriver from here https://sites.google.com/a/chromium.org/chromedriver/downloads

4. Place ChromeDriver executable in repository Technical Knowledge folder (if it's not there)

5. Install pipenv `pip3 install pipenv`

6. `$env:PIPENV_VENV_IN_PROJECT="enabled"` for Powershell and `set PIPENV_VENV_IN_PROJECT="enabled"` for CMD (this is needed to create virtualenv directory locally for easier deletion)

7. Go to repository folder

8. `pipenv --python 3`

9. `pipenv install`