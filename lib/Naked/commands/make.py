#!/usr/bin/env python
# encoding: utf-8

import Naked.toolshed.system as system
import Naked.toolshed.python as python
import Naked.toolshed.file as nfile
import Naked.toolshed.ink as ink
import datetime
import sys

## TODO: Check for a local settings file (appname.yaml)
## TODO: make directories and files
#------------------------------------------------------------------------------
# [ MakeController class ]
#   Top level logic for the make command
#------------------------------------------------------------------------------
class MakeController:
	def __init__(self, app_name):
		self.app_name = app_name

	def run(self):
		if self.app_name == None:
			i = InfoCompiler(None)
			data_container = i.getSetupFileInfo()
		else:
			i = InfoCompiler(self.app_name)
			data_container = i.getUserInfo()

		db = DirectoryBuilder(data_container)
		db.build()
		# fb = FileBuilder(data_container)
		# fb.build()

#------------------------------------------------------------------------------
# [ InfoCompiler class ]
#  obtain information from user in order to build a new project
#------------------------------------------------------------------------------
class InfoCompiler:
	def __init__(self, app_name):
		self.data = DataContainer()
		self.data.app_name = app_name
		self.displayed_info_flag = 0

	def getUserInfo(self):
		if not self.displayed_info_flag:
			print("We need some information to create your project.")
			self.displayed_info_flag = 1
		# If no project name, then query for it because this is mandatory
		if self.data.app_name == None:
			if python.is_py2:
				response = raw_input("Please enter your application name (q=quit): ")
			else:
				response = input("Please enter your application name (q=quit): ")
			if len(response) > 0:
				if response == "q":
					print("Aborted project build.")
					sys.exit(0) # user requested quit
				else:
					if len(response.split()) > 1: # if more than one word
						print("The application name must be a single word.  Please try again.")
						self.getUserInfo()
					else:
						self.data.app_name = response
			else:
				print("The Naked project will not build without an application name.  Please try again.")
				return self.getUserInfo()
		# if project name already set, then obtain the other optional information
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
			return self.getUserInfo() # try again

	def getSetupFileInfo(self):
		files = system.list_all_files_cwd()
		if len(files) > 0:
			setupfile_exists = False
			for a_file in files:
				if 'naked.yaml' == a_file.lower(): # accepts any permutation of upper/lower case 'naked.yaml'
					print("Detected a Naked project YAML setup file (" + a_file + ").")
					setupfile_exists = True
					fr = nfile.FileReader(a_file)
					the_yaml = fr.read_utf8()
					self.parseYaml(the_yaml)
			if setupfile_exists:
				if self.confirmData():
					return self.data
				else:
					print("Aborted the project build.")
					if python.is_py2():
						response = raw_input("Would you like to modify this information? (y/n) ")
					else:
						response = input("Would you like to modify this information? (y/n) ")
					if response in ['y', 'Y', 'Yes', 'YES', 'yes']:
						self.displayed_info_flag = 1
						self.data.app_name = None
						return self.getUserInfo() # return the result from the getUserInfo command to the calling method
					else:
						sys.exit(0)
			else:
				return self.getUserInfo() # there are files but no setup file, use the manual entry method
		else:
			return self.getUserInfo() # there are no files in the directory, use the manual entry method


	def parseYaml(self, yaml_string):
		import yaml
		the_yaml = yaml.load(yaml_string)
		# Parse project name
		if 'application' in the_yaml:
			self.data.app_name = the_yaml['application']
		else:
			print("Unable to find the application name ('application' field) in naked.yaml")
			if python.is_py2:
				response = raw_input("Please enter your application name: ")
			else:
				response = input("Please enter your application name: ")
			if len(response) > 0:
				self.data.app_name = response # assign the application name at CL if was not entered in file
			else:
				print("The Naked project will not build without an application name.  Please try again.")
				self.displayed_info_flag = 1
				self.getUserInfo()
		# Parse developer
		if 'developer' in the_yaml:
			self.data.developer = the_yaml['developer'] # set developer
		else:
			self.data.developer = ""
		# Parse license type
		if 'license' in the_yaml:
			self.data.license = the_yaml['license'] # set license
		else:
			self.data.license = ""


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
			self.data.app_name = None
			return False

#------------------------------------------------------------------------------
# [ getHeaderTemplate function ] (string)
#  returns the Ink header template for user confirmation
#------------------------------------------------------------------------------
def getHeaderTemplate():
	templ_str = """
----------------------------------------------------------
 {{app_name}}
 Copyright {{year}} {{developer}}
 {{license}}
----------------------------------------------------------
	"""
	return templ_str

#------------------------------------------------------------------------------
# [ DataContainer class ]
#   state maintenance object that holds project information
#------------------------------------------------------------------------------
class DataContainer:
	def __init__(self):
		self.cwd = system.cwd()
		self.year = str(datetime.datetime.now().year)

#------------------------------------------------------------------------------
# [ DirectoryBuilder class ]
#   generation of directory structure for a new project
#------------------------------------------------------------------------------
class DirectoryBuilder:
	def __init__(self, data_container):
		self.data_container = data_container

	def build(self):
		from Naked.toolshed.system import make_dirs, make_path

		top_level_dir = self.data_container.app_name
		second_level_dirs = ['docs', 'lib', 'tests']
		lib_subdir = make_path(self.data_container.app_name, 'commands')

		for xdir in second_level_dirs:
			make_dirs(make_path(top_level_dir, xdir))

		make_dirs(make_path(top_level_dir, 'lib', lib_subdir))




#------------------------------------------------------------------------------
# [ FileBuilder class ]
#  generate the files for a new project
#------------------------------------------------------------------------------
class FileBuilder:
	def __init__(self, data_container):
		self.data_container = data_container

	def build():
		pass

	def make_file_paths():
		from Naked.toolshed.system import make_path

		self.top_manifestin = make_path(self.data_container.app_name, 'MANIFEST.in')
		self.top_readmemd = make_path(self.data_container.app_name, 'README.md')
		self.top_setupcfg = make_path(self.data_container.app_name, 'setup.cfg')
		self.top_setuppy = make_path(self.data_container.app_name, 'setup.py')
		self.docs_license = make_path(self.data_container.app_name, 'docs', 'LICENSE')
		self.docs_readmerst = make_path(self.data_container.app_name, 'docs', 'README.rst')
		self.lib_initpy = make_path(self.data_container.app_name, 'lib', '__init__.py')
		self.lib_profilerpy = make_path(self.data_container.app_name, 'lib', 'profiler.py')
		self.lib_proj_initpy = make_path(self.data_container.app_name, 'lib', self.data_container.app_name, '__init__.py')
		self.lib_proj_apppy = make_path(self.data_container.app_name, 'lib', self.data_container.app_name, 'app.py')
		self.lib_proj_settingspy = make_path(self.data_container.app_name, 'lib', self.data_container.app_name, 'settings.py')

	def get_template(self, template):
		pass

	def make_template(self, template_string):
		pass

	def render_template(self, template):
		pass


if __name__ == '__main__':
	pass
