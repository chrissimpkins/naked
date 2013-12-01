#!/usr/bin/env python

import unittest
import Naked.commandline

class NakedCommandParseTest(unittest.TestCase):

	def setUp(self):
		self.cl_argv = ["naked", "nakedtest", "testcmd2", "-s", "--long", "-f", "arg1", "--flag2", "arg2", "-t", "--flag3", "-u","lparg"]
		self.test_argv = self.cl_argv[1:]
		self.cmd_obj = Naked.commandline.Command(self.cl_argv[0], self.test_argv)

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
		self.assertEqual("-t", self.test_argv[8])
		self.assertEqual("--flag3", self.test_argv[9])
		self.assertEqual("-u", self.test_argv[10])
		self.assertEqual("lparg", self.test_argv[11])

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
		self.assertEqual(self.cmd_obj.argc, 12) # 12 arguments in command
		self.assertEqual(self.cmd_obj.arg0, "nakedtest")
		self.assertEqual(self.cmd_obj.cmd, "nakedtest")
		self.assertEqual(self.cmd_obj.arg1, "testcmd2")
		self.assertEqual(self.cmd_obj.arglp, "lparg") # test last positional argument

	def test_options(self):
		"""Test option and argument parsing in the command string"""
		self.assertEqual(self.cmd_obj.option("-s"), True) #short option exists
		self.assertEqual(self.cmd_obj.option("--long"), True) #long option exists
		self.assertEqual(self.cmd_obj.option("-t"), True) #short option exists
		self.assertEqual(self.cmd_obj.option("--flag3"), True) #long option exists
		self.assertEqual(self.cmd_obj.option("-u"), True) #short option exists
		self.assertEqual(self.cmd_obj.option("-j"), False) #nonexistent short option returns false
		self.assertEqual(self.cmd_obj.option("--bogus"), False) #nonexistent long option returns false

	def test_options_with_arguments(self):
		"""Test arguments to options"""
		self.assertEqual(self.cmd_obj.option("-f", True), True) #short option with proper argument
		self.assertEqual(self.cmd_obj.option("--flag2", True), True) #long option with proper argument
		self.assertEqual(self.cmd_obj.option("-t", True), False) #short option that requires argument with incorrect argument returns false
		self.assertEqual(self.cmd_obj.option("--flag3", True), False) #long option that requires argument with incorrect argument returns false
		self.assertEqual(self.cmd_obj.arg("-f"), "arg1") #confirm that correct argument is returned for short option that requires argument
		self.assertEqual(self.cmd_obj.arg("--flag2"), "arg2") #confirm that correct argument is returned for long option that requires argument



