#!/usr/bin/env python

import Naked.settings

class Help:
    def __init__(self):
        self.help = Naked.settings.help

    def print_help(self):
        print(self.help)


if __name__ == '__main__':
    pass
