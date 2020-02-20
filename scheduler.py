#!/usr/bin/env python3

from libraryClass import *

def getBestLibToSignUp(hashCode, daysLeft):
	bestScore = 0
	bestLib = object()

	for lib in hashCode.libraries:
		worthiness = lib.getAverageValue() * (daysLeft - int(lib.timeToSignup)) * int(lib.maxBooksPerDay)
		if bestScore < worthiness:
			bestScore = worthiness
			bestLib = lib

	return bestLib


def scheduler(hashCode):
	# get the lib with the best cost function
	libsOrder = []
	libs = {} # {lib:[books]}
	signing = 0
	libReady = -1
	for day in range(hashCode.timeLimit):
		daysLeft = hashCode.timeLimit - day
		if signing <= 0 and len(hashCode.libraries) > 0:
			libReady += 1
			library = getBestLibToSignUp(hashCode, daysLeft)
			libsOrder.append(library)
			libs[library.libId] = []
			hashCode.removeLib(library)
			signing = int(library.timeToSignup)

		for i in range(libReady):
			book = libsOrder[i].getMostValuableBook()
			libs[libsOrder[i].libId].append(int(book.bookId))
			hashCode.removeBookFromEveryLibs(book.bookId)
			for l in libsOrder:
				l.removeBookFromId(book.bookId)

		signing -= 1


	libOutput = [int(l.libId) for l in libsOrder]
	return (libOutput, libs)
