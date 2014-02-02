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
    from Naked.toolshed.ink import Template, Renderer
    #------------------------------------------------------------------------------
    # Start profiler
    #------------------------------------------------------------------------------
    pr.enable()

    #------------------------------------------------------------------------------
    # Enter code to be profiled below
    #------------------------------------------------------------------------------
        # include profiled code here
    for x in range(50000):
        template = Template("This is a of the {{test}} of the {{document}} {{type}} and more of the {{test}} {{document}} {{type}}")
        renderer = Renderer(template, {'test': 'ব য', 'document':'testing document', 'type':'of mine', 'bogus': 'bogus test'})
        renderer.render()

    #------------------------------------------------------------------------------
    # End profiled code
    #------------------------------------------------------------------------------
    pr.disable()
    s = StringIO.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.strip_dirs().sort_stats("time").print_stats()
    print(s.getvalue())

if __name__ == '__main__':
    profile()
