#!/usr/bin/env python

import unittest
import Naked.commandline

class NakedCommandTest(unittest.TestCase):

	def setUp(self):
		self.cl_argv = ["naked", "nakedtest", "testcmd2", "-s", "--long", "-f", "arg1", "--flag2", "arg2", "lparg"]
		self.test_argv = self.cl_argv[1:]
		self.cmd_obj = Naked.commandline.Command(self.cl_argv[0], self.test_argv)

	# Command Object Tests
	def test_command_string(self):
		"""Test the command string arguments used for testing"""
		self.assertEqual(self.test_argv, self.cl_argv[1:])
		self.assertEqual("naked", self.cl_argv[0])
		self.assertEqual("nakedtest", self.test_argv[0])
		self.assertEqual("testcmd2", self.test_argv[1])
		self.assertEqual("-s", self.test_argv[2])
		self.assertEqual("--long", self.test_argv[3])
		self.assertEqual("-f", self.test_argv[4])
		self.assertEqual("arg1", self.test_argv[5])
		self.assertEqual("--flag2", self.test_argv[6])
		self.assertEqual("arg2", self.test_argv[7])
		self.assertEqual("lparg", self.test_argv[8])

	def test_command_object(self):
		"""Test generation of Command object instance from the test command"""
		self.assertIsInstance(self.cmd_obj, Naked.commandline.Command) #instance of Command object

	def test_command_object_attributes(self):
		"""Test the attributes of the Command object"""
		self.assertIsInstance(self.cmd_obj.argobj, Naked.commandline.Argument) #argobj is instance of Argument
		self.assertIsInstance(self.cmd_obj.optobj, Naked.commandline.Option) #optobj is instance of Option
		self.assertEqual(self.cmd_obj.app, "naked") #app path test
		self.assertIsInstance(self.cmd_obj.argv, list) #argv list test
		self.assertEqual(self.cmd_obj.argv, self.test_argv) #argv = test_argv in this test suite
