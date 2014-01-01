#!/usr/bin/env python
# coding=utf-8

import unittest
import os
import Naked.toolshed.system as system
from Naked.toolshed.file import FileWriter
from Naked.toolshed.system import make_path

class NakedSystemTest(unittest.TestCase):
	def setUp(self):
		self.sysfilepath = make_path("testfiles", "testdir", "systest.txt")
		self.sysdirpath = make_path("testfiles", "testdir")
		self.bogusfilepath = make_path("testfiles", "testdir", "bogusfile.text")
		FileWriter(self.sysfilepath).write("test")

	def tearDown(self):
		pass

	#------------------------------------------------------------------------------
	# FILE & DIRECTORY PATH & NAME TESTS
	#------------------------------------------------------------------------------

	def test_sys_make_filepath(self):
		"""Test that correct OS independent file path is created"""
		naked_path = make_path("testfiles", "testdir", "systest.txt")
		python_path = os.path.join("testfiles", "testdir", "systest.txt")
		self.assertEqual(naked_path, python_path)

	def test_sys_filename(self):
		"""Test that correct base file name returned from a filepath"""
		filename = system.filename(self.sysfilepath)
		self.assertEqual(filename, "systest.txt")

	def test_sys_file_extension(self):
		"""Test that correct file extension is returned"""
		file_ext = system.file_extension(self.sysfilepath)
		self.assertEqual(file_ext, ".txt")

	def test_sys_dir_path(self):
		"""Test that correct directory path to file is returned"""
		dir_path = system.directory(self.sysfilepath)
		self.assertEqual(dir_path, os.path.join("testfiles", "testdir"))

	def test_sys_full_path_to_file(self):
		"""Test that full path to file in cwd is returned"""
		file_path = system.fullpath("test_SYSTEM.py")
		self.assertEqual(file_path, os.path.join(os.getcwd(),"test_SYSTEM.py"))

	def test_sys_cwd_path(self):
		"""Test that full path to the cwd is returned"""
		cwd_path = system.cwd()
		self.assertEqual(cwd_path, os.getcwd())

	#------------------------------------------------------------------------------
	# FILE TESTS
	#------------------------------------------------------------------------------

	def test_sys_file_exists(self):
		"""Test for existence of a file that exists"""
		filepath = make_path("testfiles", "testdir", "systest.txt")
		self.assertEqual(True, system.file_exists(filepath))

	def test_sys_file_exists_missing_file(self):
		"""Test for existence of a file that does not exist"""
		self.assertEqual(False, system.file_exists(self.bogusfilepath))

	def test_syst_is_file(self):
		"""Test that a path is a file when it is a file"""
		self.assertEqual(True, system.is_file(self.sysfilepath))

	def test_sys_is_file_missing_file(self):
		"""Test that a path is not a file when it is not a file"""
		self.assertEqual(False, system.is_file(self.bogusfilepath))

	def test_sys_is_file_when_dir(self):
		"""Test that a path is not a file when it is a directory"""
		self.assertEqual(False, system.is_file(self.sysdirpath))


	#------------------------------------------------------------------------------
	# DIRECTORY TESTS
	#------------------------------------------------------------------------------
	def test_sys_dir_exists(self):
		"""Test for existence of a directory that exists"""
		self.assertEqual(True, system.dir_exists(self.sysdirpath))

	def test_sys_dir_exists_missing_dir(self):
		"""Test for existence of a directory that does not exist"""
		self.assertEqual(False, system.dir_exists(os.path.join("bogusdir", "anotherdir")))

	def test_sys_dir_is_dir(self):
		"""Test whether a path is a directory when it is a directory"""
		self.assertEqual(True, system.is_dir(self.sysdirpath))

	def test_sys_dir_is_dir_when_file(self):
		"""Test whether a path is a directory when it is a file"""
		self.assertEqual(False, system.is_dir(self.sysfilepath))

	def test_sys_dir_is_dir_when_missing(self):
		"""Test whether a path is a directory when it is missing"""
		self.assertEqual(False, system.is_dir(os.path.join("bogusdir", "anotherdir")))


	#------------------------------------------------------------------------------
	# DECORATOR TESTS
	#------------------------------------------------------------------------------
	def test_sys_add_currentdir_path_to_basefile(self):
		"""Test decorator addition of cwd path to base filename in first argument of decorated function"""
		@system.currentdir_to_basefile
		def path_returner(file_name):
			return file_name

		the_path = path_returner("test_SYSTEM.py")
		self.assertEqual(the_path, os.path.join(os.getcwd(), "test_SYSTEM.py"))

	def test_sys_add_currentdir_path_first_arg(self):
		"""Test decorator addition of cwd path as first argument of decorated function"""
		@system.currentdir_firstargument
		def path_returner(dir):
			return dir

		the_dir = path_returner()
		self.assertEqual(the_dir, os.getcwd())

	def test_sys_add_currentdir_last_arg(self):
		"""Test decorator addition of cwd path as last argument of decorated function"""
		@system.currentdir_lastargument
		def path_returner(bogus_param, current_dir=""):
			return current_dir

		the_dir = path_returner("bogus")
		self.assertEqual(the_dir, os.getcwd())

