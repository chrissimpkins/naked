#!/usr/bin/env python
# encoding: utf-8

import sys
from functools import wraps
from Naked.toolshed.types import NakedObject, XList

def print_scratch(func):
    @wraps(func)
    def print_wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return print_wrapper


def run_scratchpad():
    # from Naked.toolshed.file import FileReader
    # from Naked.toolshed.types import XString, XUnicode

    # r = FileReader('/Users/ces/Desktop/code/naked/tests/testfiles/unicode.txt')
    # test1 = r.read_utf8()
    # test2 = XUnicode(test1, {'a': 'b'})
    # test3 = "Hey! It's Bengali ব য,and here is some more ২"
    # print(unicode(test2))

    xl = XList([1, 2, 3], {'first_attr': 1})
    xl2 = XList([4, 5])
    xl3 = XList([6, 7])
    for x in xl.chain_iter(xl2, xl3):
        print(x)


if __name__ == '__main__':
    run_scratchpad()
