
from bookify import *
from export import export
from scheduler import scheduler

if __name__ == "__main__":
	p = Parser()
	hashcode = p.parse('data/a_example.txt')

	order, scanning = scheduler(hashcode)

	export(order, scanning, "test")