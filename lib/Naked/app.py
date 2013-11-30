#!/usr/bin/env python

def main():
    import sys
    import Naked.commandline
	# TODO: wrap in a try/catch block
    c = Naked.commandline.Command(sys.argv[0], sys.argv[1:])
    if c.cmd == "test":
        if ( c.option("-l") and c.arg("-l") ):
            print(c.arg("-l"))
        else:
            print("Not found")
        #if c.option("-t"): c.truth = True
        #print(c.truth)
    elif c.cmd == "bump":
        if c.cmd2 == "patch":
            pass
        elif c.cmd2 == "minor":
            pass
        elif c.cmd2 == "major":
            pass
    elif c.help():
        from Naked.commands.help import Help
        Help().print_help()
    elif c.usage():
        from Naked.commands.usage import Usage
        Usage().print_usage()
    elif c.version():
        from Naked.commands.version import Version
        Version().print_version()
    elif c.cmd == "nakedtest":
        pass
    else:
        print("Could not parse the command that you entered.  Please try again.")

if __name__ == '__main__':
	main()
