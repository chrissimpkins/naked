#!/usr/bin/env python
# encoding: utf-8

import Naked.settings

class Usage:
    def __init__(self):
        self.usage = Naked.settings.usage
        self.name = Naked.settings.app_name

    def print_usage(self):
        usage_string = "Usage: " + self.name + " " + self.usage
        print(usage_string)


if __name__ == '__main__':
    pass
