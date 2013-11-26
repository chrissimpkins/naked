#!/usr/bin/env python

import sys
import Naked.commandline

def main():
    Naked.commandline.Run(sys.argv[1:])

if __name__ == '__main__':
	main(sys.argv[1:])
