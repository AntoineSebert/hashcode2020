
from bookify import *
from export import export
from scheduler import scheduler

if __name__ == "__main__":
	p = Parser()
	hashcode = p.parse('data/b_read_on.txt')

	order, scanning = scheduler(hashcode)

	export(order, scanning, "test")