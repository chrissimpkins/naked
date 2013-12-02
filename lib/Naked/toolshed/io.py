#!/usr/bin/env python


import sys
import codecs

# interface for IO classes, sets the filepath in constructor
class IO:
	def __init__(self,filepath):
		self.filepath = filepath

# file writer class
#    - inherits IO class
## Usage: FileWriter(filepath).write(textstring)
## exits with status 1 on failure and handles exceptions with message to user
class FileWriter(IO):
	def write(self, text):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='w')
			f.write(text)
			f.close()
		except Exception as e:
			print("Unable to write to the file " + self.filepath)
			print((str(e)))
			sys.exit(1)

# file reader class
#   - inherits IO class
## Usage: FileReader(filepath).read()
## returns string from the file and exits with status 1 on failure, handles exceptions with message to user
class FileReader(IO):
	def read(self):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='r')
			textstring = f.read()
			f.close()
			return textstring
		except Exception as e:
			print("Unable to read the file " + self.filepath)
			print((str(e)))
			sys.exit(1)

# read remote git repositories
class GitCloner(IO):
	pass


if __name__ == '__main__':
	pass
