#!/usr/bin/env python
# encoding: utf-8

import Naked.settings

class Usage:
    def __init__(self):
        self.usage = Naked.settings.usage

    def print_usage(self):
        print(self.usage)


if __name__ == '__main__':
    pass
