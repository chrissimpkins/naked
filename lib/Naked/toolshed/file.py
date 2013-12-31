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
#------------------------------------------------------------------------------
class FileWriter(IO):
	def __init__(self, filepath):
		IO.__init__(self, filepath)

	## TODO : tests for append method
	#------------------------------------------------------------------------------
	# [ append method ]
	#   Universal text file writer that appends to existing file using system default text encoding
	#------------------------------------------------------------------------------
	def append(self, text):
		try:
			with open(self.filepath, 'a') as appender:
				appender.write(text)
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to append text to the file with the append() method (Naked.toolshed.file.py).")
			raise e
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

	#------------------------------------------------------------------------------
	# [ write_bin method ]
	#   binary data file writer
	#------------------------------------------------------------------------------
	def write_bin(self, binary_data):
		try:
			with open(self.filepath, 'wb') as bin_writer:
				bin_writer.write(binary_data)
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to write binary data to file with the write_bin method (Naked.toolshed.file.py).")
			raise e

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

	## TODO: test for read_bin method
	#------------------------------------------------------------------------------
	# [ read_bin method ] (binary byte string)
	#   Universal binary data file reader
	#   returns file contents in binary mode as binary byte strings
	#------------------------------------------------------------------------------
	def read_bin(self):
		try:
			with open(self.filepath, 'rb') as bin_reader:
				data = bin_reader.read()
				return data
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read the binary data from the file with the read_bin method (Naked.toolshed.file.py).")
			raise e

	## TODO: tests for read_as
	#------------------------------------------------------------------------------
	# [ read_as method ] (string with developer specified text encoding)
	#   Text file reader with developer specified text encoding
	#   returns file contents in developer specified text encoding
	#------------------------------------------------------------------------------
	def read_as(self, dev_spec_encoding):
		try:
			with open(self.filepath, 'rt', encoding=dev_spec_encoding) as reader:
				data = reader.read()
				return data
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read the file with the developer specified text encoding with the read_as method (Naked.toolshed.file.py).")
			raise e

	## TODO: tests for readlines method
	#------------------------------------------------------------------------------
	# [ readlines method ] (list of strings)
	#   Read text from file line by line, uses default system text encoding
	#   returns list of file lines as strings
	#------------------------------------------------------------------------------
	def readlines(self):
		try:
			with open(self.filepath, 'rt') as reader:
				file_list = reader.readlines()
				return file_list
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read text from the requested file with the readlines() method (Naked.toolshed.file.py).")
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

	#------------------------------------------------------------------------------
	# FILE TEXT READER & MODIFIER METHODS
	#------------------------------------------------------------------------------

	## TODO: tests
	#------------------------------------------------------------------------------
	# [ read_with_function ] (string)
	#   read a text file and modify with a developer specified function that takes single parameter for the text in the file
	#   the developer's function should return the modified string
	#	returns a string that contains the modified file text
	#------------------------------------------------------------------------------
	def read_with_function(self, function):
		try:
			with open(self.filepath, 'rt') as read_data:
				modified_data = function(read_data)
			return modified_data
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read and modify file text with the read_with_function() method (Naked.toolshed.file.py).")
			raise e

	## TODO: tests
	#------------------------------------------------------------------------------
	# [ readlines_with_function ] (list of strings)
	#   read a text file by line, apply a developer specified function that takes single parameter for the line string to each line
	#   the developer's function should return the modified string
	#   returns a list containing each modified line string
	#------------------------------------------------------------------------------
	def readlines_with_function(self, function):
		try:
			with open(self.filepath, 'rt') as read_data:
				modified_text_list = []
				for line in read_data:
					modified_line = function(line)
					modified_text_list.append(modified_line)
				return modified_text_list
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to read and modify file text with the readlines_with_function() method (Naked.toolshed.file.py).")
			raise e


if __name__ == '__main__':
	pass
