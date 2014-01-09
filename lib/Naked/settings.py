#!/usr/bin/env python

#------------------------------------------------------------------------------
# Application Name
#------------------------------------------------------------------------------
app_name = "naked"

#------------------------------------------------------------------------------
# Version Number
#------------------------------------------------------------------------------
major_version = "0"
minor_version = "1"
patch_version = "11"

#------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
#------------------------------------------------------------------------------
debug = True

#------------------------------------------------------------------------------
# Usage String
#------------------------------------------------------------------------------
usage = """<primary command> [secondary command] [option(s)] [argument(s)]
--- Use 'naked help' for detailed help ---
"""

#------------------------------------------------------------------------------
# Help String
#------------------------------------------------------------------------------
help = """
---------------------------------------------------
Naked | A Python command line application framework
Copyright 2014 Christopher Simpkins
MIT license
---------------------------------------------------

USAGE

  naked <primary command> [secondary command] [option(s)] [argument(s)]

The <primary command> is mandatory and includes one of the commands in the following section.  The [bracketed] syntax structure is optional and dependent upon the primary command that you use.  Use the command 'naked <primary command> help' for more information about a specific primary command.

PRIMARY COMMANDS [secondary commands]

  bump 		[major, minor, patch]
  help 		- none -
  locate	[uniset, settings]
  make 		[project, uniset]
  push 		- none -
  usage 	- none -
  version 	- none -

OPTIONS

Options are dependent upon the primary command that you use.  You can enter:

  naked <primary command> help

for more information about available options for a specific command.

SOURCE REPOSITORY

  https://github.com/chrissimpkins/naked

ISSUE REPORTING

  https://github.com/chrissimpkins/naked/issues

"""

