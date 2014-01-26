#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# Application Name
#------------------------------------------------------------------------------
app_name = "naked"

#------------------------------------------------------------------------------
# Version Number
#------------------------------------------------------------------------------
major_version = "0"
minor_version = "1"
patch_version = "15"

#------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
#------------------------------------------------------------------------------
debug = False

#------------------------------------------------------------------------------
# Usage String
#------------------------------------------------------------------------------
usage = """
Usage: naked <primary command> [secondary command] [option(s)] [argument(s)]
--- Use 'naked help' for detailed help ---
"""

#------------------------------------------------------------------------------
# Help String
#------------------------------------------------------------------------------
help = """
---------------------------------------------------
 Naked
 A Python command line application framework
 Copyright 2014 Christopher Simpkins
 MIT license
---------------------------------------------------

ABOUT

The Naked framework includes the "naked" executable and a Python extension library that can be used for application development.  The naked executable creates a complete directory structure for a command suite application with appropriate file stubs.  The library provides parsing of user entered commands into a Python object as well as type, method, & function extensions to the Python standard library.

USAGE

The naked executable syntax is:

  naked <primary command> [secondary command] [option(s)] [argument(s)]

The <primary command> is mandatory and includes one of the commands in the following section.  The [bracketed] syntax structure is optional and dependent upon the primary command that you use.  Use the command 'naked <primary command> help' for more information about a specific primary command.

PRIMARY COMMANDS   [Secondary Commands]

  build                 - none -
  help                  - none -
  locate         [ main, settings, setup ]
  make                  - none -
  test                   [ tox ]
  usage                 - none -
  version               - none -

HELP

To learn more about a primary command, use the following syntax:

  naked <primary command> help


SOURCE REPOSITORY

  https://github.com/chrissimpkins/naked

ISSUE REPORTING

  https://github.com/chrissimpkins/naked/issues

"""

