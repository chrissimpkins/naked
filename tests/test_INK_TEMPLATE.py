#!/usr/bin/env python
# coding=utf-8

import unittest
import os
from Naked.toolshed.file import FileReader
from Naked.toolshed.file import FileWriter
from Naked.toolshed.system import make_path
from Naked.toolshed.ink import Template, Renderer
from Naked.toolshed.state import StateObject
state = StateObject()

class NakedInkTemplateTest(unittest.TestCase):
	def setUp(self):
		self.template_path = make_path("testfiles", "keep", "inktests", "test_setup_template.py")
		self.template_path2 = make_path("testfiles", "keep", "inktests", "test_setup_template2.py")
		self.standard_path = make_path("testfiles", "keep", "inktests", "test_setup_standard.py")
		self.key_dictionary = {'appname':'test', 'description':'A cool app', 'url':'http://test.com', 'license':'MIT', 'author':'Christopher Simpkins', 'email':'chris@zerolabs.net'}

	def tearDown(self):
		pass

	#------------------------------------------------------------------------------
	# TEMPLATE class tests
	#------------------------------------------------------------------------------
	def test_ink_make_template_default_delimiter(self):
		"""Test default Ink template delimiter properties assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		self.assertEqual(template.odel, "{{")
		self.assertEqual(template.cdel, "}}")

	def test_ink_make_template_new_delimiters(self):
		"""Test new Ink template delimiter properties assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string, "[[", "]]", escape_regex=True)
		self.assertEqual(template.odel, "[[")
		self.assertEqual(template.cdel, "]]")

	def test_ink_make_template_new_delimiters_without_escape(self):
		"""test new Ink template delimiter properties assignment fails without proper regex escape"""
		template_string = FileReader(self.template_path).read_utf8()
		self.assertRaises(TypeError, Template(template_string, "[[", "]]"))

	def test_ink_make_template_string(self):
		"""Test new Ink template string assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		self.assertEqual(template, template_string)

	def test_ink_make_template_varlist(self):
		"""Test new Ink template variable list property assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		if state.py2:
			# pass - need to skip this for Py3.2 tests
		    self.assertEqual(template.varlist, set([u'appname', u'description', u'url', u'license', u'author', u'email'])) # convert to sets to ignore order
		else:
			self.assertEqual(template.varlist, set(['appname', 'description', 'url', 'license', 'author', 'email']))

	def test_ink_make_template_varlist_default_delim_wrong_delim(self):
		"""Test new Ink template variable list property assignment when default delimiter is incorrect"""
		template_string = FileReader(self.template_path2).read_utf8() # uses the [[ & ]] delimiters
		template = Template(template_string)
		self.assertEqual(template.varlist, set([]))

	def test_ink_make_template_varlist_new_delimiters(self):
		"""Test new Ink template variable list property assignment with new delimiters"""
		template_string = FileReader(self.template_path2).read_utf8()
		template = Template(template_string, "[[", "]]", escape_regex=True) # have to escape special regex chars
		if state.py2:
			# pass - need to skip this for Py3.2 tests
			self.assertEqual(template.varlist, set([u'appname', u'description', u'url', u'license', u'author', u'email']))
		else:
			self.assertEqual(template.varlist, set(['appname', 'description', 'url', 'license', 'author', 'email']))

	def test_ink_make_template_varlist_new_delimiter_wrong_delim(self):
		"""Test new Ink template variable list property assignment when new delimiter is wrong"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string, "[[", "]]", escape_regex=True) # have to escape special regex chars
		self.assertEqual(template.varlist, set([]))

	def test_ink_template_type_string(self):
		"""Test that Ink template is of type string"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		self.assertIsInstance(template, str)

	def test_ink_template_varlist_type_set(self):
		"""Test that the Ink template variable list is of type set"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		self.assertIsInstance(template.varlist, set)

	def test_ink_template_string_method(self):
		"""Test that a slice string method works on the Ink template"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		self.assertEqual(template[0:5], "impor")

	#------------------------------------------------------------------------------
	# RENDERER class tests
	#------------------------------------------------------------------------------
	def test_ink_renderer_default_delimiters(self):
		"""Test new Ink renderer assignment of default delimiters from the template"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		renderer = Renderer(template, self.key_dictionary)
		self.assertEqual(renderer.odel, "{{")
		self.assertEqual(renderer.cdel, "}}")

	def test_ink_renderer_new_delimiters(self):
		"""Test new Ink renderer assignment of new delimiters from the template"""
		template_string = FileReader(self.template_path2).read_utf8()
		template = Template(template_string, "[[", "]]")
		renderer = Renderer(template, self.key_dictionary)
		self.assertEqual(renderer.odel, "[[")
		self.assertEqual(renderer.cdel, "]]")

	def test_ink_renderer_template(self):
		"""Test new Ink renderer template property assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		renderer = Renderer(template, self.key_dictionary)
		self.assertEqual(renderer.template, template)

	def test_ink_renderer_template_property_string(self):
		"""Test new Ink renderer template property is a string"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		renderer = Renderer(template, self.key_dictionary)
		self.assertIsInstance(renderer.template, str)

	def test_ink_renderer_key_dictionary(self):
		"""Test new Ink renderer key_dict property"""
		template_string = FileReader(self.template_path).read_utf8()
		template = Template(template_string)
		renderer = Renderer(template, self.key_dictionary)
		self.assertEqual(renderer.key_dict, self.key_dictionary)


	def test_ink_renderer_render_default_delim(self):
		"""Test Ink render with default delimiters"""
		template_string = FileReader(self.template_path).read_utf8()
		standard_string = FileReader(self.standard_path).read_utf8()
		template = Template(template_string)
		renderer = Renderer(template, self.key_dictionary)
		rendered_doc = renderer.render()
		self.assertEqual(rendered_doc, standard_string)

	def test_ink_renderer_render_new_delim(self):
		"""Test Ink render with new delimiters"""
		template_string = FileReader(self.template_path2).read_utf8()
		standard_string = FileReader(self.standard_path).read_utf8()
		template = Template(template_string, "[[", "]]", escape_regex=True) # have to escape special regex chars
		renderer = Renderer(template, self.key_dictionary)
		rendered_doc = renderer.render()
		self.assertEqual(rendered_doc, standard_string)

	def test_ink_renderer_render_fail_with_incorrect_delim(self):
		"""Confirm that Ink renderer fails with incorrect delimiter assignment"""
		template_string = FileReader(self.template_path).read_utf8()
		standard_string = FileReader(self.standard_path).read_utf8()
		template = Template(template_string, "[[", "]]")
		renderer = Renderer(template, self.key_dictionary)
		rendered_doc = renderer.render()
		self.assertNotEqual(rendered_doc, standard_string)

    ## TODO: add tests for html entities

if __name__ == '__main__':
	pass
