#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# [ compile_c_code function ] (--none--)
#  compile C files in the lib/Naked/toolshed/c directory
#------------------------------------------------------------------------------
def compile_c_code(abs_dirpath):
	from Naked.toolshed.shell import run
	from os import chdir

	chdir(abs_dirpath)
	run("python setup.py build_ext --inplace")

def help():
	from Naked.toolshed.system import exit_success
	help_string = """
Naked build command help
------------------------
The build command compiles the Naked C libraries.

USAGE
  naked build

OPTIONS
  none
	"""
	print(help_string)
	exit_success()


if __name__ == '__main__':
	pass
