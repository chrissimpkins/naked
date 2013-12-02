#!/usr/bin/env python


import os.path

class PathMaker:
	def __init__(self):
		pass

	# get the path to the calling script file
	def get_path_to_me(self):
		return os.path.dirname(__file__)

	# make an OS independent file path string from sequential arguments to this function
	def make_os_independent_path(self, *path_list):
		return os.path.join(*path_list)

if __name__ == '__main__':
	pass
	# pm = PathMaker()
	# thepath = pm.get_path_to_me()
	# newpath = pm.make_os_independent_path(thepath, "test", "new")
	# print(newpath)
