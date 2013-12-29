#!/usr/bin/env python

import sys
import os

#------------------------------------------------------------------------------
#
# FILE & DIRECTORY PATHS
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ filename method ] (string)
#   returns file name from a file path (including the file extension)
#------------------------------------------------------------------------------
def filename(filepath):
	return os.path.basename(filepath)

#------------------------------------------------------------------------------
# [ file_extension method ] (string)
#   returns file extension from a filepath
#------------------------------------------------------------------------------
def file_extension(filepath):
	return os.path.splitext(filepath)

#------------------------------------------------------------------------------
# [ directory method ] (string)
#  returns directory path to the filepath
#------------------------------------------------------------------------------
def directory(filepath):
	return os.path.dirname(filepath)

#------------------------------------------------------------------------------
#  [ make_path method ] (string)
#   returns OS independent file path from tuple of path components
#------------------------------------------------------------------------------
def make_path(*path_list):
	return os.path.join(*path_list)

#------------------------------------------------------------------------------
#  [ currentdir decorator method ] (returns decorated original function)
#    adds the full working directory path to a file name that is used in the decorated function
#------------------------------------------------------------------------------
def currentdir(func):
	from functools import wraps

	@wraps(func)
	def wrapper(file_name, *args, **kwargs):
		current_directory = os.getcwd() #get current working directory path
		full_path = os.path.join(current_directory, file_name) # join cwd path to the filename for full path
		return func(full_path, *args, **kwargs) #return the original function with the full path to file as first argument
	return wrapper

#------------------------------------------------------------------------------
#  [ fullpath method ] (string)
#    returns the full path to a filename that is in the current working directory
#    file_name = the basename of the file in the current working directory
#    Example of filepath variable assignment where test.txt is in working directory:
#		filepath = fullpath("test.txt")
#------------------------------------------------------------------------------
@currentdir # current directory decorator - adds the directory path up to the filename in the current working directory
def fullpath(file_name):
	return file_name

#------------------------------------------------------------------------------
#
# FILE & DIRECTORY TESTING
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ file_exists method ] (boolean)
#  return boolean for existence of file in specified path
#------------------------------------------------------------------------------
def file_exists(filepath):
	return os.path.exists(filepath)

#------------------------------------------------------------------------------
# [ is_file method ] (boolean)
#  returns boolean for determination of whether filepath is a file
#------------------------------------------------------------------------------
def is_file(filepath):
	return os.path.isfile(filepath)

#------------------------------------------------------------------------------
# [ dir_exists method ] (boolean)
#   return boolean for existence of directory in specified path
#------------------------------------------------------------------------------
def dir_exists(dirpath):
	return os.path.exists(dirpath)

#------------------------------------------------------------------------------
# [ is_dir method ] (boolean)
#   returns boolean for determination of whether filepath is a directory
#------------------------------------------------------------------------------
def is_dir(filepath):
	return os.path.isdir(filepath)

#------------------------------------------------------------------------------
#
# FILE METADATA
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ filesize method ] (string)
#   return file size in bytes
#------------------------------------------------------------------------------
def file_size(filepath):
	return os.path.getsize(filepath)

#------------------------------------------------------------------------------
# [ mod_time ] (string)
#   return the file modification date/time
#------------------------------------------------------------------------------
def file_mod_time(filepath):
	import time
	return time.ctime(os.path.getmtime(filepath))

#------------------------------------------------------------------------------
#
# SYMBOLIC LINK TESTING
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ is_link method ] (boolean)
#   return boolean indicating whether the path is a symbolic link
#------------------------------------------------------------------------------
def is_link(filepath):
	return os.path.islink(filepath)

#------------------------------------------------------------------------------
# [ real_path method ] (string)
#   return the real file path pointed to by a symbolic link
#------------------------------------------------------------------------------
def real_path(filepath):
	return os.path.realpath(filepath)

#------------------------------------------------------------------------------
#
# DATA STREAMS
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ stdout method ]
#   print to std output stream
#------------------------------------------------------------------------------
def stdout(text):
	print(text)

#------------------------------------------------------------------------------
# [ stderr method ]
#   print to std error stream
#   optionally (i.e. if exit = nonzero integer) permits exit from application with developer defined exit code
#------------------------------------------------------------------------------
def stderr(text, exit=0):
	sys.stderr.write(text)
	if exit:
		raise SystemExit(exit)

#------------------------------------------------------------------------------
#
# APPLICATION CONTROL
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ exit_with_status method ]
#   application exit with developer specified exit status code (default = 1)
#------------------------------------------------------------------------------
def exit_with_status(exit=1):
	raise SystemExit(exit)

if __name__ == '__main__':
	pass
