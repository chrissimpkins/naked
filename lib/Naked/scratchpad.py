#!/usr/bin/env python
# encoding: utf-8

from functools import wraps

def print_scratch(func):
    @wraps(func)
    def print_wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return print_wrapper


@print_scratch
def run_scratchpad():
    from Naked.toolshed.file import FileReader

    r = FileReader('/Users/ces/Desktop/code/naked/tests/testfiles/ascii.txt')
    test = r.read_utf8()
    return type(test)



if __name__ == '__main__':
    run_scratchpad()
