#!/usr/bin/env python
# encoding: utf-8

import os
from Naked.toolshed.system import stderr, exit_success

class Locator:
    def __init__(self, needle):
        self.needle = needle
        self.location = self._display_location()

    def _display_location(self):
        if self.needle == 'main':
            main_path = os.path.join('<PROJECT>', 'lib', 'app.py')
            print("app.py : " + main_path)
            exit_success()
        elif self.needle == "settings":
            settings_path = os.path.join('<PROJECT>', 'lib', 'settings.py')
            print("settings.py : " + settings_path)
            exit_success()
        elif self.needle == "setup":
            setup_path = os.path.join('<PROJECT>', 'setup.py')
            print("setup.py : " + setup_path)
            exit_success()
        else:
            stderr("Unable to process your command.  Please enter 'main', 'settings' or 'setup' as the argument to the locate command.", 1)

if __name__ == '__main__':
    pass
