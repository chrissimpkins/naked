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
		self.ascii_path = make_path("testfiles", "ascii.txt")
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

	def test_file_ascii_readwrite_missing_file(self):
		"""Test that missing ascii file throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read()

	def test_file_ascii_readwrite_append(self):
		"""Test append of ascii text to existing file"""
		FileWriter(self.ascii_path).append(self.ascii_string) #append a second string of the ascii text
		ascii_text = FileReader(self.ascii_path).read()
		self.assertEqual(ascii_text, (self.ascii_string)*2) #confirm that it equals two of the ascii strings

	def test_file_ascii_readwrite_append_missingfile(self):
		"""Test append of ascii text raises IOError when file missing"""
		with (self.assertRaises(IOError)):
			FileWriter(self.bogus_path).append(self.ascii_string)

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

	def test_file_utf8_readwrite_missing_file(self):
		"""Test that missing utf-8 file throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_utf8()

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



