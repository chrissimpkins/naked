#!/usr/bin/env python

# interface for IO classes, sets the filepath in constructor
class IO:
	def __init__(self,filepath):
		self.filepath = filepath

# file writer class
class FileWriter(IO):
	def write(self, text):
		pass

# file reader class
class FileReader(IO):
	def read(self):
		pass

# read remote git repositories
class GitCloner(IO):
	pass

if __name__ == '__main__':
	pass
