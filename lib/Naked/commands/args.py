#!/usr/bin/env python
# encoding: utf-8

from Naked.commandline import Command

class Args:
    def __init__(self, command_string):
        self.com_string = command_string

    def run(self):
        cmd_list = self.com_string.split()
        c = Command(cmd_list[0], cmd_list[1:])
        print(' ')
        print("Assuming that your Command object is instantiated as an instance named 'c', the command that you entered would be parsed as follows:")
        print(' ')
        print('Application')
        print('-----------')
        print('c.app = ' + c.app)
        print(' ')
        print('Argument List Length')
        print('--------------------')
        print('c.argc = ' + str(c.argc))
        print(' ')
        print('Argument List Items')
        print('-------------------')
        print('c.argobj = ' + str(c.argobj))
        print(' ')
        print('Arguments by Zero Indexed Start Position')
        print('----------------------------------------')
        print('c.arg0 = ' + c.arg0)
        print('c.arg1 = ' + c.arg1)
        print('c.arg2 = ' + c.arg2)
        print('c.arg3 = ' + c.arg3)
        print('c.arg4 = ' + c.arg4)
        print(' ')
        print('Arguments by Named Position')
        print('---------------------------')
        print('c.first = ' + c.first)
        print('c.second = ' + c.second)
        print('c.third = ' + c.third)
        print('c.fourth = ' + c.fourth)
        print('c.fifth = ' + c.fifth)
        print(' ')
        print('Last Positional Argument')
        print('------------------------')
        print('c.arglp = ' + c.arglp)
        print('c.last = ' + c.last)
        print(' ')
        print('Primary & Secondary Commands')
        print('----------------------------')
        print('c.cmd = ' + c.cmd)
        print('c.cmd2 = ' + c.cmd2)
        print(' ')
        print('Option Exists Test')
        print('------------------')
        print('c.option_exists() = ' + str(c.option_exists()))
        print(' ')
        print('Option Argument Assignment')
        print('--------------------------')
        if c.option_exists(): # if there are options, iterate through and print arguments to them
            for x in range(len(c.optobj)):
                if '=' in c.optobj[x]:
                    continue # don't print flags, they are handled below
                else:
                    print('c.arg("' + c.optobj[x] + '") = ' + c.arg(c.optobj[x]))
        else: # otherwise, inform user that there are no options
            print("There are no short options, long options, or flags in your command.")
        print(' ')
        print('Flag Argument Assignment')
        print('------------------------')
        flags_present = False # indicator for presence of flags in the options list
        if c.option_exists():
            for y in c.optobj:
                if '=' in y:
                    the_flag = y.split('=')[0]
                    print('c.flag_arg("' + the_flag + '") = ' + c.flag_arg(the_flag))
                    flags_present = True
        if not flags_present: # provide message if there are no flags
            print("There are no flag style arguments (--flag=argument) in your command.")


#------------------------------------------------------------------------------
# [ help function ] - help for the where command
#------------------------------------------------------------------------------
def help():
    pass

if __name__ == '__main__':
	pass
