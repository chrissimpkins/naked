#!/usr/bin/env python

import os
import unittest
from Naked.toolshed.network import HTTP
from Naked.toolshed.state import StateObject
from Naked.toolshed.system import file_exists
from Naked.toolshed.file import FileReader
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

	def test_http_get_binary(self):
		"""Test HTTP get request with a binary file"""
		http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
		http.get_bin_write_file(os.path.join('testfiles', 'testdir', 'test.tar.gz'))
		self.assertTrue(file_exists(os.path.join('testfiles', 'testdir', 'test.tar.gz')))

	def test_http_get_text(self):
		"""Test HTTP get request for text data and write of text file"""
		http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
		response = http.get_txt_write_file(os.path.join('testfiles', 'testdir', 'test.txt'))
		fr = FileReader(os.path.join('testfiles', 'testdir', 'test.txt'))
		the_dl_text = fr.read()
		self.assertEqual(the_dl_text.strip(), self.http_string.strip()) #test that the file write is appropriate
		self.assertEqual(response, True) # test that the response from the method is correct (True on completed file write)

	def test_http_head(self):
		"""Test HTTP head response"""
		http = HTTP("http://www.google.com")
		head = http.head()
		self.assertEqual(head['content-type'], "text/html; charset=ISO-8859-1")

	def test_http_response_none(self):
		"""Test that the HTTP response is None before the run of a HTTP method"""
		http = HTTP('http://google.com')
		self.assertEqual(None, http.res)

	def test_http_get_response_change(self):
		"""Confirm that the response object is changed from None after a HTTP GET method"""
		http = HTTP("http://www.google.com")
		http.get()
		self.assertNotEqual(None, http.res)

	def test_http_post_reponse_change(self):
		"""Confirm that the reponse object is changed from None after a HTTP POST method"""
		http = HTTP('http://www.google.com')
		http.post()
		self.assertNotEqual(None, http.res)

	def test_http_get_response_check(self):
		"""Confirm that the response object contains appropriate returned data"""
		http = HTTP('http://www.google.com')
		http.get()
		self.assertEqual(http.res.status_code, 200) # test the response object attribute
		response = http.response()
		self.assertEqual(response.status_code, 200) # test the returned object from the response() method

	def test_http_get_status_check_true(self):
		"""Confirm the truth check for status response code OK (=200) is True when should be true"""
		http = HTTP('http://www.google.com')
		self.assertEqual(http.get_status_ok(), True)
		self.assertEqual(http.res.status_code, 200) #confirm that the response object is set after the get_status_ok() call


	def test_http_get_status_check_false(self):
		"""Confirm the truth check for status response code OK is False for non-existent site"""
		http = HTTP('http://www.abogussitename.com')
		self.assertEqual(http.get_status_ok(), False)
		self.assertEqual(http.res, None) # confirm that the response object is None when site does not exist









