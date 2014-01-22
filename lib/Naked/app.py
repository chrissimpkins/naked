#!/usr/bin/env python
# encoding: utf-8

#------------------------------------------------------------------------------
# Naked | A Python command line application framework
# Copyright 2014 Christopher Simpkins
# MIT License
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
# c.cmd = Primary command (<executable> <primary command>)
# c.cmd2 = Secondary command (<executable> <primary command> <secondary command>)
#
# c.option(option_string, [bool argument_required]) = test for option with optional test for positional arg to the option
# c.option_with_arg(option_string) = test for option and mandatory positional argument to option test
# c.flag(flag_string) = test for presence of a "--option=argument" style flag
#
# c.arg(arg_string) = returns the next positional argument to the arg_string argument
# c.flag(flag_string) = returns the flag assignment for a "--option=argument" style flag
#------------------------------------------------------------------------------------

# Application start
def main():
    import sys
    from Naked.commandline import Command
    from Naked.toolshed.state import StateObject

    #------------------------------------------------------------------------------------------
    # [ Instantiate command line object ]
    #   used for all subsequent conditional logic in the CLI application
    #------------------------------------------------------------------------------------------
    c = Command(sys.argv[0], sys.argv[1:])

    state = StateObject()
    #------------------------------------------------------------------------------------------
    # [ Command Suite Validation ] - early validation of appropriate command syntax
    # Test that user entered a primary command, print usage if not
    #------------------------------------------------------------------------------------------
    if not c.command_suite_validates():
        from Naked.commands.usage import Usage
        Usage().print_usage()
        sys.exit(1)
    #------------------------------------------------------------------------------------------
    # [ PRIMARY COMMAND LOGIC ]
    #   Test for primary commands and handle them
    #------------------------------------------------------------------------------------------
    if c.cmd == "build":
        from Naked.commands.build import compile_c_code
        import os, inspect
        abs_dirpath = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "toolshed", "c")
        compile_c_code(abs_dirpath) # function calls exit status code
    elif c.cmd == "test":
        import Naked.templates.licenses as licenses
        print()
        #if c.option("-t"): c.truth = True
        #print(c.truth)
    elif c.cmd == "dl":
        from Naked.toolshed.network import HTTP
        http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
        http.get_bin_write_file("test.tgz")
    elif c.cmd == "loc":
        from Naked.toolshed.system import cwd
        print(cwd())
        import os
        print(os.path.expanduser(os.path.join("~", "naked", "universal_settings.yaml")))
    elif c.cmd == "yaml":
        import yaml
        doc = """
        developer: Christopher Simpkins
        email: chris@zerolabs.net
        default_license: MIT
        base_repository: http://github.com/chrissimpkins
        """
        theyam = yaml.load(doc)
        print(theyam['developer'])
        print(theyam['email'])
        print(theyam['default_license'])
        print(theyam['base_repository'])
    elif c.cmd == "bump":
        if c.cmd2 == "patch":
            pass
        elif c.cmd2 == "minor":
            pass
        elif c.cmd2 == "major":
            pass
    #------------------------------------------------------------------------------------------
    # [ NAKED FRAMEWORK COMMANDS ]
    # Naked framework provides default help, usage, and version commands for all applications
    #   --> settings for user messages are assigned in the lib/PROJECT/settings.py file
    #------------------------------------------------------------------------------------------
    elif c.help():  # User requested naked help (help.py module in commands directory)
        from Naked.commands.help import Help
        Help().print_help()
    elif c.usage():  # user requested naked usage info (usage.py module in commands directory)
        from Naked.commands.usage import Usage
        Usage().print_usage()
    elif c.version(): # user requested naked version (version.py module in commands directory)
        from Naked.commands.version import Version
        Version().print_version()
    #------------------------------------------------------------------------------------------
    # [ DEFAULT MESSAGE FOR MATCH FAILURE ]
    # Message to provide to the user when all above conditional logic fails to meet a true condition
    #------------------------------------------------------------------------------------------
    else:
        print("Could not complete the command that you entered.  Please try again.")
        sys.exit(1) #exit

if __name__ == '__main__':
    main()
