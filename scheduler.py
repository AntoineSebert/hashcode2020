#!/usr/bin/env python3

from libraryClass import Solution


def cost(state: Solution) -> int:
	total_cost: int = 0

	for library in state.libraries:
		for book in library.books:
			total_cost += book.score

	return total_cost


# actual scheduler

class scheduler:
	hashCode = None
	scanningLibs = []

	toScan = {}

	def addToScan(self, libId, books):
		self.scanningLibs.append(libId)
		self.toScan[libId] = books

	def getSubmissionFile(self):
		output = f"{len(scanningLibs)}\n"

		for libs in self.scanningLibs:
			output += f"{libs} {len(self.toScan[libs])}\n"
			for book in self.toScan[libs]:
				output += f"{book} "
		return output

	def compute(self):
		pass

	def __init__(self, hashCode):
		self.hashCode = hashCode
