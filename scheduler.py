#!/usr/bin/env python3

from libraryClass import *

# actual scheduler

def scheduler(hashCode):
	# get the lib with the most valuable books first
	libsOrder = []
	libs = {} # {lib:[books]}
	for day in hashCode.timeLimit:
		daysLeft = timeLimit - day
		lib