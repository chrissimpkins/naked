#!/usr/bin/env python
# encoding: utf-8

import os
from Naked.toolshed.system import file_exists, stderr, exit_success
from Naked.toolshed.shell import run

class Dist:
    def __init__(self):
        self.register = "python setup.py register"
        self.sdist = "python setup.py sdist upload"
        self.wheel = "python setup.py bdist_wheel upload"
        self.win = "python setup.py bdist_wininst upload"
        self.all = "python setup.py sdist bdist_wheel bdist_wininst upload"

    #------------------------------------------------------------------------------
    # [ run method ] - iterates through up to 4 directories above current working
    #                  directory and then runs command if setup.py found
    #------------------------------------------------------------------------------
    def run(self, command):
        setuppy_found = False
        for i in range(4): # navigate up at most 4 directory levels to search for the setup.py file
            if not self._is_setup_py_at_this_level():
                os.chdir(os.pardir)
            else:
                setuppy_found = True
                self._run_dist_command(command)
                break
        if not setuppy_found:
            stderr("Unable to locate the setup.py file for your project.  Please confirm that you are in your project directory and try again.", 1)

    # search for setup.py file
    def _is_setup_py_at_this_level(self):
        if file_exists('setup.py'):
            return True
        else:
            return False

    # run the user requested command
    def _run_dist_command(self, the_command):
        if the_command in "register":
            run(self.register)
        elif the_command in "sdist":
            run(self.sdist)
        elif the_command in "wheel":
            run(self.wheel)
        elif the_command in "win":
            run(self.win)
        elif the_command in "all":
            run(self.all)
        else:
            stderr("Unrecognized command.  Use 'naked dist help' to view the supported commands.", 1)


def help():
    help_string = """
Naked dist Command Help
-----------------------
The dist secondary commands run the standard distutils 'python setup.py <command>' source/binary distribution commands.

USAGE
  naked dist <secondary_command>

SECONDARY COMMANDS   python setup.py <command(s)>
  all                  sdist bdist_wheel bdist_wininst upload
  register             register
  sdist                sdist upload
  wheel                bdist_wheel upload
  win                  bdist_wininst

OPTIONS
  none"""
    print(help_string)
    exit_success()

if __name__ == '__main__':
    pass
