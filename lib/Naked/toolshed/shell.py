#!/usr/bin/env python

import os
import sys
from Naked.settings import debug as DEBUG_FLAG

class Environment():
	def __init__(self):
		self.env = os.environ
		self.vars = list(os.environ.keys())

	#------------------------------------------------------------------------------
	# [ is_var method ] (boolean)
	#   return boolean for presence of a variable name in the shell environment
	#------------------------------------------------------------------------------
	def is_var(self, var_name):
		try:
			return (var_name in self.vars)
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: unable to determine if the variable is included in the shell variable list with the is_var() method (Naked.toolshed.shell).")
			raise e

	#------------------------------------------------------------------------------
	# [ get_var method ] (string)
	#   get the variable value for a variable in the shell environment list
	#   returns empty string if the variable is not included in the environment variable list
	#------------------------------------------------------------------------------
	def get_var(self, var_name):
		try:
			if var_name in self.vars:
				return self.env[var_name]
			else:
				return ""
		except Exception, e:
			raise e

	#------------------------------------------------------------------------------
	# [ get_split_var_list method ] (list of strings)
	#   return a list of strings split by OS dependent separator from the shell variable assigment string
	#------------------------------------------------------------------------------
	def get_split_var_list(self, var_name):



if __name__ == '__main__':
	pass
