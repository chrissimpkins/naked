#!/usr/bin/env python

import unittest
import subprocess
import Naked.commandline
import Naked.settings

class NakedHelpCommandTest(unittest.TestCase):

	def test_help_command(self):
		"""Test the help command"""
		# the help string to test against
		output_standard = Naked.settings.help + "\n"

		# test the --help option
		output = subprocess.check_output(["naked", "--help"])
		self.assertEqual(output, output_standard)
		# test the 'help' primary command
		output = subprocess.check_output(["naked", "help"])
		self.assertEqual(output, output_standard)

class NakedUsageCommandTest(unittest.TestCase):

	def test_usage_command(self):
		"""Test the usage command"""
		# the usage string to test against
		usage_standard = "Usage: " + Naked.settings.app_name + " " + Naked.settings.usage + "\n"

		#test the --usage option
		output = subprocess.check_output(["naked", "--usage"])
		self.assertEqual(output, usage_standard)

		#test the 'usage' primary command
		output = subprocess.check_output(["naked", "usage"])
		self.assertEqual(output, usage_standard)

class NakedVersionCommandTest(unittest.TestCase):

	def test_version_command(self):
		"""Test the version command"""
		# the version string to test against
		version_standard = Naked.settings.app_name + " " + Naked.settings.major_version + "." + Naked.settings.minor_version + "." + Naked.settings.patch_version + "\n"

		#test the --version option
		output = subprocess.check_output(["naked", "--version"])
		self.assertEqual(output, version_standard)
		#test the 'version' primary command
		output = subprocess.check_output(["naked", "version"])
		self.assertEqual(output, version_standard)
