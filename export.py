#!/usr/bin/env python3


def export(result: Solution, filename: str):
	file = open(filename + ".txt","w+")

	file.write(result.libraries.length())

	for library in result.libraries:
		file.write(library.id() + " " + library.books.length())

	for book in library.books:
		file.write(book.bookId() + " ")

	file.close()