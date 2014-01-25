#!/usr/bin/env python

import unittest
import subprocess
import Naked.commandline
import Naked.settings
from Naked.toolshed.state import StateObject
state = StateObject()

class NakedHelpCommandTest(unittest.TestCase):

	def test_help_command(self):
		"""Test the help command"""
		# the help string to test against
		output_standard = Naked.settings.help + "\n"

		# test the --help option
		if state.py2:
			output = subprocess.check_output(["naked", "--help"])
		else:
			output = subprocess.check_output(["naked", "--help"], universal_newlines=True)
		self.assertEqual(output, output_standard)

		# test the 'help' primary command
		if state.py2:
			output = subprocess.check_output(["naked", "help"])
		else:
			output = subprocess.check_output(["naked", "help"], universal_newlines=True)
		self.assertEqual(output, output_standard)

class NakedUsageCommandTest(unittest.TestCase):

	def test_usage_command(self):
		"""Test the usage command"""
		# the usage string to test against
		usage_standard =  Naked.settings.usage + "\n" #print adds an extra '\n'

		#test the --usage option
		if state.py2:
			output = subprocess.check_output(["naked", "--usage"])
		else:
			output = subprocess.check_output(["naked", "--usage"], universal_newlines=True)
		self.assertEqual(output, usage_standard)

		#test the 'usage' primary command
		if state.py2:
			output = subprocess.check_output(["naked", "usage"])
		else:
			output = subprocess.check_output(["naked", "usage"], universal_newlines=True)
		self.assertEqual(output, usage_standard)

class NakedVersionCommandTest(unittest.TestCase):

	def test_version_command(self):
		"""Test the version command"""
		# the version string to test against
		version_standard = Naked.settings.app_name + " " + Naked.settings.major_version + "." + Naked.settings.minor_version + "." + Naked.settings.patch_version + "\n"

		#test the --version option
		if state.py2:
			output = subprocess.check_output(["naked", "--version"])
		else:
			output = subprocess.check_output(["naked", "--version"], universal_newlines=True)
		self.assertEqual(output, version_standard)
		#test the 'version' primary command
		if state.py2:
			output = subprocess.check_output(["naked", "version"])
		else:
			output = subprocess.check_output(["naked", "version"], universal_newlines=True)
		self.assertEqual(output, version_standard)
