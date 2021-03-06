#!/usr/bin/env python3

from typing import *


class HashCode:
	timeLimit = 0
	numOfLibraries = 0
	libraries = []

	def check(self):
		return len(self.libraries) == numOfLibraries

	def addLibrary(self, lib):
		self.libraries.append(lib)

	def removeLib(self, lib):
		self.libraries.remove(lib)

	def getMostValuableLib(self):
		maxVal = 0
		maxLib = None
		for l in self.libraries:
			totalValue = l.getTotalValue
			if totalValue > maxVal:
				maxVal = totalValue
				maxLib = l

		return maxLib

	def removeBookFromEveryLibs(self, bookId):
		for l in self.libraries:
			l.removeBookFromId(bookId)

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

	def removeBookFromId(self, bookId):
		for b in self.books:
			if b.bookId == bookId:
				self.books.remove(b)

	def addBook(self, bookId, score):
		self.books.append(Book(bookId, score))

	def addBook(self, book):
		self.books.append(book)

	def removeBook(self, book):
		self.books.remove(book)

	def check(self):
		return len(self.books) == self.numOfBooks

	def getTotalValue(self):
		total = 0
		for b in self.books:
			total += int(b.score)
		return total

	def getAverageValue(self):
		return self.getTotalValue() / len(self.books)

	def getMostValuableBook(self):
		score = 0
		bookId = 0
		for b in self.books:
			if int(score) < int(b.score):
				score = b.score
				bookId = b.bookId
		return b

	"""
	_reverse == False : ascending
	_reverse == True : descending
	I guess
	"""
	def sort_books(self, _reverse: bool = False):
		return sorted(books, key=lambda book : book.bookId, reverse=_reverse)

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


class Solution:
	"""
	list[ { library_id: books } ]

	Example:
	[
		{
			0: [{Book 2}, {Book 3}]
		},
		{
			0: [{Book 1}, {Book 4}]
		},
		{
			1: [{Book 2}, {Book 3}]
			2: [{Book 5}]
			3: [{Book 2}, {Book 3}]
		},
		{
			2: [{Book 1}]
			3: [{Book 1}, {Book 2}, {Book 3}]
		}
	]
	"""
	time: List = []
	ellasped_time: int = 0
	scanned_books: Dict = {}


	def add_entry(self, day: dict):
		self.time[-1].append(day)

		for library_id, books in day:
			if library_id not in self.scanned_books:
				self.scanned_books[library_id] = [book.id for book in books]
			else:
				for book in books:
					if book.id not in self.scanned_books[library_id]:
						self.scanned_books[library_id].append(book.id)


	def next(self):
		self.ellasped_time += 1
		self.time.append({})


	def libraries(self):
		libraries: List = []

		for day in self.time:
			for library_id, books in day:
				libraries.append(library)

		return set(libraries)


	def cost(self) -> int:
		total_cost: int = 0

		for day in self.time:
			for library_id, books in day:
				for book in books:
					total_cost += book.score

		return total_cost


	def __init__(self):
		self.time.append({})