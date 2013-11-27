#!/usr/bin/env python

#############################################################
# Command line command string object
#   argv = list of command line arguments and options
#   argc = count of command line arguments and options
#   arg0 = first argument to command
#   arg1 = second argument to command
#   arglp = last positional argument to command
#   argprimarycmd = primary command for command suite application
#   argsecondarycmd = secondary command for command suite application
##############################################################
class Command:
	def __init__(self, cmdarg, argv):
		# from Naked.commandline import Argument # import the Argument class
		# from Naked.commandline import Option # import Option class
		self.argobj = Argument(argv) # create a Argument obj
		self.optobj = Option(argv) # create an Option obj
		self.cmd = cmdarg   # path to command executable file
		self.argv = argv    # list of the command arguments argv[0] is first argument
		self.argc = len(argv)  # length of the argument list
		self.arg0 = self.argobj._getArg(0) # define the first argument as a local variable
		self.arg1 = self.argobj._getArg(1) # define the second argument as a local variable
		self.arglp = self.argobj._getArg(len(argv) - 1) # define the last positional argument as a local variable
		self.primarycmd = self.arg0  # define the primary command variable as the first positional argument (user dependent & optional, may be something else)
		self.secondarycmd = self.arg1 # define the secondary command variable as the second positional argument (user dependent & optional, may be something else)
		# self.options

	def option(self, option_string, argument_required = False):
		if (option_string in self.optobj):
			## TODO: add handling for options that require an argument
			return True
		else:
			return False

	def command(self, cmd_str, argument_required = False):
		if (cmd_str == self.primarycmd):
			## TODO: add handling for command that requires additional arguments
			return True
		else:
			return False

	# print the arguments with their corresponding agv list position to std out
	def show_args(self):
		x = 0
		for arg in self.argv:
			print("argv[" + str(x) + "] = " + arg)
			x = x + 1

# Command line argument object (list object inherited from Python list)
class Argument(list):
	def __init__(self, argv):
		self.argv = argv
		list.__init__(self, self.argv)


	# return argument at position specified by the 'position' parameter
	def _getArg(self, position):
		if ( self.argv ) and ( len(self.argv) > position ):
			return self.argv[position]
		else:
			return ""

# Command line option object (list object inherited from Python list)
class Option(list):
	def __init__(self, argv):
		self.argv = argv
		list.__init__(self, self._make_option_list())

	# make a list of the options in the command (defined as anything that starts with "-" character)
	def _make_option_list(self):
		optargv = []
		for x in self.argv:
			if x.startswith("-"):
				optargv.append(x)
		return optargv
