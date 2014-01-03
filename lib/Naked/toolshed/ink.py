#!/usr/bin/env python

#------------------------------------------------------------------------------
# The Ink Templating System
#  A lightweight, flexible text templating system
# Copyright 2014 Christopher Simpkins
# MIT License
#------------------------------------------------------------------------------
import re

#------------------------------------------------------------------------------
# Template class
#  A template string class that is inherited from Python str
#  Includes metadata about the template:
#    odel = opening delimiter
#    cdel = closing delimiter
#    varlist = inclusive list of all variables in the template text (parsed in constructor)
#  Delimiters:
#    default = {{variable}}
#    assign new opening and closing delimiters as parameters when you make a new Template instance
#------------------------------------------------------------------------------
class Template(str):
	def __new__(cls, template_text, open_delimiter="{{", close_delimiter="}}"):
		obj = str.__new__(cls, template_text)
		obj.odel = open_delimiter
		obj.cdel = close_delimiter
		obj.varlist = obj._make_var_list(template_text) #contains all parsed variables from the template in a list
		return obj

	#------------------------------------------------------------------------------
	# [ _make_var_list method ] (list of strings)
	#   Private method that parses the template string for all variables that match the delimiter pattern
	#   Returns a list of the variable names as strings
	#------------------------------------------------------------------------------

	def _make_var_list(self, template_text):
		open_match_pat = self._escape_regex_special_chars(self.odel)
		close_match_pat = self._escape_regex_special_chars(self.cdel)
		match_pat = open_match_pat + r'(.*?)' + close_match_pat # capture group contains the variable name used between the opening and closing delimiters
		re_pat = re.compile(match_pat)
		var_list = re_pat.findall(template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
		return var_list

	#------------------------------------------------------------------------------
	# [ _escape_regex_special_chars method ] (string)
	#   Private method that escapes special regex metacharacters
	#   Returns a string with the escaped character modifications
	#------------------------------------------------------------------------------
	def _escape_regex_special_chars(self, test_escape_string):
		return re.escape(test_escape_string)

#------------------------------------------------------------------------------
# Renderer class
#  Render the variable replacements in the ink template using a Python dictionary key argument
#  Construct the instace of the Renderer with the Ink template and the dictionary key
#  Run the renderer with the render method on the instance (e.g. r.render())
#  Parameters to constructor:
#    - template = an Ink Template instance
#	 - key = a dictionary mapped key = variable name : value = variable replacement data
#    - html_entities = encode html entities with HTML escaped characters (default = False = do not encode)
#------------------------------------------------------------------------------

class Renderer:
	def __init__(self, template, key, html_entities=False):
		self.odel = template.odel
		self.cdel = template.cdel
		self.template = template
		self.html_entities = html_entities
		self.key_dict = key

	#------------------------------------------------------------------------------
	# [ render method ] (string)
	#   renders the variable replacements in the Ink template
	#   returns the rendered template as a string
	#------------------------------------------------------------------------------
	def render(self):
		local_template = self.template
		for key in self.key_dict:
			if key in self.template.varlist:
				value = self.key_dict[key]
				replace_string = self.odel + key + self.cdel
				if self.html_entities:
					from xml.sax.saxutils import escape #from Python std lib
					value = escape(value)
				local_template = local_template.replace(replace_string, value)
		return local_template


if __name__ == '__main__':
	pass
	# t = Template("A {{thing}} {{name}} has a {{attribute}} example {{attribute}}")
	# r = Renderer(t, {"thing":"dog", "name":"Naked", "attribute":"cool"})
	# r.render()
