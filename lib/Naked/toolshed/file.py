#!/usr/bin/env python


import sys
import codecs
from Naked.settings import debug as DEBUG_FLAG

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
#  methods: write(text), safe_write(text), write_utf8(text)
#------------------------------------------------------------------------------
class FileWriter(IO):
	def __init__(self, filepath):
		IO.__init__(self, filepath)

	## TODO : tests
	#------------------------------------------------------------------------------
	# [ write method ]
	#   Universal text file writer that uses system default text encoding
	#------------------------------------------------------------------------------
	def write(self,text):
		try:
			with open(self.filepath, 'wt') as writer:
				writer.write(text)
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to write to requested file with the write() method (Naked.toolshed.file.py).")
			raise e

	## TODO : tests
	#------------------------------------------------------------------------------
	# [ safe_write method ] (boolean)
	#   Universal text file writer (system default text encoding) that will NOT overwrite existing file at the requested filepath
	#   returns boolean indicator for success of write based upon test for existence of file
	#------------------------------------------------------------------------------
	def safe_write(self,text):
		try:
			import os.path
			if not os.path.exists(self.filepath):
				with open(self.filepath, 'wt') as writer:
					writer.write(text)
					return True
			else:
				return False
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to write to requested file with the safe_write() method (Naked.toolshed.file.py).")
			raise e

	#------------------------------------------------------------------------------
	# [ write_utf8 method ]
	#   Text file writer with explicit UTF-8 text encoding
	#   uses filepath from class constructor
	#   requires text to passed as a method parameter
	#------------------------------------------------------------------------------
	def write_utf8(self, text):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='w')
		except IOError, ioe:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to open file for write with the write_utf8() method (Naked.toolshed.file.py).")
			raise e
		try:
			f.write(text)
		except Exception as e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to write UTF-8 encoded text to file with the write_utf8() method (Naked.toolshed.file.py).")
			raise e
		finally:
			f.close()

#------------------------------------------------------------------------------
# [ FileReader class ]
#  reads data from local files
#  filename assigned in constructor (inherited from IO class interface)
#  methods: read(), read_utf8()
#------------------------------------------------------------------------------
class FileReader(IO):
	def __init__(self, filepath):
		IO.__init__(self, filepath)

	## TODO : tests
	#------------------------------------------------------------------------------
	# [ read method ] (string)
	#    Universal text file reader that uses the default system text encoding
	#    returns string that is encoded in the default system text encoding
	#------------------------------------------------------------------------------
	def read(self):
		try:
			with open(self.filepath, 'rt') as reader:
				data = reader.read()
				return data
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read text from the requested file with the read() method (Naked.toolshed.file.py).")
			raise e

	#------------------------------------------------------------------------------
	# [ read_utf8 method ] (string)
	#   read data from a file with explicit UTF-8 encoding
	#   uses filepath from class constructor
	#   returns a string containing the file data
	#------------------------------------------------------------------------------
	def read_utf8(self):
		try:
			f = codecs.open(self.filepath, encoding='utf-8', mode='r')
		except IOError, ioe:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to open file for read with read_utf8() method (Naked.toolshed.file.py).")
			raise ioe
		try:
			textstring = f.read()
			return textstring
		except Exception as e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read the file with UTF-8 encoding using the read_utf8() method (Naked.toolshed.file.py).")
			raise e
		finally:
			f.close()


if __name__ == '__main__':
	pass
