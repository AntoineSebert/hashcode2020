#!/usr/bin/env python3

from libraryClass import *

# actual scheduler

def scheduler(hashCode):
	# get the lib with the best cost function
	libsOrder = []
	libs = {} # {lib:[books]}
	for day in hashCode.timeLimit:
		daysLeft = timeLimit - day
		pass