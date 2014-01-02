#!/usr/bin/env python

#------------------------------------------------------------------------------
# The Ink Templating System
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
		obj.varlist = obj._make_var_list(template_text)
		return obj

	def _make_var_list(self, template_text):
		open_match_pat = self._escape_regex_special_chars(self.odel)
		close_match_pat = self._escape_regex_special_chars(self.cdel)
		match_pat = open_match_pat + r'(.*?)' + close_match_pat
		re_pat = re.compile(match_pat)
		var_list = re_pat.findall(template_text)
		return var_list

	def _escape_regex_special_chars(self, test_escape_string):
		return re.escape(test_escape_string)

#------------------------------------------------------------------------------
# Renderer class
#  Render the variable replacements in the ink template with a Python dictionary key
#------------------------------------------------------------------------------

class Renderer:
	def __init__(self, template, key):
		self.odel = template.odel
		self.cdel = template.cdel
		self.template = template
		self.key_dict = key

	def render(self):
		local_template = self.template
		for key, value in self.key_dict.iteritems():
			if key in self.template.varlist:
				replace_string = self.odel + key + self.cdel
				local_template = local_template.replace(replace_string, value)
		return local_template


if __name__ == '__main__':
	t = Template("A {{thing}} {{name}} has a {{attribute}} example {{attribute}}")
	r = Renderer(t, {"thing":"dog", "name":"Naked", "attribute":"cool"})
	print(r.render())
