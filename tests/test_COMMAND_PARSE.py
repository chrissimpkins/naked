#!/usr/bin/env python

import unittest
import Naked.commandline

class NakedCommandParseTest(unittest.TestCase):

	def setUp(self):
		#------------------------------------------------------------------------------
		# setup for full command inclusion tests
		#------------------------------------------------------------------------------
		self.cl_argv = ["naked", "nakedtest", "testcmd2", "-s", "--long", "-f", "arg1", "--flag2", "arg2", "-t", "--flag3", "-u","lparg"]
		self.test_argv = self.cl_argv[1:]
		self.cmd_obj = Naked.commandline.Command(self.cl_argv[0], self.test_argv)
		#------------------------------------------------------------------------------
		# setup for no primary command tests
		#------------------------------------------------------------------------------
		self.cl2_argv = ["naked"]
		self.test2_argv = self.cl2_argv[1:]
		self.cmd_no_arg_obj = Naked.commandline.Command(self.cl2_argv[0], self.test2_argv)
		#------------------------------------------------------------------------------
		# setup for first argument as option tests
		#------------------------------------------------------------------------------
		self.cl3_argv = ["naked", "--help"]
		self.test3_argv = self.cl3_argv[1:]
		self.cmd_arg_is_option_obj = Naked.commandline.Command(self.cl3_argv, self.test3_argv)
		#------------------------------------------------------------------------------
		# setup for no secondary command to primary command test
		#------------------------------------------------------------------------------
		self.cl4_argv = ["naked", "nakedtest"]
		self.test4_argv = self.cl4_argv[1:]
		self.cmd_no_secondary_cmd_obj = Naked.commandline.Command(self.cl4_argv, self.test4_argv)

	#------------------------------------------------------------------------------
	# Command object tests
	#------------------------------------------------------------------------------
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


	#------------------------------------------------------------------------------
	# Options tests
	#------------------------------------------------------------------------------
	def test_options_present(self):
		"""Test detection of presence of option in the command string"""
		self.assertEqual(self.cmd_obj.option("-s"), True) #short option exists
		self.assertEqual(self.cmd_obj.option("--long"), True) #long option exists
		self.assertEqual(self.cmd_obj.option("-t"), True) #short option exists
		self.assertEqual(self.cmd_obj.option("--flag3"), True) #long option exists
		self.assertEqual(self.cmd_obj.option("-u"), True) #short option exists

	def test_options_absent(self):
		"""Test detection of absence of options that are not present in the command"""
		self.assertEqual(self.cmd_obj.option("-j"), False) #nonexistent short option returns false
		self.assertEqual(self.cmd_obj.option("--bogus"), False) #nonexistent long option returns false

	def test_options_with_arguments(self):
		"""Test detection of appropriate existing arguments to options"""
		self.assertEqual(self.cmd_obj.option("-f", True), True) #short option with proper argument
		self.assertEqual(self.cmd_obj.option_with_arg("-f"), True) #short option with proper argument (method 2)
		self.assertEqual(self.cmd_obj.option("--flag2", True), True) #long option with proper argument
		self.assertEqual(self.cmd_obj.option_with_arg("--flag2"), True) #long option with proper argument (method 2)

	def test_options_with_arguments_bad_arg(self):
		"""Test detection of bad argument (i.e. another option) to option"""
		self.assertEqual(self.cmd_obj.option("-t", True), False) #short option that requires argument with incorrect argument returns false
		self.assertEqual(self.cmd_obj.option_with_arg("-t"), False) #short option that requires argument with incorrect argument returns false (method 2)
		self.assertEqual(self.cmd_obj.option("--flag3", True), False) #long option that requires argument with incorrect argument returns false
		self.assertEqual(self.cmd_obj.option_with_arg("--flag3"), False) #long option that requires argument with incorrect argument returns false (method 2)

	def test_options_correct_argument_returned(self):
		"""Test correct argument string returned for option that requires argument"""
		self.assertEqual(self.cmd_obj.arg("-f"), "arg1") #confirm that correct argument is returned for short option that requires argument
		self.assertEqual(self.cmd_obj.arg("--flag2"), "arg2") #confirm that correct argument is returned for long option that requires argument

	def test_options_in_first_positional_location(self):
		"""Test that first positional argument as option correctly interpreted"""
		self.assertEqual(self.cmd_arg_is_option_obj.arg0, "--help")

	#------------------------------------------------------------------------------
	# Primary command tests
	#------------------------------------------------------------------------------
	def test_primary_command_type(self):
		"""Test detection of the primary command specified"""
		self.assertEqual(self.cmd_obj.cmd, "nakedtest") #primary command is specified as "nakedtest"
		self.assertEqual(self.cmd_no_arg_obj.cmd, "") #primary command is empty string when not specified

		self.assertEqual(self.cmd_obj.command("nakedtest"), True) # test that command method returns True on test for present primary command
		self.assertEqual(self.cmd_obj.command("bogus"), False) # test that command method returns False for absent primary command

		self.assertEqual(self.cmd_obj.command_with_argument("nakedtest"), True) # test that command_with_argument method returns True when command present and correct argument present
		self.assertEqual(self.cmd_obj.command_with_argument("bogus"), False) # test that command_with_argument method returns False when command not present
		self.assertEqual(self.cmd_no_secondary_cmd_obj.command_with_argument("nakedtest"), False) # test that absence of secondary command when mandatory returns False

	def test_primary_command_without_argument(self):
		"""Test primary command with no arguments presented to it"""
		self.assertEqual(self.cmd_no_arg_obj.cmd2, "") #confirm that when primary command entered alone, empty string returned
		self.assertEqual(self.cmd_no_arg_obj.argc, 0) # test length of primary command alone is 0 (the arg list only includes arguments to application cmd)

	#------------------------------------------------------------------------------
	# Command suite validation tests
	#------------------------------------------------------------------------------
	def test_command_suite_validation(self):
		"""Test validation of command suite syntax"""
		self.assertEqual(self.cmd_obj.command_suite_validates(), True) # correct style of primary command validates to true
		self.assertEqual(self.cmd_no_arg_obj.command_suite_validates(), False) # empty argument to application does not validate as command suite
		self.assertEqual(self.cmd_arg_is_option_obj.command_suite_validates(), True) #argument to application that is option validates by default
		self.assertEqual(self.cmd_arg_is_option_obj.command_suite_validates(False), False) #arugment to application that is option does not validate if explicitly specified by user



