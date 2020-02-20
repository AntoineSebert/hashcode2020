from libraryClass import *

class Parser:


	def __init__(self, filename='data/a_example.txt'):
		self.filename = filename
		self.hashcode = None


	def parse(self, filename):

		with open(filename) as f:
			data = f.readlines()		# each element in data is line from input file


		# read in header info

		header = data[0].split(' ') 	#	read first line into books, libraries, days
		timeLimit = header[2]			# set days
		numOfLibraries = header[1]		# set num libraries

		bookdata = data[1].split(' ')	# book scores


		## build up library list
		libraries = []

		for i in range(2, len(data), 2):


			library = data[i].split(' ')
			numOfBooks = library[0]
			timeToSignup = library[1]
			maxBooksPerDay = library[2]

			bookline = data[i+1].split(' ')
			librarybooks = []

			## build book objects for given library
			for id in range(len(bookline)):
				book = Book(bookline[id], bookdata[int(bookline[id])])
				librarybooks.append(book)

			libId = (i-2)

			# libraryclass init : def __init__(self, numOfBooks, libId, timeToSignup, maxBooksPerDay):

			lib = LibraryClass(numOfBooks, libId, timeToSignup, maxBooksPerDay)
			lib.books = librarybooks

			libraries.append(lib)



		# 	def __init__(self, numOfLibraries):
		hashcode = HashCode(numOfLibraries)
		hashcode.timeLimit = int(timeLimit)
		hashcode.libraries = libraries

		self.hashcode = hashcode

		return self.hashcode



"""
if __name__ == "__main__":
	parser = Parser()
	hashcode = parser.parse(parser.filename)
	print(hashcode.libraries[0].numOfBooks)
	print(hashcode.libraries[0].timeToSignup)
	print(hashcode.libraries[0].maxBooksPerDay)
	for i in hashcode.libraries[1].books:
		print(str(i.bookId)+' '+str(i.score))
	#print(hashcode.check())
"""