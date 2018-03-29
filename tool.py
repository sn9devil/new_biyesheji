import time

def now_time():
    localtime = time.localtime(time.time())
    mon = str(localtime.tm_mon)
    day = str(localtime.tm_mday)
    date = mon + '.' + day
    return date
