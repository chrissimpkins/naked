#!/usr/bin/env python

import unittest
from Naked.toolshed.network import HTTP
from Naked.toolshed.state import StateObject
state = StateObject()

class NakedCommandParseTest(unittest.TestCase):

	def setUp(self):

		self.http_string = """The MIT License (MIT)

Copyright (c) 2013 Chris Simpkins

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

	def tearDown(self):
		pass

	def test_http_constructor(self):
		"""Test default HTTP class constructor"""
		http = HTTP("http://www.google.com")

	def test_http_constructor_with_change_timeout(self):
		"""Test HTTP class constructor with change in default timeout duration"""
		http = HTTP("http://www.google.com", 20)

	def test_http_get(self):
		"""Test HTTP get request"""
		http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
		http_text = http.get()

		if state.py2:
			self.http_string = unicode(self.http_string)
		self.assertEqual(http_text.strip(), self.http_string.strip())






