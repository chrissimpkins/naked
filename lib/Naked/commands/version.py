#!/usr/bin/env python

import Naked.settings

class Version:
	def __init__(self):
		self.major_version = Naked.settings.major_version
		self.minor_version = Naked.settings.minor_version
		self.patch_version = Naked.settings.patch_version
		self.name = Naked.settings.app_name

	def print_version(self):
		version_string = self.name + " " + self.major_version + "." + self.minor_version + "." + self.patch_version
		print(version_string)


if __name__ == '__main__':
	pass
