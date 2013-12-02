#!/usr/bin/env python
# coding=utf-8

import unittest
from Naked.toolshed.io import FileReader
from Naked.toolshed.io import FileWriter
from Naked.toolshed.ospaths import PathMaker


class NakedIOReadWriteTest(unittest.TestCase):

	def setUp(self):
		self.ascii_string = """This is a string
 & more string"""
		self.unicode_string = u"Hey! It's Bengali ব য,\nand here is some more ২"
		self.pm = PathMaker()
		self.ascii_path = self.pm.make_os_independent_path("testfiles", "ascii.txt")
		self.unicode_path = self.pm.make_os_independent_path("testfiles", "unicode.txt")
		self.bogus_path = self.pm.make_os_independent_path("testfiles", "bogus.txt")

	def tearDown(self):
		pass #remove the newly created files

	def test_file_ascii_string_readwrite(self):
		"""Test write and read of ascii file string"""
		FileWriter(self.ascii_path).write(self.ascii_string)
		ascii_file = FileReader(self.ascii_path).read()
		self.assertEqual(ascii_file, self.ascii_string)

	def test_file_unicode_string_readwrite(self):
		"""Test write and read of a unicode file string"""
		FileWriter(self.unicode_path).write(self.unicode_string)
		unicode_file = FileReader(self.unicode_path).read()
		self.assertEqual(unicode_file, self.unicode_string)

	def test_filereader_missing_file(self):
		"""Test that missing file throws SystemExit exception"""
		with self.assertRaises(SystemExit) as cm:
			FileReader(self.bogus_path).read()
			self.assertEqual(cm.exception.code, 1)




