                #!/usr/bin/env python
# coding=utf-8

import unittest
import os
from Naked.toolshed.file import FileReader
from Naked.toolshed.file import FileWriter
from Naked.toolshed.ospaths import PathMaker


class NakedIOReadWriteTest(unittest.TestCase):

	def setUp(self):
		self.ascii_string = """This is a string
 & more string"""
		self.unicode_string = u"Hey! It's Bengali ব য,\nand here is some more ২"
		self.ascii_string = "Check it! This is ascii text!"
		self.pm = PathMaker()
		self.ascii_path = self.pm.make_os_independent_path("testfiles", "ascii.txt")
		self.unicode_path = self.pm.make_os_independent_path("testfiles", "unicode.txt")
		self.bogus_path = self.pm.make_os_independent_path("testfiles", "bogus.txt")

	def tearDown(self):
		pass

    #------------------------------------------------------------------------------
    # ASCII file tests
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

	def test_file_utf8_readwrite_missing_file(self):
		"""Test that missing utf-8 file throws IOError"""
		with (self.assertRaises(IOError)):
			FileReader(self.bogus_path).read_utf8()




