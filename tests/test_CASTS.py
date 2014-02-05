#!/usr/bin/env python
# encoding: utf-8

import unittest
from Naked.toolshed.types import XString, XDict, XList, XSet, XFSet, XTuple, NakedObject
from Naked.toolshed.casts import xstr, xd, xl, xq, xset, xfset, xt, nobj

class NakedCastsTest(unittest.TestCase):

    def setUp(self):
        self.teststring = "this is a test"
        self.testdict = {'key1': 'val1', 'key2': 'val2'}
        self.testlist = ['item1', 'item2', 'item3']
        self.testset = {'item1', 'item2', 'item3'}
        self.frozenset = frozenset(self.testset)
        self.testtuple = ('item1', 'item2', 'item3')
        self.stringtype = type(self.teststring)
        self.dicttype = type(self.testdict)
        self.listtype = type(self.testlist)
        self.settype = type(self.testset)
        self.fsettype = type(self.frozenset)
        self.tupletype = type(self.testtuple)

        self.nobj = NakedObject(self.testdict)
        self.xstring = XString(self.teststring, self.testdict)
        self.xdict = XDict(self.testdict, self.testdict)
        self.xlist = XList(self.testlist, self.testdict)
        self.xsets = XSet(self.testset, self.testdict)
        self.xfsets = XFSet(self.testset, self.testdict)
        self.xtuple = XTuple(self.testtuple, self.testdict)
        self.nobjtype = type(self.nobj)
        self.xstringtype = type(self.xstring)
        self.xdicttype = type(self.xdict)
        self.xlisttype = type(self.xlist)
        self.xsettype = type(self.xsets)
        self.xfsettype = type(self.xfsets)
        self.xtupletype = type(self.xtuple)

        self.test_nobj = nobj(self.testdict)
        self.test_xstring = xstr(self.teststring, self.testdict)
        self.test_xdict = xd(self.testdict, self.testdict)
        self.test_xlist = xl(self.testlist, self.testdict)
        self.test_xset = xset(self.testset, self.testdict)
        self.test_xfset = xfset(self.frozenset, self.testdict)
        self.test_xtuple = xt(self.testtuple, self.testdict)

    def tearDown(self):
        pass

    #------------------------------------------------------------------------------
    # Python type assertions
    #------------------------------------------------------------------------------

    def test_string_python_type(self):
        self.assertEqual(self.stringtype, type(self.teststring))

    def test_dict_python_type(self):
        self.assertEqual(self.dicttype, type(self.testdict))

    def test_list_python_type(self):
        self.assertEqual(self.listtype, type(self.testlist))

    def test_set_python_type(self):
        self.assertEqual(self.settype, type(self.testset))

    def test_fset_python_type(self):
        self.assertEqual(self.fsettype, type(self.frozenset))

    def test_tuple_python_type(self):
        self.assertEqual(self.tupletype, type(self.testtuple))

    #------------------------------------------------------------------------------
    # Naked type extension assertions
    #------------------------------------------------------------------------------

    def test_naked_object_naked_type(self):
        self.assertEqual(self.nobjtype, type(self.nobj))

    def test_xstring_naked_type(self):
        self.assertEqual(self.xstringtype, type(self.xstring))

    def test_xdict_naked_type(self):
        self.assertEqual(self.xdicttype, type(self.xdict))

    def test_xlist_naked_type(self):
        self.assertEqual(self.xlisttype, type(self.xlist))

    def test_xset_naked_type(self):
        self.assertEqual(self.xsettype, type(self.xsets))

    def test_xfset_naked_type(self):
        self.assertEqual(self.xfsettype, type(self.xfsets))

    def test_xtuple_naked_type(self):
        self.assertEqual(self.xtupletype, type(self.xtuple))

    #------------------------------------------------------------------------------
    # Confirm that Python type is not equal to the Naked type
    #------------------------------------------------------------------------------

    def test_nobj_not_equal_dict_type(self):
        self.assertNotEqual(self.nobjtype, self.dicttype)

    def test_xstring_not_equal_string_type(self):
        self.assertNotEqual(self.xstringtype, self.stringtype)

    def test_xdict_not_equal_dict_type(self):
        self.assertNotEqual(self.xdicttype, self.dicttype)

    def test_xlist_not_equal_list_type(self):
        self.assertNotEqual(self.xlisttype, self.listtype)

    def test_xset_not_equal_set_type(self):
        self.assertNotEqual(self.xsettype, self.settype)

    def test_xfset_not_equal_fset_type(self):
        self.assertNotEqual(self.xfsettype, self.fsettype)

    def test_xtuple_not_equal_tuple_type(self):
        self.assertNotEqual(self.xtupletype, self.tupletype)

    #------------------------------------------------------------------------------
    # Confirm that casts create objects that are of Naked types
    #------------------------------------------------------------------------------

    def test_naked_object_from_dict_type(self):
        self.assertEqual(self.nobjtype, type(self.test_nobj))

    def test_xstring_from_string_type(self):
        self.assertEqual(self.xstringtype, type(self.test_xstring))

    def test_xdict_from_dict_type(self):
        self.assertEqual(self.xdicttype, type(self.test_xdict))

    def test_xlist_from_list_type(self):
        self.assertEqual(self.xlisttype, type(self.test_xlist))

    def test_xset_from_set_type(self):
        self.assertEqual(self.xsettype, type(self.test_xset))

    def test_xfset_from_fset_type(self):
        self.assertEqual(self.xfsettype, type(self.test_xfset))

    def test_xtuple_from_tuple_type(self):
        self.assertEqual(self.xtupletype, type(self.test_xtuple))

    #------------------------------------------------------------------------------
    # And confirm that casted objects are no longer of original Python types
    #------------------------------------------------------------------------------

    def test_naked_obj_not_dict_type(self):
        self.assertNotEqual(self.dicttype, type(self.test_nobj))

    def test_xstring_not_string_type(self):
        self.assertNotEqual(self.stringtype, type(self.test_xstring))

    def test_xdict_not_dict_type(self):
        self.assertNotEqual(self.dicttype, type(self.test_xdict))

    def test_xlist_not_list_type(self):
        self.assertNotEqual(self.listtype, type(self.test_xlist))

    def test_xset_not_set_type(self):
        self.assertNotEqual(self.settype, type(self.test_xset))

    def test_xfset_not_fset_type(self):
        self.assertNotEqual(self.fsettype, type(self.test_xfset))

    def test_xtuple_not_tuple_type(self):
        self.assertNotEqual(self.tupletype, type(self.test_xtuple))

    #------------------------------------------------------------------------------
    # Confirm that the cast appropriately assigned attributes
    #------------------------------------------------------------------------------

    def test_naked_obj_attr(self):
        self.assertEqual('val1', self.test_nobj.key1)

    def test_xstring_obj_attr(self):
        self.assertEqual('val1', self.test_xstring.key1)

    def test_xdict_obj_attr(self):
        self.assertEqual('val1', self.test_xdict.key1)

    def test_xlist_obj_attr(self):
        self.assertEqual('val1', self.test_xlist.key1)

    def test_xset_obj_attr(self):
        self.assertEqual('val1', self.test_xset.key1)

    def test_xfset_obj_attr(self):
        self.assertEqual('val1', self.test_xfset.key1)

    def test_xtuple_obj_attr(self):
        self.assertEqual('val1', self.test_xtuple.key1)





