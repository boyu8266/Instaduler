# Instaduler
A scheduling script that integrates with Instagrapi, using JSON file as a simple database for pending posts.
- [Instaduler](#instaduler)
  - [Commands](#commands)
  - [How to](#how-to)
    - [Install](#install)
    - [Login](#login)
    - [Schedule](#schedule)
  - [Todo](#todo)



## Commands
```
usage: __main__.py [-h] {login,post,run} ...

Login and Post operations

positional arguments:
  {login,post,run}  Action to perform
    login           Perform login operation
    post            Perform post operation
    run             Run Schedule Post

options:
  -h, --help        show this help message and exit
```



## How to
### Install
1. Open your terminal.
2. (Optional) Activate a virtual environment, e.g., conda, pyenv, ...
3. Run `pip install -r requirements.txt` to install dependencies.
4. Run `python setup.py install`.
### Login
1. Open your terminal.
2. Activate a virtual environment (if available).
3. Run `instaduler login --user=xxx --psw=xxx`.
### Schedule
1. Open your terminal.
2. Activate a virtual environment (if available).
3. Run `instaduler post --folder=xxx --text=xxx`.

## Todo
| Item          | Status | Open       | Close      |
|---------------|--------|------------|------------|
| Support Album | Doing  | 2023/10/05 | 2023/10/05 |
| Support Reels | Todo   | 2023/10/05 |            |