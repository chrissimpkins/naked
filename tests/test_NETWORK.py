#!/usr/bin/env python
# encoding: utf-8

import os
import json
import unittest
from Naked.toolshed.network import HTTP
from Naked.toolshed.state import StateObject
from Naked.toolshed.system import file_exists
from Naked.toolshed.file import FileReader, FileWriter
state = StateObject()

class NakedNetworkTest(unittest.TestCase):

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

    def test_http_response_none(self):
        """Test that the HTTP response is None before the run of a HTTP method"""
        http = HTTP('http://google.com')
        self.assertEqual(None, http.res)

    def test_http_response_none_attribute_error(self):
        """Test that the HTTP response object is None before HTTP method run and attempt to access attribute raises exception"""
        http = HTTP('http://google.com')
        with self.assertRaises(AttributeError):
            http.res.content


    #------------------------------------------------------------------------------
    # GET request tests
    #------------------------------------------------------------------------------
    def test_http_get(self):
        """Test HTTP GET request content data"""
        http = HTTP("http://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        http_text = http.get()

        if state.py2:
            self.http_string = unicode(self.http_string)
        self.assertEqual(http_text.strip(), self.http_string.strip())

    def test_http_get_ssl(self):
        """Test HTTP GET request content data with secure HTTP"""
        http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        http_text = http.get()

        if state.py2:
            self.http_string = unicode(self.http_string)
        self.assertEqual(http_text.strip(), self.http_string.strip())

    def test_http_get_type(self):
        """Test the HTTP GET request return value type"""
        http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        http_text = http.get()

        if state.py2:
            self.assertEqual(type(u"test string"), type(http_text))
        else:
            self.assertEqual(type(str("test string")), type(http_text))

    def test_http_get_bin_type(self):
        """Test the return value type with the get_bin() method"""
        http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
        bin_data = http.get_bin()
        self.assertEqual(type(b"110"), type(bin_data))


            #------------------------------------------------------------------------------
            # The response object
            #------------------------------------------------------------------------------
    def test_http_get_response_obj_present(self):
        """Confirm that response object is set after GET request with site that exists"""
        http = HTTP('http://google.com')
        http.get()
        self.assertTrue(http.res)             # the response object
        self.assertTrue(http.res.content)     # the content of the response
        self.assertTrue(http.res.status_code) # the status code

    def test_http_get_response_obj_nonexistentsite(self):
        """Test the response object after GET request for a non-existent site"""
        http = HTTP('http://bigtimebogussite.io')
        self.assertEqual(False, http.get())
        self.assertEqual(None, http.res)
        with self.assertRaises(AttributeError):
            http.res.content
        with self.assertRaises(AttributeError):
            http.res.status_code


            #------------------------------------------------------------------------------
            # redirect handling
            #------------------------------------------------------------------------------
    def test_http_get_follow_redirects(self):
        """Confirm that the GET request follows redirects and returns 200 status code by default"""
        http = HTTP("http://httpbin.org/status/301")
        http_text = http.get()
        self.assertEqual(200, http.res.status_code)

    def test_http_get_follow_redirects_false_on_nofollow_arg(self):
        """Confirm that GET request does not follow redirect and returns non-200 status code when requested"""
        http = HTTP("http://httpbin.org/status/301")
        http_text = http.get(follow_redirects=False)
        self.assertEqual(301, http.res.status_code)

    def test_http_get_follow_redirects_false_content(self):
        """Test the contents of the returned data from the GET request when site returns non-200 status code"""
        http = HTTP("http://httpbin.org/status/301")
        http_text = http.get(follow_redirects=False)
        self.assertEqual("", http_text)


            #------------------------------------------------------------------------------
            # non-existent site handling
            #------------------------------------------------------------------------------
    def test_http_get_contents_response_missingsite(self):
        """Test the contents of the GET request response when the site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        self.assertEqual(False, http.get()) # returns False if requests ConnectionError

    def test_http_get_response_object_missingsite(self):
        """Test the GET response object returned by requests when site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        http.get()
        self.assertEqual(None, http.res)

    def test_http_get_response_content_object_missingsite(self):
        """Test the contents of the GET response object returned by requests when site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        http.get()
        with self.assertRaises(AttributeError):
            http.res.content # confirm that attempt to access the content attribute of res raises Exception when no site

    def test_http_get_response_method_return_value_missingsite(self):
        """Test the return type from response() method after GET request when non-existent site is requested"""
        http = HTTP('http://www.abogussitename.com')
        http.get()
        self.assertEqual(None, http.response())


            #------------------------------------------------------------------------------
            # file writes
            #------------------------------------------------------------------------------
    def test_http_get_binary_file_absent(self):
        """Test HTTP GET request and write to binary file when it does not exist"""
        filepath = os.path.join('testfiles', 'testdir', 'test.tar.gz')
        if file_exists(filepath):
            os.remove(filepath)
        http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
        http.get_bin_write_file(filepath)
        self.assertTrue(file_exists(filepath))

    def test_http_get_binary_file_exists(self):
        """Test HTTP GET request and write to binary file when it does exist - should not overwrite by default"""
        filepath = os.path.join('testfiles', 'keep', 'test.tar.gz')
        if not file_exists(filepath):
            raise RuntimeError("Missing test file for the unit test")
        http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
        self.assertFalse(http.get_bin_write_file(filepath)) # should not overwrite file by default

    def test_http_get_binary_file_exists_request_overwrite(self):
        """Test HTTP GET request and write binary file executes the write when the file exists and overwrite requested"""
        filepath = os.path.join('testfiles', 'testdir', 'test.tar.gz')
        fw = FileWriter(filepath)
        fw.write("test")
        if not file_exists(filepath):
            raise RuntimeError("Missing test file for the unit test")
        http = HTTP("https://github.com/chrissimpkins/six-four/tarball/master")
        http.get_bin_write_file(filepath, overwrite_existing=True)
        self.assertTrue(file_exists(filepath))

    def test_http_get_text_absent(self):
        """Test HTTP get request for text data and write of text file"""
        filepath = os.path.join('testfiles', 'testdir', 'test.txt')
        if file_exists(filepath):
            os.remove(filepath)
        http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        response = http.get_txt_write_file(filepath)
        fr = FileReader(filepath)
        the_dl_text = fr.read()
        self.assertEqual(the_dl_text.strip(), self.http_string.strip()) #test that the file write is appropriate
        self.assertEqual(response, True) # test that the response from the method is correct (True on completed file write)

    def test_http_get_text_exists(self):
        """Test HTTP GET request with text file write does not overwrite existing file by default"""
        filepath = os.path.join('testfiles', 'keep', 'file1.txt')
        if not file_exists(filepath):
            raise RuntimeError("Missing test file for the unit test.")
        http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        self.assertFalse(http.get_txt_write_file(filepath)) # should not overwrite by default

    def test_http_get_text_exists_request_overwrite(self):
        """Test HTTP GET request with text file write does overwrite existing file when requested to do so"""
        filepath = os.path.join('testfiles', 'testdir', 'test.txt')
        http = HTTP('https://raw.github.com/chrissimpkins/six-four/master/LICENSE')
        fw = FileWriter(filepath)
        fw.write("test")
        http.get_txt_write_file(filepath, overwrite_existing=True)
        self.assertEqual(FileReader(filepath).read().strip(), self.http_string.strip())

        #------------------------------------------------------------------------------
        # response status code tests
        #------------------------------------------------------------------------------
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

    def test_http_post_type(self):
        """Test the HTTP POST request return value type"""
        http = HTTP("https://raw.github.com/chrissimpkins/six-four/master/LICENSE")
        http_text = http.post()

        if state.py2:
            self.assertEqual(type(u"test string"), type(http_text))
        else:
            self.assertEqual(type(str("test string")), type(http_text))


            #------------------------------------------------------------------------------
            # non-existent site handling
            #------------------------------------------------------------------------------
    def test_http_post_contents_response_missingsite(self):
        """Test the contents of the POST request response when the site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        self.assertEqual(False, http.post()) # returns False if requests ConnectionError

    def test_http_POST_response_object_missingsite(self):
        """Test the POST response object returned by requests when site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        http.post()
        self.assertEqual(None, http.res)

    def test_http_get_response_content_object_missingsite(self):
        """Test the contents of the response object returned by requests when site is non-existent"""
        http = HTTP('http://www.abogussitename.com')
        http.post()
        with self.assertRaises(AttributeError):
            http.res.content # confirm that attempt to access the content attribute of res raises Exception when no site

    def test_http_get_response_method_return_value_missingsite(self):
        """Test the return type from response() method when non-existent site is requested"""
        http = HTTP('http://www.abogussitename.com')
        http.post()
        self.assertEqual(None, http.response())


        #------------------------------------------------------------------------------
        # file writes
        #------------------------------------------------------------------------------
    def test_http_post_binary_file_absent(self):
        """Test HTTP POST request binary file write when the file does not exist"""
        filepath = os.path.join('testfiles', 'testdir', 'post.gz')
        if file_exists(filepath):
            os.remove(filepath)
        http = HTTP("http://httpbin.org/gzip")
        http_data_write = http.post_bin_write_file(filepath)
        self.assertEqual(True, http_data_write) #test boolean for confirmation of data write
        self.assertEqual(True, file_exists(filepath))

    def test_http_post_binary_file_present(self):
        """Test HTTP POST request binary file write when file does exist - should not write by default"""
        filepath = os.path.join('testfiles', 'keep', 'test.tar.gz')
        if not file_exists(filepath):
            raise RuntimeError("Missing test file for unit test")
        http = HTTP('http://httpbin.org/gzip')
        response = http.post_bin_write_file(filepath)
        self.assertEqual(False, response)

    def test_http_post_binary_file_present_request_overwrite(self):
        """Test HTTP POST request binary file write when file does exist and request for overwrite"""
        filepath = os.path.join('testfiles', 'testdir', 'post.gz')
        if not file_exists(filepath):
            fw = FileWriter(filepath)
            fw.write('test')
        http = HTTP('http://httpbin.org/gzip')
        response = http.post_bin_write_file(filepath, overwrite_existing=True)
        self.assertEqual(True, response)
        self.assertEqual(True, file_exists(filepath))

    def test_http_post_text_file_absent(self):
        """Test HTTP POST request text file write when the file does not exist"""
        filepath = os.path.join('testfiles', 'testdir', 'post.txt')
        if file_exists(filepath):
            os.remove(filepath)
        http = HTTP("http://httpbin.org/post")
        http_text = http.post_txt_write_file(filepath)
        fr = FileReader(filepath)
        the_text = fr.read_utf8() #read file in
        textobj = json.loads(the_text) #convert JSON to Py object
        self.assertEqual(True, http_text) # test boolean for confirmation of data write
        self.assertEqual(textobj['url'], 'http://httpbin.org/post') #confirm the write of subset of the text

    def test_http_post_text_file_present(self):
        """Test HTTP POST request text file write does not occur when file already exists"""
        filepath = os.path.join('testfiles', 'keep', 'file1.txt')
        if not file_exists(filepath):
            raise RuntimeError("Missing test file for unit test")
        http = HTTP('http://httpbin.org/gzip')
        response = http.post_bin_write_file(filepath)
        self.assertEqual(False, response)

    def test_http_post_text_file_present_request_overwrite(self):
        """Test HTTP request text file write does occur when file present and request overwrite"""
        filepath = os.path.join('testfiles', 'testdir', 'post.txt')
        if not file_exists(filepath):
            fw = FileWriter(filepath)
            fw.write('test')
        http = HTTP('http://httpbin.org/gzip')
        response = http.post_bin_write_file(filepath, overwrite_existing=True)
        self.assertEqual(True, response)

        #------------------------------------------------------------------------------
        # reponse status codes
        #------------------------------------------------------------------------------
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

    # def test_http_head(self):
    #     """Test HTTP head response"""
    #     http = HTTP("http://www.google.com")
    #     head = http.head()
    #     self.assertEqual(head['content-type'], "text/html; charset=ISO-8859-1")


    # def test_http_head_ssl(self):
    #     """Test HTTP head response with SSL"""
    #     http = HTTP("https://www.google.com")
    #     head = http.head()
    #     self.assertEqual(head['content-type'], "text/html; charset=ISO-8859-1")

