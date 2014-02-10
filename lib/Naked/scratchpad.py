#!/usr/bin/env python
# encoding: utf-8

from functools import wraps

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

    from Naked.toolshed.network import HTTP

    http = HTTP('bogus.com')
    if http.get():
        status = http.res.status_code
    else:
        fail_status = http.res.status_code



if __name__ == '__main__':
    run_scratchpad()
