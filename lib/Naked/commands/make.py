#!/usr/bin/env python
# encoding: utf-8

import Naked.toolshed.system as system
import Naked.toolshed.python as python
import Naked.toolshed.ink as ink
import datetime
import sys

class MakeController:
	def __init__(self, app_name):
		i = InfoCompiler(app_name)
		data_container = i.getUserInfo()
		print(data_container.__dict__)

class InfoCompiler:
	def __init__(self, app_name):
		self.data = DataContainer()
		self.data.app_name = app_name
		self.displayed_info_flag = 0

	def getUserInfo(self):
		if not self.displayed_info_flag:
			print("We need some information to generate your project.")
			self.displayed_info_flag = 1
		if python.is_py2():
			self.data.developer = raw_input("Enter the licensing developer or organization (q=quit): ")
			if self.data.developer == "q":
				print("Aborted the project build.")
				sys.exit(0)
			self.data.license = raw_input("Enter the license type (or leave blank, q=quit): ")
			if self.data.license == "q":
				print("Aborted the project build.")
				sys.exit(0)
		else:
			self.data.developer = input("Enter the licensing developer or organization: ")
			if self.data.developer == "q":
				print("Aborted the project build.")
				sys.exit(0)
			self.data.license = input("Enter the license type (or leave blank): ")
			if self.data.license == "q":
				print("Aborted the project build.")
				sys.exit(0)
		if self.confirmData():
			return self.data
		else:
			print("Let's try again...")
			self.getUserInfo() # try again

	def confirmData(self):
		templ_str = getHeaderTemplate()
		template = ink.Template(templ_str)
		renderer = ink.Renderer(template, {'app_name': self.data.app_name, 'developer': self.data.developer, 'license': self.data.license, 'year': self.data.year})
		display_header = renderer.render()
		print("\nPlease confirm the information below:")
		print(display_header)

		if python.is_py2():
			response = raw_input("Is this correct? (y/n) ")
		else:
			response = input("Is this correct? (y/n) ")

		if response in ['y', 'Y', 'yes', 'YES']:
			return True
		else:
			return False

def getHeaderTemplate():
	templ_str = """
----------------------------------------------------------
 {{app_name}}
 Copyright {{year}} {{developer}}
 {{license}}
----------------------------------------------------------
	"""
	return templ_str


class DataContainer:
	def __init__(self):
		self.cwd = system.cwd()
		self.year = str(datetime.datetime.now().year)

class DirectoryBuilder:
	pass

class FileBuilder:
	pass


if __name__ == '__main__':
	pass
