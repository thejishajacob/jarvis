#!/usr/bin/python

#General Libraries
from datetime import datetime
from os import system
import pywapi
import feedparser

#Jarvis Specific Libraries
from greeting import greeting
from weather import weather
from coffee import coffee
from dinner import dinner
from current_events import current_events, bbc_podcast


now = datetime.now()
weather_result = pywapi.get_weather_from_weather_com('10001')
period = now.strftime("%p")

def main():
    
    if period == 'AM':
        greeting(now);
        weather(weather_result);
        current_events(now);
        coffee(now);
        bbc_podcast(now);
    else:
        greeting(now);
        weather(weather_result);
        current_events(now);
        dinner(now);

if __name__ == "__main__":
    main()