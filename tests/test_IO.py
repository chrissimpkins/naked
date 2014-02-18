#!/usr/bin/env python
# coding=utf-8

import unittest
import os
from Naked.toolshed.file import FileReader
from Naked.toolshed.file import FileWriter
from Naked.toolshed.system import make_path
from Naked.toolshed.state import StateObject
state = StateObject()


class NakedIOReadWriteTest(unittest.TestCase):

    def setUp(self):
        self.ascii_string = """This is a string
 & more string"""
        if state.py2:
            # pass - need to skip this assigment for Py3.2 tests
            self.unicode_string = u"Hey! It's Bengali ব য,\nand here is some more ২"
        else:
            self.unicode_string = "Hey! It's Bengali ব য,\nand here is some more ২"
        self.ascii_string = "Check it! This is ascii text!"
        self.latin_string = "grégory"
        self.binary_string = b"This is a binary string"
        self.multiline_string = "This is line 1\nThis is line 2"
        if state.py2:
            # pass - need to skip this assignment for Py3.2 tests
            self.multiline_unicode_string = u"This is line1ব য\nThis is line 2ব য"
        else:
            self.multiline_unicode_string = "This is line1ব য\nThis is line 2ব য"
        self.multiline_list = ["This is line 1\n", "This is line 2"]
        self.mod_multi_list = ["AThis is line 1\n", "AThis is line 2"]
        if state.py2:
            # pass - need to skip this assignment for Py3.2 tests
            self.uni_multi_list = [u"This is line1ব য\n", u"This is line 2ব য"]
        else:
            self.uni_multi_list = ["This is line1ব য\n", "This is line 2ব য"]
        if state.py2:
            # pass - need to skip this assignment for Py3.2 tests
            self.mod_uni_multi_list = [u"AHey! It's Bengali ব য,\n", u"Aand here is some more ২"]
        else:
            self.mod_uni_multi_list = ["AHey! It's Bengali ব য,\n", "Aand here is some more ২"]
        self.ascii_path = make_path("testfiles", "ascii.txt")
        self.binary_path = make_path("testfiles", "binary.bin")
        self.multiline_path = make_path("testfiles", "multi.txt")
        self.unicode_path = make_path("testfiles", "unicode.txt")
        self.unicode2_path = make_path("testfiles", "unicode2.txt")
        self.utfsixteen_path = make_path("testfiles", "sixteen.txt")
        self.latin_path = make_path("testfiles", "latin.txt")
        self.bogus_path = make_path("testfiles", "bogus.txt")

    def tearDown(self):
        pass

    #------------------------------------------------------------------------------
    # ASCII read & write file tests
    #------------------------------------------------------------------------------
    def test_file_ascii_readwrite(self):
        """Test write and read of ascii encoded file"""
        FileWriter(self.ascii_path).write(self.ascii_string) # file write
        ascii_text = FileReader(self.ascii_path).read() # file read
        self.assertEqual(ascii_text, self.ascii_string)

    def test_file_ascii_readwrite_append(self):
        """Test append of ascii text to existing file"""
        FileWriter(self.ascii_path).append(self.ascii_string) #append a second string of the ascii text
        ascii_text = FileReader(self.ascii_path).read()
        self.assertEqual(ascii_text, (self.ascii_string)*2) #confirm that it equals two of the ascii strings

    def test_file_ascii_safewrite(self):
        """Test safe_write() to confirm does not overwrite existing file"""
        os.remove(self.ascii_path) #remove the existing text file for tests
        if os.path.exists(self.ascii_path):
            raise IOError("The ascii test file was not deleted. (test_IO.py.test_file_ascii_safewrite)")
        else:
            safe_response = FileWriter(self.ascii_path).safe_write(self.ascii_string) # attempt safe_write when no preexisting file present
            ascii_text = FileReader(self.ascii_path).read()
            self.assertEqual(ascii_text, self.ascii_string) # assert that the correct text was written
            self.assertEqual(safe_response, True) # assert that returns True when file not present and writes

            if os.path.exists(self.ascii_path):
                    self.assertEqual(FileWriter(self.ascii_path).safe_write(self.ascii_string), False) #confirm that returns False to calling function when there is a pre-existing file
            else:
                raise IOError("The ascii test file is not present (test_IO.py.test_file_ascii_safewrite)")

    def test_file_ascii_readwrite_string_type(self):
        FileWriter(self.ascii_path).write(self.ascii_string) # file write
        ascii_text = FileReader(self.ascii_path).read() # file read
        if state.py2:
            self.assertEqual(type(unicode("test string")), type(ascii_text)) #python 2 treats all input as unicode type
        elif state.py3:
            self.assertEqual(type(str("test string")), type(ascii_text)) #python 3 treats all input as str


    #------------------------------------------------------------------------------
    # UTF-8 file tests
    #------------------------------------------------------------------------------
    def test_file_utf8_readwrite(self):
        """Test write and read of a utf-8 encoded file"""
        FileWriter(self.unicode_path).write_utf8(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read_utf8()
        self.assertEqual(unicode_text, self.unicode_string)

    def test_file_utf8_readas_writeas(self):
        """Test read_as & write_as with utf-8 encoding"""
        FileWriter(self.unicode2_path).write_as(self.unicode_string, "utf-8")
        unicode_text = FileReader(self.unicode2_path).read_as("utf-8")
        self.assertEqual(unicode_text, self.unicode_string)

    def test_file_utf8_readwrite_append(self):
        FileWriter(self.unicode_path).write_utf8(self.unicode_string)
        FileWriter(self.unicode_path).append_utf8(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read_utf8()
        self.assertTrue(len(unicode_text)>0)
        self.assertEqual(unicode_text, (self.unicode_string*2))

    def test_file_utf8_append_works_with_utf8(self):
        FileWriter(self.unicode_path).write_utf8(self.unicode_string)
        FileWriter(self.unicode_path).append(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read_utf8()
        self.assertTrue(len(unicode_text)>0)
        self.assertEqual(unicode_text, (self.unicode_string*2))

    def test_file_utf8_write_noraise_unicodeerror(self):
        """Test write of a utf-8 file with write method does not raise UnicodeEncodeError in Python 2 or 3"""
        FileWriter(self.unicode_path).write(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read_utf8()
        self.assertEqual(self.unicode_string, unicode_text)

    def test_file_utf8_readwrite_noraise_unicodeerror(self):
        """Test read and write does not raise unicode errors in Python 2 or 3"""
        FileWriter(self.unicode_path).write(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read()
        self.assertEqual(self.unicode_string, unicode_text)

    def test_file_utf8_safewrite(self):
        """Test safe_write() to confirm does not overwrite existing file with unicode string"""
        os.remove(self.unicode_path) #remove the existing text file for tests
        if os.path.exists(self.unicode_path):
            raise IOError("The unicode test file was not deleted. (test_IO.py.test_file_utf8_safewrite)")
        else:
            safe_response = FileWriter(self.unicode_path).safe_write(self.unicode_string) # attempt safe_write when no preexisting file present
            u_text = FileReader(self.unicode_path).read()
            self.assertEqual(u_text, self.unicode_string) # assert that the correct text was written
            self.assertEqual(safe_response, True) # assert that returns True when file not present and writes

            if os.path.exists(self.unicode_path):
                    self.assertEqual(FileWriter(self.unicode_path).safe_write(self.unicode_string), False) #confirm that returns False to calling function when there is a pre-existing file
            else:
                raise IOError("The unicode test file is not present (test_IO.py.test_file_utf8_safewrite)")

    def test_file_readwrite_utf8_string_type(self):
        FileWriter(self.unicode_path).write(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read()
        if state.py2:
            self.assertEqual(type(unicode("test string")), type(unicode_text)) # confirm that python2 treats as unicode
        elif state.py3:
            self.assertEqual(type(str("test string")), type(unicode_text)) # confirm that python3 treats as str

    def test_file_readutf8_writeutf8_string_type(self):
        FileWriter(self.unicode_path).write_utf8(self.unicode_string)
        unicode_text = FileReader(self.unicode_path).read_utf8()
        if state.py2:
            self.assertEqual(type(unicode("test string")), type(unicode_text)) # confirm that python2 treats as unicode
        elif state.py3:
            self.assertEqual(type(str("test string")), type(unicode_text)) # confirm that python3 treats as str

    #------------------------------------------------------------------------------
    # BINARY DATA tests
    #------------------------------------------------------------------------------
    def test_file_bin_readwrite(self):
        """Test read and write of binary data"""
        FileWriter(self.binary_path).write_bin(self.binary_string)
        bin_data = FileReader(self.binary_path).read_bin()
        self.assertEqual(bin_data, self.binary_string)

    def test_file_bin_read_unicode_as_bin(self):
        """Test read of unicode as binary with decode"""
        FileWriter(self.unicode_path).write_utf8(self.unicode_string)
        bin_data = FileReader(self.unicode_path).read_bin() #read unicode file as binary
        uni_text = bin_data.decode("utf-8") #decode to utf-8
        self.assertEqual(uni_text, self.unicode_string)

    #------------------------------------------------------------------------------
    # LINE READS
    #------------------------------------------------------------------------------
    def test_file_readlines(self):
        """Test line reads with ascii text"""
        FileWriter(self.multiline_path).write(self.multiline_string)
        line_list = FileReader(self.multiline_path).readlines()
        self.assertEqual(line_list, self.multiline_list)

    def test_file_readlines_unicode(self):
        """Test line reads with unicode text"""
        FileWriter(self.unicode_path).write_utf8(self.multiline_unicode_string)
        line_list = FileReader(self.unicode_path).readlines_utf8()
        self.assertEqual(line_list, self.uni_multi_list)

    def test_file_readlines_as_ascii(self):
        """Test line reads with readlines_as from ascii file"""
        FileWriter(self.ascii_path).write(self.multiline_string)
        line_list = FileReader(self.ascii_path).readlines_as("ascii")
        self.assertEqual(line_list, self.multiline_list)

    def test_file_readlines_as_utf8(self):
        """Test line reads with readlines_as from utf8 file"""
        FileWriter(self.unicode_path).write_utf8(self.multiline_unicode_string)
        line_list = FileReader(self.unicode_path).readlines_as("utf-8")
        self.assertEqual(line_list, self.uni_multi_list)

    #------------------------------------------------------------------------------
    # FILE COMPRESSION tests
    #------------------------------------------------------------------------------
    def test_file_gzip_ascii_readwrite(self):
        """Test gzip compression and read from compressed ascii text file in Python 2"""
        if state.py2:
            FileWriter(self.ascii_path).gzip(self.ascii_string)
            gzip_contents = FileReader(self.ascii_path + ".gz").read_gzip()
            self.assertEqual(gzip_contents, self.ascii_string)
        elif state.py3:
            FileWriter(self.ascii_path).gzip(bytes(self.ascii_string, 'utf-8'))
            gzip_contents = FileReader(self.ascii_path + ".gz").read_gzip()
            self.assertEqual(gzip_contents.decode('ascii'), self.ascii_string)

    def test_file_gzip_utf8_readwrite(self):
        """Test gzip compression and read from compressed unicode text file without explicit utf-8 decode"""
        if state.py2:
            FileWriter(self.unicode_path).gzip(self.unicode_string)
            gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip() # when read without explicit utf-8 decoding, the strings will not match
            self.assertNotEqual(gzip_contents, self.unicode_string)
        elif state.py3:
            FileWriter(self.unicode_path).gzip(bytes(self.unicode_string, 'utf-8'))
            gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip() # when read without explicit utf-8 decoding, the strings will not match
            self.assertNotEqual(gzip_contents, self.unicode_string)


    def test_file_gzip_utf8_readwrite_explicit_decode(self):
        """Test gzip compression and read from compressed unicode text file with explicit utf-8 decode"""
        if state.py2:
            FileWriter(self.unicode_path).gzip(self.unicode_string)
            gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip("utf-8") # when read with explicit utf-8 decoding, strings should match
            self.assertEqual(gzip_contents, self.unicode_string)
        elif state.py3:
            FileWriter(self.unicode_path).gzip(bytes(self.unicode_string, 'utf-8'))
            gzip_contents = FileReader(self.unicode_path + ".gz").read_gzip("utf-8") # when read with explicit utf-8 decoding, strings should match
            self.assertEqual(gzip_contents, self.unicode_string)

    #------------------------------------------------------------------------------
    # MISSING FILE tests
    #------------------------------------------------------------------------------
    def test_file_read_missing_file(self):
        """Test that missing file to read() throws IOError"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).read()

    def test_file_readas_missing_file(self):
        """Test that missing file to read_as() throws IOError"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).read_as("utf-8")

    def test_file_read_gzip_missing_file(self):
        """Test that missing file to read_gzip() throws IOError"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).read_gzip()

    def test_file_read_utf8_missing_file(self):
        """Test that missing file to read_utf8 throws IOError"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).read_utf8()

    def test_file_append_missing_file(self):
        """Test append of ascii text raises IOError when file missing"""
        with (self.assertRaises(IOError)):
            FileWriter(self.bogus_path).append(self.ascii_string)

    def test_file_append_utf8_missing_file(self):
        """Test append of unicode text raises IOError when file missing"""
        with (self.assertRaises(IOError)):
            FileWriter(self.bogus_path).append_utf8(self.unicode_string)

    def test_file_read_bin_missing_file(self):
        """Test read_bin raises IOError when file is missing"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).read_bin()

    def test_file_readlines_missing_file(self):
        """Test readlines raises IOError when file is missing"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).readlines()

    def test_file_readlines_utf8_missing_file(self):
        """Test readlines_utf8 raises IOError when file is missing"""
        with (self.assertRaises(IOError)):
            FileReader(self.bogus_path).readlines_utf8()

