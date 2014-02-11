#!/usr/bin/env python
# encoding: utf-8

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 7: # do not run with tox in non-2.7 versions (fails because not building the C files)

    import unittest
    from Naked.toolshed.c.python import py_version, py_major_version, py_minor_version, py_patch_version, is_py3, is_py2

    class NakedPythonTest(unittest.TestCase):

        def setUp(self):
            self.truth_pyversion = (sys.version_info[0], sys.version_info[1], sys.version_info[2])
            self.truth_pymajor = sys.version_info[0]
            self.truth_pyminor = sys.version_info[1]
            self.truth_pypatch = sys.version_info[2]
            self.truth_is_py2 = (self.truth_pymajor == (2))
            self.truth_is_py3 = (self.truth_pymajor == (3))

            self.test_pyversion = py_version()
            self.test_pymajor = py_major_version()
            self.test_pyminor = py_minor_version()
            self.test_pypatch = py_patch_version()
            self.test_is_py2 = is_py2()
            self.test_is_py3 = is_py3()

        def tearDown(self):
            pass

        #------------------------------------------------------------------------------
        # Version Tuple Test
        #------------------------------------------------------------------------------
        def test_version_tuple(self):
            self.assertEqual(self.test_pyversion, self.truth_pyversion)

        def test_version_major_tuple(self):
            self.assertEqual(self.test_pyversion[0], self.truth_pymajor)

        def test_version_minor_tuple(self):
            self.assertEqual(self.test_pyversion[1], self.truth_pyminor)

        def test_version_patch_tuple(self):
            self.assertEqual(self.test_pyversion[2], self.truth_pypatch)


        #------------------------------------------------------------------------------
        # Version Major Test
        #------------------------------------------------------------------------------
        def test_version_major(self):
            self.assertEqual(self.test_pymajor, self.truth_pymajor)


        #------------------------------------------------------------------------------
        # Version Minor Test
        #------------------------------------------------------------------------------
        def test_version_minor(self):
            self.assertEqual(self.test_pyminor, self.truth_pyminor)

        #------------------------------------------------------------------------------
        # Version Patch Test
        #------------------------------------------------------------------------------
        def test_version_patch(self):
            self.assertEqual(self.test_pypatch, self.truth_pypatch)

        #------------------------------------------------------------------------------
        # Python 2/3 truth tests
        #------------------------------------------------------------------------------
        def test_is_py2_is_py3(self):
            if self.truth_pymajor == 2:
                self.assertEqual(self.test_is_py2, True)
                self.assertEqual(self.test_is_py3, False)
            elif self.truth_pymajor == 3:
                self.assertEqual(self.test_is_py2, False)
                self.assertEqual(self.test_is_py3, True)



