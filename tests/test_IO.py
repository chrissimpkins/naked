                #!/usr/bin/env python
# coding=utf-8

import unittest
import os
from Naked.toolshed.file import FileReader
from Naked.toolshed.file import FileWriter
from Naked.toolshed.system import make_path


class NakedIOReadWriteTest(unittest.TestCase):

	def setUp(self):
		self.ascii_string = """This is a string
 & more string"""
		self.unicode_string = u"Hey! It's Bengali ব য,\nand here is some more ২"
		self.ascii_string = "Check it! This is ascii text!"
		self.latin_string = "grégory"
		self.binary_string = b"This is a binary string"
		self.multiline_string = "This is line 1\nThis is line 2"
		self.multiline_list = ["This is line 1\n", "This is line 2"]
		self.mod_multi_list = ["AThis is line 1\n", "AThis is line 2"]
		self.mod_uni_multi_list = [u"AHey! It's Bengali ব য,\n", u"Aand here is some more ২"]
		self.ascii_path = make_path("testfiles", "ascii.txt")
		self.binary_path = make_path("testfiles", "binary.bin")
		self.multiline_path = make_path("testfiles", "multi.txt")
		self.unicode_path = make_path("testfiles", "unicode.txt")
		self.unicode2_path = make_path("testfiles", "unicode2.txt")
		self.utfsixteen_path = make_path("testfiles", "sixteen.txt")
		self.latin_path = make_path("testfiles", "latin.txt")
		self.bogus_path = make_path("testfiles", "bogus.txt")

	def tearDown(self):
		pass

    #------------------------------------------------------------------------------
    # ASCII read & write file tests
    #------------------------------------------------------------------------------
	def test_file_ascii_readwrite(self):
		"""Test write and read of ascii encoded file"""
		FileWriter(self.ascii_path).write(self.ascii_string) # file write
		ascii_text = FileReader(self.ascii_path).read() # file read
		self.assertEqual(ascii_text, self.ascii_string)

	def test_file_ascii_readwrite_append(self):
		"""Test append of ascii text to existing file"""
		FileWriter(self.ascii_path).append(self.ascii_string) #append a second string of the ascii text
		ascii_text = FileReader(self.ascii_path).read()
		self.assertEqual(ascii_text, (self.ascii_string)*2) #confirm that it equals two of the ascii strings

	def test_file_ascii_safewrite(self):
		"""Test safe_write() to confirm does not overwrite existing file"""
		os.remove(self.ascii_path) #remove the existing text file for tests
		if os.path.exists(self.ascii_path):
			raise IOError("The ascii test file was not deleted. (test_IO.py.test_file_ascii_safewrite)")
		else:
			safe_response = FileWriter(self.ascii_path).safe_write(self.ascii_string) # attempt safe_write when no preexisting file present
			ascii_text = FileReader(self.ascii_path).read()
			self.assertEqual(ascii_text, self.ascii_string) # assert that the correct text was written
			self.assertEqual(safe_response, True) # assert that returns True when file not present and writes

			if os.path.exists(self.ascii_path):
					self.assertEqual(FileWriter(self.ascii_path).safe_write(self.ascii_string), False) #confirm that returns False to calling function when there is a pre-existing file
			else:
				raise IOError("The ascii test file is not present (test_IO.py.test_file_ascii_safewrite)")


	#------------------------------------------------------------------------------
	# UTF-8 file tests
	#------------------------------------------------------------------------------
	def test_file_utf8_readwrite(self):
		"""Test write and read of a utf-8 encoded file"""
		FileWriter(self.unicode_path).write_utf8(self.unicode_string)
		unicode_text = FileReader(self.unicode_path).read_utf8()
		self.assertEqual(unicode_text, self.unicode_string)

	def test_file_utf8_readas_writeas(self):
		"""Test read_as & write_as with utf-8 encoding"""
		FileWriter(self.unicode2_path).write_as(self.unicode_string, "utf-8")
		unicode_text = FileReader(self.unicode2_path).read_as("utf-8")
		self.assertEqual(unicode_text, self.unicode_string)

	def test_file_utf8_readwrite_append(self):
		FileWriter(self.unicode_path).append_utf8(self.unicode_string)
		unicode_text = FileReader(self.unicode_path).read_utf8()
		self.assertEqual(unicode_text, (self.unicode_string*2))

	def test_file_utf8_write_raises_unicodeerror(self):
		"""Test write of a utf-8 encoded file with write method raises UnicodeEncodeError"""
		with (self.assertRaises(UnicodeEncodeError)):
			FileWriter(self.unicode_path).write(self.unicode_string)

	def test_file_utf8_readwrite_raises_unicodeerror(self):
		"""Test read of utf-8 encoded file with read method & attempt to encode as utf-8 raises exception"""
		with (self.assertRaises(UnicodeDecodeError)):
			FileWriter(self.unicode_path).write_utf8(self.unicode_string)
			unicode_text = FileReader(self.unicode_path).read()
			encoded_text = unicode_text.encode("utf-8")

	#------------------------------------------------------------------------------
	# BINARY DATA tests
	#------------------------------------------------------------------------------
	def test_file_bin_readwrite(self):
		"""Test read and write of binary data"""
		FileWriter(self.binary_path).write_bin(self.binary_string)
		bin_data = FileReader(self.binary_path).read_bin()
		self.assertEqual(bin_data, self.binary_string)

	#------------------------------------------------------------------------------
	# LINE READS
	#------------------------------------------------------------------------------
	def test_file_readlines(self):
		"""Test line reads with readlines"""
		FileWriter(self.multiline_path).write(self.multiline_string)
		line_list = FileReader(self.multiline_path).readlines()
		self.assertEqual(line_list, self.multiline_list)

	#------------------------------------------------------------------------------
	# FILE COMPRESSION tests
	#------------------------------------------------------------------------------
	def test_file_gzip_ascii_readwrite(self):
		"""Test gzip compression and read from compressed ascii text file"""
		FileWriter(self.ascii_path).gzip(self.ascii_string)
		gzip_contents = FileReader(self.ascii_path + ".gz").read_gzip()
		self.assertEqual(gzip_contents, self.ascii_string)

	def test_file_gzip_utf8_readwrite(self):
		"""Test gzip compression and read from compressed unicode text file without explicit utf-8 decode"""
		FileWriter(self.unicode_path).gzip(self.unicode_string)
		gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip() # when read without explicit utf-8 decoding, the strings will not match
		self.assertNotEqual(gzip_contents, self.unicode_string)

	def test_file_gzip_utf8_readwrite_explicit_decode(self):
		"""Test gzip compression and read from compressed unicode text file with explicit utf-8 decode"""
		FileWriter(self.unicode_path).gzip(self.unicode_string)
		gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip("utf-8") # when read with explicit utf-8 decoding, strings should match
		self.assertEqual(gzip_contents, self.unicode_string)

	#------------------------------------------------------------------------------
	# FILE READER + MODIFIER function tests
	#------------------------------------------------------------------------------
	def test_file_read_apply_function(self):
		"""Test apply function to text read from file with read_apply_function"""
		def add_a_char(text):
			mod_text = "A" + text
			return mod_text
		FileWriter(self.ascii_path).write(self.ascii_string)
		func_text = FileReader(self.ascii_path).read_apply_function(add_a_char)
		self.assertEqual(func_text, ("A" + self.ascii_string))

	def test_file_read_apply_function_unicode(self):
		"""Test apply function to unicode text read from file with read_apply_function"""
		def add_a_char(text):
			mod_text = "A" + text
			return mod_text
		FileWriter(self.unicode_path).write_utf8(self.unicode_string)
		func_text = FileReader(self.unicode_path).read_apply_function(add_a_char)
		decoded_text = func_text.decode("utf-8") # have to decode binary string as utf-8 if the original file contained unicode
		self.assertEqual(decoded_text, ("A" + self.unicode_string))

	def test_file_readlines_apply_function(self):
		"""Test apply function to each line of a file with readlines_apply_function"""
		def add_a_char(text):
			mod_text = "A" + text
			return mod_text
		FileWriter(self.multiline_path).write(self.multiline_string)
		file_line_list = FileReader(self.multiline_path).readlines_apply_function(add_a_char)
		self.assertEqual(file_line_list, self.mod_multi_list)

	def test_file_readlines_apply_function_unicode(self):
		"""Test apply function to each line of a file with readlines_apply_function on unicode file"""
		def add_a_char(text):
			mod_text = "A" + text
			return mod_text
		FileWriter(self.unicode_path).write_utf8(self.unicode_string)
		file_line_list = FileReader(self.unicode_path).readlines_apply_function(add_a_char)
		decoded_list = []
		for line in file_line_list:
			decoded_line = line.decode("utf-8")
			decoded_list.append(decoded_line)
		self.assertEqual(decoded_list, self.mod_uni_multi_list)
	#------------------------------------------------------------------------------
	# MISSING FILE tests
	#------------------------------------------------------------------------------
	def test_file_read_missing_file(self):
		"""Test that missing file to read() throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read()

	def test_file_readas_missing_file(self):
		"""Test that missing file to read_as() throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_as("utf-8")

	def test_file_read_gzip_missing_file(self):
		"""Test that missing file to read_gzip() throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_gzip()

	def test_file_read_utf8_missing_file(self):
		"""Test that missing file to read_utf8 throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_utf8()

	def test_file_append_missing_file(self):
		"""Test append of ascii text raises IOError when file missing"""
		with (self.assertRaises(IOError)):
			FileWriter(self.bogus_path).append(self.ascii_string)

	def test_file_append_utf8_missing_file(self):
		"""Test append of unicode text raises IOError when file missing"""
		with (self.assertRaises(IOError)):
			FileWriter(self.bogus_path).append_utf8(self.unicode_string)

	def test_file_read_bin_missing_file(self):
		"""Test read_bin raises IOError when file is missing"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_bin()

	def test_file_readlines_missing_file(self):
		"""Test readlines raises IOError when file is missing"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).readlines()

