import datetime
import time


def str2timstamp(timsstr: str):
    return int(time.mktime(datetime.datetime.strptime(timsstr, "%Y-%m-%d").timetuple()))
