#!/usr/bin/env python3


class HashCode:
	timeLimit = 0
	numOfLibraries = 0
	libraries = []

	def check(self):
		return len(libraries) == numOfLibraries

	def addLibrary(self, lib):
		self.libraries.append(lib)

	def __init__(self, numOfLibraries):
		self.numOfLibraries = numOfLibraries
	

class LibraryClass:
	timeToSignup = 0
	books = []
	numOfBooks = 0
	libId = 0

	def addBook(self, bookId, score):
		self.books.append(Book(bookId, score))

	def check(self):
		return len(self.books) == self.numOfBooks
	
	def __init__(self, numOfBooks, libId, timeToSignup):
		self.numOfBooks = numOfBooks
		self.libId = libId
		self.timeToSignup = timeToSignup

	def getTotalValue(self):
		total = 0
		for b in self.books:
			total += b.score
		return total

	def getMostValuable(self):
		score = 0
		bookId = 0
		for b in self.books:
			if score < b.score:
				score = b.score
				bookId = b.bookId
		return bookId, score


class Book:
	bookId = 0
	score = 0

	def __init__(self, bookId, score):
		self.bookId = bookId
		self.score = score