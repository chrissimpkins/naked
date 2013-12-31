#!/usr/bin/env python

import sys
import os
from Naked.settings import debug as DEBUG_FLAG

#------------------------------------------------------------------------------
#
# FILE & DIRECTORY PATHS
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ filename function ] (string)
#   returns file name from a file path (including the file extension)
#------------------------------------------------------------------------------
def filename(filepath):
	try:
		return os.path.basename(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return base filename from filename() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ file_extension function ] (string)
#   returns file extension from a filepath
#------------------------------------------------------------------------------
def file_extension(filepath):
	try:
		return os.path.splitext(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return file extension with file_extension() function (Naked.toolshed.system).")
		raise e


#------------------------------------------------------------------------------
# [ directory function ] (string)
#  returns directory path to the filepath
#------------------------------------------------------------------------------
def directory(filepath):
	try:
		return os.path.dirname(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return directory path to file with directory() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#  [ make_path function ] (string)
#   returns OS independent file path from tuple of path components
#------------------------------------------------------------------------------
def make_path(*path_list):
	try:
		return os.path.join(*path_list)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to make OS independent path with the make_path() function (Naked.toolshed.system).")
		raise e


#------------------------------------------------------------------------------
#  [ currentdir_to_basefile decorator function ] (returns decorated original function)
#    adds the full working directory path to the basename of file in the first argument of the undecorated function
#------------------------------------------------------------------------------
def currentdir_to_basefile(func):
	try:
		from functools import wraps

		@wraps(func)
		def wrapper(file_name, *args, **kwargs):
			current_directory = os.getcwd() #get current working directory path
			full_path = os.path.join(current_directory, file_name) # join cwd path to the filename for full path
			return func(full_path, *args, **kwargs) #return the original function with the full path to file as first argument
		return wrapper
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with the currentdir_to_basefile() decorator function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ currentdir_firstargument decorator function ] (returns decorated original function)
#   adds the current working directory as the first function argument to the original function
#------------------------------------------------------------------------------
def currentdir_firstargument(func):
	try:
		from functools import wraps

		@wraps(func)
		def wrapper(dir="", *args, **kwargs):
			current_directory = os.getcwd()
			return func(current_directory, *args, **kwargs)
		return wrapper
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with the currentdir_firstargument() decorator function (Naked.toolshed.system).")
		raise e


#------------------------------------------------------------------------------
# [ currentdir_lastargument decorator function ] (returns decorated original function)
#   adds the current working directory as the last function argument to the original function
#   Note: you cannot use other named arguments in the original function with this decorator
#   Note: the current directory argument in the last position must be named current_dir
#------------------------------------------------------------------------------
def currentdir_lastargument(func):
	try:
		from functools import wraps

		@wraps(func)
		def wrapper(*args, **kwargs):
			the_cwd = os.getcwd()
			return func(*args, current_dir=the_cwd)
		return wrapper
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with the currentdir_lastargument() decorator function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#  [ fullpath function ] (string)
#    returns the full path to a filename that is in the current working directory
#    file_name = the basename of the file in the current working directory
#    	Example usage where test.txt is in working directory:
#			filepath = fullpath("test.txt")
#------------------------------------------------------------------------------
@currentdir_to_basefile # current directory decorator - adds the directory path up to the filename to the basefile name argument to original function
def fullpath(file_name):
	try:
		return file_name
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return absolute path to the file with the fullpath() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ cwd function ] (string)
#   returns the current working directory path
#   does not need to be called with an argument, the decorator assigns it
#   	Example usage:
#       	current_dir = cwd()
#------------------------------------------------------------------------------
@currentdir_firstargument
def cwd(dir=""):
	try:
		return dir
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return the current working directory with the cwd() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# FILE & DIRECTORY TESTING
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ file_exists function ] (boolean)
#  return boolean for existence of file in specified path
#------------------------------------------------------------------------------
def file_exists(filepath):
	try:
		return os.path.exists(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with test for the presence of the file with the file_exists() method (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ is_file function ] (boolean)
#  returns boolean for determination of whether filepath is a file
#------------------------------------------------------------------------------
def is_file(filepath):
	try:
		return os.path.isfile(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with test for file with the is_file() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ dir_exists function ] (boolean)
#   return boolean for existence of directory in specified path
#------------------------------------------------------------------------------
def dir_exists(dirpath):
	try:
		return os.path.exists(dirpath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with test for directory with the dir_exists() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ is_dir function ] (boolean)
#   returns boolean for determination of whether filepath is a directory
#------------------------------------------------------------------------------
def is_dir(filepath):
	try:
		return os.path.isdir(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: error with test for directory with the is_dir() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# FILE METADATA
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ filesize function ] (string)
#   return file size in bytes
#------------------------------------------------------------------------------
def file_size(filepath):
	try:
		return os.path.getsize(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return file size with the file_size() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ mod_time function ] (string)
#   return the file modification date/time
#------------------------------------------------------------------------------
def file_mod_time(filepath):
	try:
		import time
		return time.ctime(os.path.getmtime(filepath))
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return file modification data with the file_mod_time() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# FILE LISTINGS
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ list_all_files function ] (list)
#   returns a list of all files in developer specified directory
#------------------------------------------------------------------------------
def list_all_files(dir):
	try:
		filenames = [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]
		return filenames
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to generate directory file list with the list_all_files() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ list_filter_files function ] (list)
#   returns a list of files filtered by developer defined file extension in developer defined directory
#   	Usage example:
#   		filenames = list_filter_files("py", "tests")
#------------------------------------------------------------------------------
def list_filter_files(extension_filter, dir):
	try:
		if not extension_filter.startswith("."):
		extension_filter = "." + extension_filter #add a period to the extension if the developer did not include it
		filenames = [name for name in os.listdir(dir) if name.endswith(extension_filter)]
		return filenames
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return list of filtered files with the list_filter_files() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ list_all_files_cwd function ] (list)
#   returns a list of all files in the current working directory
#   Note: does not require argument, the decorator assigns the cwd
#   	Usage example:
#			file_list = list_all_files_cwd()
#------------------------------------------------------------------------------
@currentdir_firstargument
def list_all_files_cwd(dir=""):
	try:
		return list_all_files(dir)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return list of all files in current working directory with the list_all_files_cwd() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ list_filter_files_cwd function ] (list)
