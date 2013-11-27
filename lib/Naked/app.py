#!/usr/bin/env python

import sys
import Naked.commandline

def main():
	# TODO: wrap in a try/catch block
    c = Naked.commandline.Command(sys.argv[0], sys.argv[1:])
    print(c.primarycmd)
    print(c.option("--help"))
    print(c.command("new"))
    #print(command.cmd)
    #print(command.argv)
    #print(command.argc)
    #print(command.arg0)
    #print(command.arg1)
    #print(command.arglp)
    #command.show_args()

if __name__ == '__main__':
	main()
