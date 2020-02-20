#!/usr/bin/env python3

from libraryClass import Solution


def cost(state: Solution) -> int:
	total_cost: int = 0

	for library in state.libraries:
		for book in library.books:
			total_cost += book.score

	return total_cost


# actual scheduler