#   returns a list of all files in the current working directory filtered by developer specified file extension
#	Note: do not specify the second argument, decorator assigns it
#   	Usage example:
#			file_list = list_filter_files_cwd(".py")
#------------------------------------------------------------------------------
@currentdir_lastargument
def list_filter_files_cwd(extension_filter, current_dir=""):
	try:
		return list_filter_files(extension_filter, current_dir)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return list of filtered files in current working directory with the list_filter_files_cwd() function (Naked.toolshed.system).")
		raise e


#------------------------------------------------------------------------------
# [ list_match_files function ] (list)
#   returns a list of all files that match the developer specified match pattern
#	can optionally specify return of full path to the files (rather than relative path from cwd) by setting full_path to True
#   	Usage examples:
#			file_list = list_match_files("*.py")
#			file_list_fullpath = list_match_files("*.py", True)
#------------------------------------------------------------------------------
def list_match_files(match_pattern, full_path = False):
	try:
		from glob import glob
		filenames = glob(match_pattern)
		if full_path:
			filenames_fullpath = []
			cwd = os.getcwd()
			for name in filenames:
				name = os.path.join(cwd, name) #make the full path to the file
				filenames_fullpath.append(name) #add to the new list
			return filenames_fullpath #then return that list
		else:
			return filenames
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return list of matched files with the list_match_files() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# SYMBOLIC LINK TESTING
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ is_link function ] (boolean)
#   return boolean indicating whether the path is a symbolic link
#------------------------------------------------------------------------------
def is_link(filepath):
	try:
		return os.path.islink(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to determine whether path is a symbolic link with the is_link() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ real_path function ] (string)
#   return the real file path pointed to by a symbolic link
#------------------------------------------------------------------------------
def real_path(filepath):
	try:
		return os.path.realpath(filepath)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to return real path for symbolic link with the real_path() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# DATA STREAMS
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ stdout function ]
#   print to std output stream
#------------------------------------------------------------------------------
def stdout(text):
	try:
		print(text)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to print to the standard output stream with the stdout() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
# [ stderr function ]
#   print to std error stream
#   optionally (i.e. if exit = nonzero integer) permits exit from application with developer defined exit code
#------------------------------------------------------------------------------
def stderr(text, exit=0):
	try:
		sys.stderr.write(text)
		if exit:
			raise SystemExit(exit)
	except Exception as e:
		if DEBUG_FLAG:
			sys.stderr.write("Naked Framework Error: unable to print to the standard error stream with the stderr() function (Naked.toolshed.system).")
		raise e

#------------------------------------------------------------------------------
#
# APPLICATION CONTROL
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# [ exit_with_status function ]
#   application exit with developer specified exit status code (default = 1)
#------------------------------------------------------------------------------
def exit_with_status(exit=1):
	raise SystemExit(exit)

#------------------------------------------------------------------------------
# [ exit_fail function ]
#   application exit with status code 1
#------------------------------------------------------------------------------
def exit_fail():
	sys.exit(1)

#------------------------------------------------------------------------------
# [ exit_success function]
#   application exit with status code 0
#------------------------------------------------------------------------------
def exit_success():
	sys.exit(0)

if __name__ == '__main__':
	pass
