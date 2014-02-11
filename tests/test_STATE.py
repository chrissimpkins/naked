#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import unittest
from Naked.toolshed.state import StateObject

class NakedStateTest(unittest.TestCase):

    def setUp(self):
        self.state = StateObject()
        self.cur_dir = os.getcwd()

    def tearDown(self):
        pass

    def test_so_py2py3(self):
        """StateObject Py2 and Py3 tests"""
        if sys.version_info[0] == 2:
            self.assertTrue(self.state.py2)
            self.assertFalse(self.state.py3)
        elif sys.version_info[0] == 3:
            self.assertTrue(self.state.py3)
            self.assertFalse(self.state.py2)

    def test_so_py_major(self):
        """StateObject Python major version test"""
        if sys.version_info[0] == 2:
            self.assertEqual(2, self.state.py_major)
        elif sys.version_info[0] == 3:
            self.assertEqual(3, self.state.py_major)


    def test_so_py_minor(self):
        """StateObject Python minor version test"""
        if sys.version_info[1] == 7:
            self.assertEqual(7, self.state.py_minor)
        elif sys.version_info[1] == 2:
            self.assertEqual(2, self.state.py_minor)
        elif sys.version_info[1] == 3:
            self.assertEqual(3, self.state.py_minor)
        elif sys.version_info[1] == 4:
            self.assertEqual(4, self.state.py_minor)
        elif sys.version_info[1] == 5:
            self.assertEqual(5, self.state.py_minor)
        elif sys.version_info[1] == 6:
            self.assertEqual(6, self.state.py_minor)

    def test_so_py_patch(self):
        """StateObject Python patch version test"""
        if sys.version_info[2] == 7:
            self.assertEqual(7, self.state.py_patch)
        elif sys.version_info[2] == 2:
            self.assertEqual(2, self.state.py_patch)
        elif sys.version_info[2] == 3:
            self.assertEqual(3, self.state.py_patch)
        elif sys.version_info[2] == 4:
            self.assertEqual(4, self.state.py_patch)
        elif sys.version_info[2] == 5:
            self.assertEqual(5, self.state.py_patch)
        elif sys.version_info[2] == 6:
            self.assertEqual(6, self.state.py_patch)

    def test_so_os(self):
        """StateObject OS test"""
        if sys.platform == 'darwin':
            self.assertEqual('darwin', self.state.os)

    def test_so_cwd(self):
        """StateObject CWD test"""
        self.assertEqual(self.cur_dir, self.state.cwd)
        self.assertEqual(type("test"), type(self.state.cwd)) #string type

    def test_so_pardir(self):
        """StateObject parent directory test"""
        self.assertEqual(os.pardir, self.state.parent_dir)
        self.assertEqual(type("test string"), type(self.state.parent_dir)) #string type

    def test_so_defaultpath(self):
        """StateObject default path test"""
        self.assertEqual(os.defpath, self.state.default_path)
        self.assertEqual(type("test string"), type(self.state.default_path))

    def test_so_userpath(self):
        """StateObject user path test"""
        self.assertEqual(os.path.expanduser("~"), self.state.user_path)
        self.assertEqual(type("test string"), type(self.state.user_path))

    def test_so_stringencode(self):
        """StateObject string encoding test"""
        self.assertEqual(sys.getdefaultencoding(), self.state.string_encoding)
        self.assertEqual(type("test string"), type(self.state.string_encoding))

    def test_so_fileencode(self):
        """StateObject file encoding test"""
        self.assertEqual(sys.getfilesystemencoding(), self.state.file_encoding)
        self.assertEqual(type("test string"), type(self.state.file_encoding))

    def test_so_time_types(self):
        """StateObject time/date type tests"""
        self.assertEqual(type(20), type(self.state.hour))
        self.assertEqual(type(20), type(self.state.min))
        self.assertEqual(type(20), type(self.state.second))
        self.assertEqual(type(20), type(self.state.day))
        self.assertEqual(type(20), type(self.state.year))
        self.assertEqual(type(20), type(self.state.month))

