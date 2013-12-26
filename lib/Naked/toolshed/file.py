#!/usr/bin/env python


import sys
import codecs

#------------------------------------------------------------------------------
# [ IO class ]
#  interface for all local file IO classes
#------------------------------------------------------------------------------
class IO:
	def __init__(self,filepath):
		self.filepath = filepath

#------------------------------------------------------------------------------
# [ FileWriter class ]
#  writes data to local files
#  methods: write_utf8(text)
#------------------------------------------------------------------------------
class FileWriter(IO):
	def __init__(self, filepath):
		IO.__init__(self, filepath)

	#------------------------------------------------------------------------------
	# [ write_utf8 method ]
	#   write to file with UTF-8 encoding
	#   uses filepath from class constructor
	#   requires text to passed as a method parameter
	#------------------------------------------------------------------------------
	def write_utf8(self, text):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='w')
		except IOError, ioe:
			pass
			## TODO : Handle missing file exception here
		try:
			f.write(text)
		except Exception as e:
			print("Unable to write to the file " + self.filepath)
			print((str(e)))
			sys.exit(1)
		finally:
			f.close()

#------------------------------------------------------------------------------
# [ FileReader class ]
#  reads data from local files
#  filename assigned in constructor (inherited from IO class interface)
#  methods: read_utf8(text)
#------------------------------------------------------------------------------
class FileReader(IO):
	def __init__(self, filepath):
		IO.__init__(self, filepath)

	#------------------------------------------------------------------------------
	# [ read_utf8 method ]
	#   read data from a file with UTF-8 encoding
	#   uses filepath from class constructor
	#   returns a string containing the file data
	#------------------------------------------------------------------------------
	def read_utf8(self):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='r')
		except IOError, ioe:
			pass
			## TODO: handle missing file exceptions here
		try:
			textstring = f.read()
			return textstring
		except Exception as e:
			print("Unable to read the file " + self.filepath)
			print((str(e)))
			sys.exit(1)
		finally:
			f.close()


if __name__ == '__main__':
	pass
