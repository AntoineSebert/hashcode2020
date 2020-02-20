#!/usr/bin/env python3


from libraryClass import Solution


def export(order, scanning, filename: str):
	file = open(filename + ".txt", "w+")

	print(order)
	print(scanning)

	file.write(str(len(order)))

	for library_id in order:
		file.write(str(library_id) + " " + str(len(scanning[library_id])) + "\n")

		for book in scanning[library_id]:
			file.write(str(book) + " ")

	file.close()