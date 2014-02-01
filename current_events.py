#!/usr/bin/python

from datetime import datetime
from os import system
import feedparser

now = datetime.now()

def current_events(now):
	cnn = {}
	cnn = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')

	entries = {}
	entries = cnn['entries']

	cnn_topstories = []

	system('say The top news stories for today are: ')

	count = 0
	for story in entries[:5]:
		system('say %s' %story['title'])
		count += 1

def bbc_podcast(now):
	system('say Would you like to hear the latest BBC Podcast?')
	bbc_answer = raw_input("")

	if (bbc_answer == 'yes'):
		system('great. Opening up to the bbc now')
	else:
		return 0