#!/usr/bin/env python

from Naked.settings import version as App_Version

class VersionEditor:
	def __init__(self):
		self.app_version = App_Version

	def get_version(self):
		return self.app_version

	def bump_version_patch(self):
		pass

	def bump_version_minor(self):
		pass

	def bump_version_major(self):
