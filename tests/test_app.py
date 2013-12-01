#!/usr/bin/env python

#==========================================================
# unittest
#==========================================================
# Install:
#		part of standard library
#
# Usage:
#  		-->> Run all tests in a suite <<--
#  				python test_app.py
#
#  		-->> Run specific test(s) <<--
#  				python test_app.py test_true
#-----------------------------------------------------------

#==========================================================
# Nose
#==========================================================
# Install:
#		pip install nose
#
# Usage:
#  		-->> Run all tests in a suite <<--
#  				nosetests --verbosity=3 test_app.py
#
#  		-->> Run specific test(s) <<--
#  				nosetests --verbosity=3 "test_app.py:NakedTest.test_true"
#-----------------------------------------------------------------------

#==========================================================
# Pytest
#==========================================================
# Install:
# 		pip install pytest
# Usage:
#  		-->> Run all tests in a suite <<--
#  				py.test --verbose test_app.py
#
#  		-->> Run specific test(s) <<--
#  				py.test --verbose -k test_true
#-----------------------------------------------------------

import unittest

class AppTest(unittest.TestCase):

	def setUp(self):
		print("setup!")

	def tearDown(self):
		print("tear down!")

	def test_true(self):
		"""Test that True == True"""
		thetruth = True
		self.assertEqual(True, thetruth)

	def test_false(self):
		"""Test that False == False"""
		thefalse = False
		self.assertEqual(False, thefalse)


if __name__ == "__main__":
	import sys
	suite = unittest.TestSuite()
	# default to load all tests from the test suite
	if len(sys.argv) == 1:
		suite = unittest.TestLoader().loadTestsFromTestCase(AppTest)
	# user can indicate specific tests that they would like to run
	else:
		for the_test in sys.argv[1:]:
			suite.addTest(AppTest(the_test))
	# run tests
	unittest.TextTestRunner(verbosity=2).run(suite)
