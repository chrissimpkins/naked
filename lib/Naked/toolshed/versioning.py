#!/usr/bin/env python

from Naked.settings import major_version as major_version
from Naked.settings import minor_version as minor_version
from Naked.settings import patch_version as patch_version

class VersionEditor:
	def __init__(self):
		self.app_version = major_version + "." + minor_version + "." + patch_version

	def get_version(self):
		return self.app_version

	def bump_version_patch(self):
		pass

	def bump_version_minor(self):
		pass

	def bump_version_major(self):
		pass
