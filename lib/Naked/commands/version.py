#!/usr/bin/env python

import Naked.settings

class Version:
	def __init__(self):
		self.version = Naked.settings.version
		self.name = Naked.settings.app_name

	def print_version(self):
		version_string = self.name + " " + self.version
		print(version_string)


if __name__ == '__main__':
	pass
