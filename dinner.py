#!/usr/bin/python

import time
from datetime import datetime
from dateutil import tz
from os import system

def dinner(now):
	system('say Have you had dinner?')
	eaten = raw_input("")

	if (eaten == 'no'):
		system('say What would you like?')
	else:
		return 0