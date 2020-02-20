#!/usr/bin/env python3


class HashCode:
	timeLimit = 0
	libraries = []
	

class LibraryClass:
	books = []
	numOfBooks = 0
	libId = 0

	def addBook(self, bookId, score):
		self.books.append(Book(bookId, score))

	def check(self):
		return len(books) == numOfBooks
	
	def __init__(self, numOfBooks, libId):
		self.numOfBooks = numOfBooks


class Book:
	bookId = 0
	score = 0

	def __init__(self, bookId, score):
		self.bookId = bookId
		self.score = score