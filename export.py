#!/usr/bin/env python3


from libraryClass import Solution


def export(solution: Solution, filename: str):
	file = open(filename + ".txt","w+")

	file.write(str(len(solution.scanned_books)))

	for library, books in solution.scanned_books:
		file.write(library + " " + len(book))

		for book in books:
			file.write(book.bookId() + " ")

	file.close()