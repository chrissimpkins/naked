#!/usr/bin/env python
# encoding: utf-8


import unittest
from Naked.toolshed.types import NakedObject

class NakedTypesTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    #------------------------------------------------------------------------------
    # NakedObject Tests
    #------------------------------------------------------------------------------

    def test_nobj_constructor(self):
        no = NakedObject({'key': 'value'})
        self.assertTrue(no)

    def test_nobj_constructor_empty(self):
        no = NakedObject()
        self.assertTrue(no)

    def test_nobj_constructor_type(self):
        no = NakedObject({'key': 'value'})
        self.assertEqual(type(no), type(NakedObject()))

    def test_nobj_attribute(self):
        no = NakedObject({'key': 'value'})
        self.assertEqual(no.key, 'value')

    def test_nobj_add_attribute(self):
        no = NakedObject({'key': 'value'})
        no.key2 = 'value2'
        self.assertEqual(no.key2, 'value2')


