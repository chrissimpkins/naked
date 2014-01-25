#!/usr/bin/env python
# encoding: utf-8

import os
import json
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

    #------------------------------------------------------------------------------
    # Constructors
    #------------------------------------------------------------------------------
    def test_http_constructor(self):
        """Test default HTTP class constructor"""
        http = HTTP("http://www.google.com")

    def test_http_constructor_with_change_timeout(self):
        """Test HTTP class constructor with change in default timeout duration"""
        http = HTTP("http://www.google.com", 20)


    #------------------------------------------------------------------------------
    # GET request tests
    #------------------------------------------------------------------------------
    def test_http_get(self):
        """Test HTTP get request content data"""
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

    def test_http_response_none(self):
        """Test that the HTTP response is None before the run of a HTTP method"""
        http = HTTP('http://google.com')
        self.assertEqual(None, http.res)

    def test_http_get_response_change(self):
        """Confirm that the response object is changed from None after a HTTP GET method"""
        http = HTTP("http://www.google.com")
        http.get()
        self.assertNotEqual(None, http.res)

    def test_http_get_response_check_200(self):
        """Confirm that the response object contains 200 status code"""
        http = HTTP('http://httpbin.org/status/200')
        http.get()
        self.assertEqual(http.res.status_code, 200) # test the response object attribute
        response = http.response()
        self.assertEqual(response.status_code, 200) # test the returned object from the response() method

    def test_http_get_response_check_301(self):
        """Confirm that the reponse object contains 301 status code when do not follow redirects"""
        http = HTTP('http://httpbin.org/status/301')
        http.get(False) # do not follow redirects
        self.assertEqual(http.res.status_code, 301)
        response = http.response()
        self.assertEqual(response.status_code, 301)

    def test_http_get_response_check_404(self):
        """Confirm that the response object contains a 404 status code when authentication required"""
        http = HTTP('http://httpbin.org/status/404')
        http.get()
        self.assertEqual(http.res.status_code, 404)
        response = http.response()
        self.assertEqual(response.status_code, 404)

    def test_http_get_status_check_true(self):
        """Confirm the truth check for status response code OK (=200) is True when should be true"""
        http = HTTP('http://httpbin.org/status/200')
        self.assertEqual(http.get_status_ok(), True)
        self.assertEqual(http.res.status_code, 200) #confirm that the response object is set after the get_status_ok() call


    def test_http_get_status_check_false(self):
        """Confirm the truth check for status response code OK is False for non-existent site"""
        http = HTTP('http://www.abogussitename.com')
        self.assertEqual(http.get_status_ok(), False)
        self.assertEqual(http.res, None) # confirm that the response object is None when site does not exist

    def test_http_get_status_ssl(self):
        """Confirm that GET request for a https domain returns appropriate status code"""
        http = HTTP('https://httpbin.org/status/200')
        http.get()
        self.assertEqual(http.res.status_code, 200)

    def test_http_get_status_ssl_redirect(self):
        """Confirm that GET request for a https domain returns appropriate 301 status code when redirects"""
        http = HTTP('https://httpbin.org/status/301')
        http.get(False) # do not allow redirects in order to capture this code
        self.assertEqual(http.res.status_code, 301)

    #------------------------------------------------------------------------------
    # POST Tests
    #------------------------------------------------------------------------------

    def test_http_post(self):
        """Test HTTP POST request content data"""
        http = HTTP("http://httpbin.org/post")
        http_text = http.post()
        response = http.response()
        self.assertEqual(response.url, 'http://httpbin.org/post')

    def test_http_post_ssl(self):
        """Test HTTP POST request content data"""
        http = HTTP("https://httpbin.org/post")
        http_text = http.post()
        response = http.response()
        self.assertEqual(response.url, 'https://httpbin.org/post')

    def test_http_post_binary_file(self):
        """Test HTTP POST request binary file write"""
        http = HTTP("http://httpbin.org/gzip")
        http_data_write = http.post_bin_write_file(os.path.join('testfiles', 'testdir', 'post.gz'))
        self.assertEqual(True, http_data_write) #test boolean for confirmation of data write
        self.assertEqual(True, file_exists(os.path.join('testfiles', 'testdir', 'post.gz')))

    def test_http_post_text_file(self):
        """Test HTTP POST request text file write"""
        http = HTTP("http://httpbin.org/post")
        http_text = http.post_txt_write_file(os.path.join('testfiles', 'testdir', 'post.txt'))
        fr = FileReader(os.path.join('testfiles', 'testdir', 'post.txt'))
        the_text = fr.read_utf8() #read file in
        textobj = json.loads(the_text) #convert JSON to Py object
        self.assertEqual(True, http_text) # test boolean for confirmation of data write
        self.assertEqual(textobj['url'], 'http://httpbin.org/post') #confirm the write of subset of the text

    def test_http_post_response_changes(self):
        """Test that the reponse object on the HTTP instance changes after POST request"""
        http = HTTP("http://httpbin.org/post")
        http.post()
        self.assertNotEqual(None, http.res)

    def test_http_post_reponse_status_200(self):
        """Test that the status code 200 is appropriately detected after a POST request"""
        http = HTTP("http://httpbin.org/post")
        http.post()
        self.assertEqual(http.res.status_code, 200)

    def test_http_post_response_status_200_ssl(self):
        """Test that the status code 200 is appropriately detected after a SSL POST request"""
        http = HTTP("https://httpbin.org/post")
        http.post()
        self.assertEqual(http.res.status_code, 200)

    def test_http_post_status_check_true(self):
        """Test that the status check returns True for POST request when it should return True"""
        http = HTTP('http://httpbin.org/post')
        result = http.post_status_ok()
        self.assertEqual(True, result)

    def test_http_post_status_check_false(self):
        """Test that the status check returns False for POST requst when the site does not exist"""
        http = HTTP('http://www.atrulybogussite.com')
        result = http.post_status_ok()
        self.assertEqual(False, result)
    #------------------------------------------------------------------------------
    # HEAD tests
    #------------------------------------------------------------------------------

    def test_http_head(self):
        """Test HTTP head response"""
        http = HTTP("http://www.google.com")
        head = http.head()
        self.assertEqual(head['content-type'], "text/html; charset=ISO-8859-1")

    def test_http_head_ssl(self):
        """Test HTTP head response with SSL"""
        http = HTTP("https://www.google.com")
        head = http.head()
        self.assertEqual(head['content-type'], "text/html; charset=ISO-8859-1")

