#!/usr/bin/env python
# encoding: utf-8

# VARS = --none--
profiler_file_string = """
#!/usr/bin/env python
# encoding: utf-8

import cProfile, pstats, StringIO

def profile():
    #------------------------------------------------------------------------------
    # Setup a profile
    #------------------------------------------------------------------------------
    pr = cProfile.Profile()
    #------------------------------------------------------------------------------
    # Enter setup code below
    #------------------------------------------------------------------------------
        # Optional: include setup code below


    #------------------------------------------------------------------------------
    # Start profiler
    #------------------------------------------------------------------------------
    pr.enable()

    #------------------------------------------------------------------------------
    # Enter code to be profiled below
    #------------------------------------------------------------------------------
        # include profiled code here


    #------------------------------------------------------------------------------
    # End profiler & print results to std out - do not modify below
    #------------------------------------------------------------------------------
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.strip_dirs().sort_stats("time").print_stats()
    print(s.getvalue())

if __name__ == '__main__':
    profile()
"""
