#!/usr/bin/python

import time
from datetime import datetime
from dateutil import tz
from os import system

def greeting(now):

    #Time-zone Definitions
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
 
    #Time-zone Switching
    now_UTC = now.replace(tzinfo=from_zone)
    now_EST = now_UTC.astimezone(to_zone)
    
    #Jarvis Time Output Definitions
    weekday = time.strftime("%A")
    month = time.strftime("%B")
    hour = time.strftime("%X")

    if now_UTC.hour < 12:
        system('say Good morning Jisha! Today is %s, %s %s, and the current time is %s.' % (weekday, month, now.day, hour))
    elif now_UTC.hour >= 12 and now_UTC.hour < 16:
        system('say Good afternoon Jisha! Today is %s, %s %s, and the current time is %s.' % (weekday, month, now.day, hour))
    else:
        system('say Good evening Jisha! Today is %s, %s %s, and the current time is %s.' % (weekday, month, now.day, hour))
