#!/usr/bin/env python3


class HashCode:
	timeLimit = 0
	numOfLibraries = 0
	libraries = []

	def check(self):
		return len(libraries) == numOfLibraries

	def addLibrary(self, lib):
		self.libraries.append(lib)

	def removeBookFromEveryLibs(self, bookId):
		for l in self.libraries:
			l.removeBook(bookId)

	def __str__(self):
		output = f"Time limit = {self.timeLimit}"
		for l in self.libraries:
			output += str(l) + "\n"
		return output

	def __init__(self, numOfLibraries):
		self.numOfLibraries = numOfLibraries
	

class LibraryClass:
	timeToSignup = 0
	books = []
	numOfBooks = 0
	maxBooksPerDay = 0
	libId = 0

	def removeBook(self, bookId):
		for b in self.books:
			if b.bookId == bookId:
				self.books.remove(b)

	def addBook(self, bookId, score):
		self.books.append(Book(bookId, score))

	def addBook(self, book):
		self.books.append(book)

	def check(self):
		return len(self.books) == self.numOfBooks
	
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

	def __str__(self):
		books = ""
		for b in self.books:
			books += str(b)
		return f"Id :{self.libId}, time: {self.libId}, max/day: {self.maxBooksPerDay} -> " + books

	def __init__(self, numOfBooks, libId, timeToSignup, maxBooksPerDay):
		self.numOfBooks = numOfBooks
		self.libId = libId
		self.timeToSignup = timeToSignup
		self.maxBooksPerDay = maxBooksPerDay


class Book:
	bookId = 0
	score = 0

	def __str__(self):
		return f"({self.bookId}:{self.score})"

	def __init__(self, bookId, score):
		self.bookId = bookId
		self.score = score