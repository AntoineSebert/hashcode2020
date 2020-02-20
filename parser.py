#!/usr/bin/env python3
import sys
import argparse
import LibraryClass
import HashCode
import Book


def readFile(file)


	with open(file) as f:
		data = f.readlines()		# each element in data is line from input file


	# read in header info

	header = data[0].split(' ') 	#	read first line into books, libraries, days
	timeLimit = header[2]			# set days
	numOfLibraries = header[1]		# set num libraries 

	

	## build up library list
	libraries = []

	for i in range(2, len(data), 2):


		library = data[i].split(' ')
		numOfBooks = library[0]
		timeToSignup = library[1]
		maxBooksPerDay = library[2]

		bookline = data[i+1].split(' ')
		librarybooks = []

		## build book objects for given library
		for id in bookline
			book = Book(id,bookline[id])
			librarybooks.append(book)

		libId = (i-2)

		# libraryclass init : def __init__(self, numOfBooks, libId, timeToSignup, maxBooksPerDay):
		
		lib = LibraryClass(numOfBooks, libId, timeToSignup, maxBooksPerDay)
		lib.books = librarybooks

		libraries.append(lib)


	
	# 	def __init__(self, numOfLibraries):
	hashcode = HashCode(numOfLibraries)
	hashcode.timeLimit = timeLimit
	hashcode.libraries = libraries


	return hashcode



