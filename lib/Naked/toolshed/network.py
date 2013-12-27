#!/usr/bin/env python

import sys
import requests
from Naked.settings import debug as DEBUG_FLAG

## TODO: re-raise exception for any errors rather than handle them in this file (for other users)

#------------------------------------------------------------------------------
#[ HTTP class]
#  handle HTTP requests
#  Uses the requests external library to handle HTTP requests and response object
#------------------------------------------------------------------------------
class HTTP():
	def __init__(self, url="", request_timeout=10):
		self.url = url
		self.request_timeout = request_timeout
		self.res = None # assigned with the requests external library response object after a HTTP method call

	#------------------------------------------------------------------------------
	# [ get method ] (string) - uses external requests library available on PyPI
	#   open HTTP data stream with GET request for user specified URL and return text data
	#   returns data stream read from the URL (string)
	#   Default timeout = 10 s from class constructor
	#------------------------------------------------------------------------------
	def get(self):
		try:
			response = requests.get(self.url, timeout=self.request_timeout)
			self.res = response # assign the response object from requests to a property on the instance
			return response.text
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to perform GET request with the URL " + self.url + "using the get() method (Naked.toolshed.network.py)")
			raise e

	#------------------------------------------------------------------------------
	# [ get_data method ] (binary data)
	#   open HTTP data stream with GET request and return binary data
	#   returns data stream with raw binary data
	#------------------------------------------------------------------------------
	def get_data(self):
		try:
			response = requests.get(self.url, timeout=self.request_timeout)
			self.res = response # assign the response object from requests to a property on the instance
			return response.content # return binary data instead of text (get() returns text)
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to perform GET request with the URL " + self.url + "using the get_data() method (Naked.toolshed.network.py)")
			raise e

	#------------------------------------------------------------------------------
	# [ get_data_make_file method ] (boolean)
	#   open HTTP data stream with GET request, make file with the returned binary data
	#   file path is passed to the method by the developer
	#   return True on successful pull and write to disk
	#------------------------------------------------------------------------------
	def get_data_make_file(self, filepath=""):
		try:
			import os # used for os.fsync() method in the write
			if (filepath == "" and len(self.url) > 1):
				filepath = self.url.split('/')[-1] # use the filename from URL and working directory as default if not specified
			response = requests.get(self.url, timeout=self.request_timeout, stream=True)
			self.res = response
			with open(filepath, 'wb') as f:
				for chunk in response.iter_content(chunk_size=1024):
					f.write(chunk)
					f.flush()
					os.fsync(f.fileno()) # flush all internal buffers to disk
			return True # return True if successful write
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to perform GET request and write file with the URL " + self.url + "using the get_data_make_file() method (Naked.toolshed.network.py)")
			raise e

	#------------------------------------------------------------------------------
	# [ response method ]
	#   getter method for the requests library object that is assigned as a property
	#   on the HTTP class after a HTTP request method is run (e.g. get())
	#   note: must run one of these HTTP methods to assign this property (None by default)
	#------------------------------------------------------------------------------
	def response(self):
		try:
			return self.res
		except Exception, e:
			if DEBUG_FLAG:
				sys.stderr.write("Naked Framework Error: Unable to return the response from your HTTP request with the response() method (Naked.toolshed.network.py).")
			raise e


if __name__ == '__main__':
	pass
	#------------------------------------------------------------------------------
	# HTTP GET 1
	#------------------------------------------------------------------------------
	# http = HTTP("http://www.google.com")
	# data = http.get()
	# print(data)
	# from Naked.toolshed.file import FileWriter
	# w = FileWriter("testfile.txt")
	# w.write_utf8(data)
	#------------------------------------------------------------------------------
	# HTTP GET 2
	#------------------------------------------------------------------------------
	# http = HTTP()
	# http.url = "http://www.google.com"
	# print(http.get())
	#------------------------------------------------------------------------------
	# RESPONSE TEST
	#------------------------------------------------------------------------------
	# http = HTTP("http://www.google.com")
	# http.get()
	# print(http.res.status_code)

