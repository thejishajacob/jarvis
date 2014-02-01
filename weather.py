#!/usr/bin/python

import pywapi
import string
from os import system

weather_result = pywapi.get_weather_from_weather_com('10001')

def weather(weather_result):
    system('say The weather in New York is reported as %s. It is %s degrees celsius.' %(weather_result['current_conditions']['text'], weather_result['current_conditions']['temperature']))