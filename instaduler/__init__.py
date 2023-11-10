import os

from logging_service import LoggingService

_datetimestr: str = None


def newdatetimestr() -> str:
    global _datetimestr
    _datetimestr = get_datetimestr()
    return get_datetimestr()


def get_datetimestr() -> str:
    if _datetimestr == None:
        newdatetimestr()
    return _datetimestr


def newlogfile():
    folder = 'logs'
    if not os.path.exists(folder):
        os.makedirs(folder)
    LoggingService().log_file = os.path.join(folder, f'{get_datetimestr()}.txt')
