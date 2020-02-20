#!/usr/bin/env python3

from libraryClass import *

# actual scheduler

def getBestLibToSignUp(hashCode, daysLeft):
	bestScore = 0
	bestLib = None
	for lib in hashCode.libraries:
		worthiness = lib.getAverageValue() * (daysLeft - lib.timeToSignup) * lib.maxBooksPerDay
		if bestScore < worthiness:
			bestScore = worthiness
			bestLib = lib
	return lib


def scheduler(hashCode):
	# get the lib with the best cost function
	libsOrder = []
	libs = {} # {lib:[books]}
	signing = 0
	libReady = -1 
	for day in hashCode.timeLimit:
		daysLeft = timeLimit - day
		if signing <= 0:
			libReady += 1
			library = getBestLibToSignUp(hashCode, daysLeft)
			libsOrder.append(library)
			libs[library.libId] = []
			hashCode.removeLib(library)
			signing = library.timeToSignup

		for i in range(libReady):
			book = libsOrder[i].getMostValuableBook()
			libs[libsOrder[i].libId].append(book.bookId)
			hashCode.removeBookFromEveryLibs(book.bookId)
			for l in libsOrder:
				l.removeBookFromId(book.bookId)

		signing -= 1

	libOutput = [l.libId for l in libsOrder]
	
	return (libOutput, libs)
