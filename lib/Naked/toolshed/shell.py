#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import subprocess
from Naked.settings import debug as DEBUG_FLAG

#------------------------------------------------------------------------------
# [ run function ] (byte string or False)
#   run a shell command
#   print the standard output to the standard output stream by default
#   set suppress_output to True to suppress stream to standard output.  String is still returned to calling function
#   set suppress_exit_status_call to True to suppress raising sys.exit on failures with shell subprocess exit status code (if available) or 1 if not available
#   returns the standard output byte string from the subprocess executable on success
#   returns False if the subprocess exits with a non-zero exit code
#------------------------------------------------------------------------------
def run(command, suppress_output=False, suppress_exit_status_call=False):
    try:
        response = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        if not suppress_output:
            print(response)
        return response
    except subprocess.CalledProcessError as cpe:
        if not suppress_output:
            sys.stderr.write(cpe.output)

        if not suppress_exit_status_call:
            if cpe.returncode:
                sys.exit(cpe.returncode)
            else:
                sys.exit(1)
        return False # return False on non-zero exit status codes (i.e. failures in the subprocess executable)
    except Exception as e:
        if DEBUG_FLAG:
            sys.stderr.write("Naked Framework Error: unable to run the shell command with the run() function (Naked.toolshed.shell.py).")
        raise e

#------------------------------------------------------------------------------
# [ run_py function ] (byte string or False)
#  execute a python script in a shell subprocess
#  print the standard output to the standard output stream by default
#  set suppress_output to True to suppress stream to standard output.  String is still returned to calling function
#  set suppress_exit_status_call to True to suppress raising sys.exit on failures with shell subprocess exit status code (if available) or 1 if not available
#  returns the standard output byte string from the subprocess executable on success
#  returns False if the subprocess exits with a non-zero exit code
#------------------------------------------------------------------------------
def run_py(command, suppress_output=False, suppress_exit_status_call=False):
    try:
        py_command = 'python -c "' + command + '"'
        response = subprocess.check_output(py_command, stderr=subprocess.STDOUT, shell=True)
        if not suppress_output:
            print(response)
        return response
    except subprocess.CalledProcessError as cpe:
        if not suppress_output:
            sys.stderr.write(cpe.output)

        if not suppress_exit_status_call:
            if cpe.returncode:
                sys.exit(cpe.returncode)
            else:
                sys.exit(1)
        return False # return False on non-zero exit status codes (i.e. failures in the subprocess executable)
    except Exception as e:
        if DEBUG_FLAG:
            sys.stderr.write("Naked Framework Error: unable to run the shell command with the run_py() function (Naked.toolshed.shell.py).")
        raise e

#------------------------------------------------------------------------------
# [ run_rb function ] (byte string or False)
#  execute a ruby script file in a shell subprocess
#  print the standard output to the standard output stream by default
#  set suppress_output to True to suppress stream to standard output.  String is still returned to calling function
#  set suppress_exit_status_call to True to suppress raising sys.exit on failures with shell subprocess exit status code (if available) or 1 if not available
#  returns the standard output byte string from the subprocess executable on success
#  returns False if the subprocess exits with a non-zero exit code
#------------------------------------------------------------------------------
def run_rb(file_path, args="", suppress_output=False, suppress_exit_status_call=False):
    try:
        if len(args) > 0:
            rb_command = 'ruby ' + filepath + " " + args
        else:
            rb_command = 'ruby ' + filepath
        response = subprocess.check_output(rb_command, stderr=subprocess.STDOUT, shell=True)
        if not suppress_output:
            print(response)
        return response
    except subprocess.CalledProcessError as cpe:
        if not suppress_output:
            sys.stderr.write(cpe.output)

        if not suppress_exit_status_call:
            if cpe.returncode:
                sys.exit(cpe.returncode)
            else:
                sys.exit(1)
        return False # return False on non-zero exit status codes (i.e. failures in the subprocess executable)
    except Exception as e:
        if DEBUG_FLAG:
            sys.stderr.write("Naked Framework Error: unable to run the shell command with the run_rb() function (Naked.toolshed.shell.py).")
        raise e

#------------------------------------------------------------------------------
# [ run_js function ] (byte string or False)
#  execute a node.js script file in a shell subprocess
#  print the standard output to the standard output stream by default
#  set suppress_output to True to suppress stream to standard output.  String is still returned to calling function
#  set suppress_exit_status_call to True to suppress raising sys.exit on failures with shell subprocess exit status code (if available) or 1 if not available
#  returns the standard output byte string from the subprocess executable on success
#  returns False if the subprocess exits with a non-zero exit code
#------------------------------------------------------------------------------
def run_js(file_path, args="", suppress_output=False, suppress_exit_status_call=False):
    try:
        if len(args) > 0:
            rb_command = 'node ' + filepath + " " + args
        else:
            rb_command = 'node ' + filepath
        response = subprocess.check_output(rb_command, stderr=subprocess.STDOUT, shell=True)
        if not suppress_output:
            print(response)
        return response
    except subprocess.CalledProcessError as cpe:
        if not suppress_output:
            sys.stderr.write(cpe.output)

        if not suppress_exit_status_call:
            if cpe.returncode:
                sys.exit(cpe.returncode)
            else:
                sys.exit(1)
        return False # return False on non-zero exit status codes (i.e. failures in the subprocess executable)
    except Exception as e:
        if DEBUG_FLAG:
            sys.stderr.write("Naked Framework Error: unable to run the shell command with the run_js() function (Naked.toolshed.shell.py).")
        raise e
#------------------------------------------------------------------------------
# [ Environment Class ]
#   shell environment variables class
#   self.env = the environment variable dictionary
#   self.vars = the environment variable names list
#------------------------------------------------------------------------------
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
        except Exception as e:
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
        except Exception as e:
            if DEBUG_FLAG:
                sys.stderr.write("Naked Framework Error: unable to return the requested shell variable with the get_var() method (Naked.toolshed.shell).")
            raise e

    #------------------------------------------------------------------------------
    # [ get_split_var_list method ] (list of strings)
    #   return a list of strings split by OS dependent separator from the shell variable assigment string
    #   if the variable name is not in the environment list, returns an empty list
    #------------------------------------------------------------------------------
    def get_split_var_list(self, var_name):
        try:
            if var_name in self.vars:
                return self.env[var_name].split(os.pathsep)
            else:
                return []
        except Exception as e:
            if DEBUG_FLAG:
                sys.stderr.write("Naked Framework Error: unable to return environment variable list with the get_split_var_list() method (Naked.toolshed.shell).")
            raise e


if __name__ == '__main__':
    pass
    # e = Environment()
    # pathlist = e.get_split_var_list("PATH")
    # for item in pathlist:
    #   print(item)
