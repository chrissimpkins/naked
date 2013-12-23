#!/usr/bin/env python

#####################################################################
# Command line command string object
#   argv = list of command line arguments and options
#   argc = count of command line arguments and options
#   arg0 = first positional argument to command
#   arg1 = second positional argument to command
#   arglp = last positional argument to command
#   cmd = primary command for command suite application (=arg0)
#   cmd2 = secondary command for command suite application (=arg1)
#####################################################################
class Command:
	def __init__(self, app_path, argv):
		self.argobj = Argument(argv) # create an Argument obj
		self.optobj = Option(argv) # create an Option obj
		self.app = app_path   # path to application executable file
		self.argv = argv    # list of the command arguments argv[0] is first argument
		self.argc = len(argv)  # length of the argument list
		self.arg0 = self.argobj._getArg(0) # define the first positional argument as a local variable
		self.arg1 = self.argobj._getArg(1) # define the second positional argument as a local variable
		self.arglp = self.argobj._getArg(len(argv) - 1) # define the last positional argument as a local variable
		self.cmd = self.arg0  # define the primary command variable as the first positional argument (user dependent & optional, may be something else)
		self.cmd2 = self.arg1 # define the secondary command variable as the second positional argument (user dependent & optional, may be something else)

	# test that the command includes an option (option_string parameter)
	def option(self, option_string, argument_required = False):
		if (option_string in self.optobj):
			argument_to_option = self.argobj._getArgNext(self.argobj._getArgPosition(option_string))
			if argument_required and ( argument_to_option == "" or argument_to_option.startswith("-") ):
				return False
			else:
				return True
		else:
			return False

	# TODO : add to tests
	# test that command includes an option (option_string parameter) that includes an argument (=option(option_string, True))
	def option_with_arg(self, option_string, argument_required = True):
		if (option_string in self.optobj):
			argument_to_option = self.argobj._getArgNext(self.argobj._getArgPosition(option_string))
			if argument_required and ( argument_to_option == "" or argument_to_option.startswith("-") ):
				return False
			else:
				return True
		else:
			return False

	# test that the command includes a primary command suite command (cmd_str parameter)
	def command(self, cmd_str, argument_required = False):
		if (cmd_str == self.cmd):
			return True
		else:
			return False

	# return the next positional argument to a command line object (e.g. an option that requires an argument)
	def arg(self, arg_recipient):
		recipient_position = self.argobj._getArgPosition(arg_recipient)
		return self.argobj._getArgNext(recipient_position)

	# did user request help?
	def help(self):
		if ( (self.option("--help")) or (self.option("-h")) or (self.cmd == "help") ):
			return True
		else:
			return False

	# did user request usage info?
	def usage(self):
		if ( (self.argc == 0) or (self.option("--usage")) or (self.cmd == "usage") ):
			return True
		else:
			return False

	# did user request version info?
	def version(self):
		if ( (self.option("--version")) or (self.option("-v")) or (self.cmd == "version") ):
			return True
		else:
			return False

	# print the arguments with their corresponding argv list position to std out
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

	# return position of user specified argument in the argument list
	def _getArgPosition(self, test_arg):
		if ( self.argv ):
			if test_arg in self.argv:
				return self.argv.index(test_arg)
			else:
				return -1

	# return the argument at the next position following a user specified positional argument (e.g. for argument to an option in cmd)
	def _getArgNext(self, position):
		if len(self.argv) > (position + 1):
			return self.argv[position + 1]
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
