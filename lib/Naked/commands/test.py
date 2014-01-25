#!/usr/bin/env python
# encoding: utf-8

import os
from Naked.toolshed.system import cwd, file_exists, dir_exists, stderr

#------------------------------------------------------------------------------
# [ ToxTester class ]
#  Run Tox on the project directory, by default runs all python versions in tox.ini
#  Optional specify the version of Python to test in constructor (runs 'tox -e py<version>')
#------------------------------------------------------------------------------
class ToxTester:
    def __init__(self, py_version=""):
        self.cwd = cwd()
        self.py_version = py_version

    def run(self):
        tox_found = False
        for i in range(4):
            if not self._is_tox_ini_at_this_level():
                os.chdir(os.pardir)
            else:
                tox_found = True
                self._run_tox()
                break
        if not tox_found:
            stderr("Unable to locate your tox.ini file.  Please navigate to your project directory.", 1)

    def _is_tox_ini_at_this_level(self):
        if file_exists('tox.ini'):
            return True
        else:
            return False

    def _run_tox(self):
        if self.py_version == "":
            os.system("tox")
        else:
            cmd_string = "tox -e" + self.py_version
            os.system(cmd_string)

if __name__ == '__main__':
    pass
