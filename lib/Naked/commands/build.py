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
	print('•naked• Compiling the C source library files...')
	run("python setup.py build_ext --inplace")

def help():
	from Naked.toolshed.system import exit_success
	help_string = """
Naked build Command Help
========================
The build command compiles the Naked C libraries.  This requires an installed C compiler.

USAGE
  naked build

SECONDARY COMMANDS
  none

OPTIONS
  none"""
	print(help_string)
	exit_success()


if __name__ == '__main__':
	pass
