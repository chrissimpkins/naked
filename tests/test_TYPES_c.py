#!/usr/bin/env python
# encoding: utf-8

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 7: # do not run with tox in non-2.7 versions (fails because not building the C files)

    import unittest
    from Naked.toolshed.types import NakedObject, XDict, XList, XSet, XFSet, XTuple, XMinHeap, XMaxHeap

    class NakedTypesTest(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        #------------------------------------------------------------------------------
        # NakedObject Tests
        #------------------------------------------------------------------------------

        # constructors
        def test_nobj_constructor(self):
            no = NakedObject({'key': 'value'})
            self.assertTrue(no)

        def test_nobj_constructor_empty(self):
            no = NakedObject()
            self.assertTrue(no)

        def test_nobj_constructor_type(self):
            no = NakedObject({'key': 'value'})
            self.assertEqual(type(no), type(NakedObject())) # <class 'Naked.toolshed.types.NakedObject'>

        def test_nobj_attribute_default_constructor(self):
            no = NakedObject({'key': 'value'})
            self.assertTrue(hasattr(no, 'key')) #has attribute key
            self.assertEqual(no.key, 'value') #with appropriate value

        # attributes
        def test_nobj_auto_generated_type_attribute(self):
            no = NakedObject()
            self.assertTrue(hasattr(no, '_naked_type_')) # contains the automatically generated type attribute
            self.assertEqual(no._naked_type_, 'NakedObject') # contains correct string for the attribute

        def test_nobj_set_attribute_dot(self):
            no = NakedObject()
            no.key = 'value'
            self.assertTrue(hasattr(no, 'key')) #has attr key
            self.assertEqual(no.key, 'value') #with appropriate value

        def test_nobj_set_attribute_dict(self):
            no = NakedObject({'key': 'value'})
            no.key2 = 'value2' # add new attribute
            self.assertTrue(hasattr(no, 'key2'))
            self.assertEqual(no.key2, 'value2')

        def test_nobj_get_attribute_exists(self):
            no = NakedObject({'key': 'value'})
            self.assertEqual(getattr(no, 'key'), no.key)

        def test_nobj_get_attribute_dot_noexist(self):
            no = NakedObject({'key': 'value'})
            with self.assertRaises(AttributeError):
                test = no.bogus

        def test_nobj_get_attribute_noexist(self):
            no = NakedObject({'key': 'value'})
            with self.assertRaises(AttributeError): # raisees AttributeError on getattr attempt without attribute
                test = getattr(no, 'bogus')

        def test_nobj_del_attribute(self):
            no = NakedObject({'key': 'value'})
            self.assertEqual(no.key, 'value')
            del no.key
            with self.assertRaises(AttributeError): # raises AttributeError on attempt to access with dot syntax without attribute
                test = no.test

        def test_nobj_has_attr_true(self):
            no = NakedObject({'key': 'value'})
            self.assertTrue(hasattr(no, 'key')) # True for attr that exists

        def test_nobj_has_attr_false(self):
            no = NakedObject({'key': 'value'})
            self.assertFalse(hasattr(no, 'bogus')) # False for attr that does not exist

        # methods
           ## equality testing
        def test_nobj_equality(self):
            no = NakedObject({'key': 'value'})
            nd = no
            self.assertTrue(no == nd) # the same object
            self.assertFalse(no != nd)

        def test_nobj_equality_diff_obj(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'value'})
            self.assertTrue(no == nd) # true when different objects
            self.assertFalse(no != nd)

        def test_nobj_equality_empty(self):
            no = NakedObject()
            nd = NakedObject()
            self.assertTrue(no == nd)
            self.assertFalse(no != nd)

        def test_nobj_equality_attributes(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'value'})
            self.assertTrue(no._equal_attributes(nd)) # attributes are the same

        def test_nobj_equality_attributes_fail_on_val(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'bogus'})
            self.assertFalse(no._equal_attributes(nd))

        def test_nobj_equality_attributes_fail_on_attrname(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'bogus': 'value'})
            self.assertFalse(no._equal_attributes(nd))

        def test_nobj_equality_type(self):
            no = NakedObject({'key': 'value'})
            nd = no
            self.assertTrue(no._equal_type(nd)) # variable that points to same object is same class

        def test_nobj_equality_type_newobj(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'value'})
            self.assertTrue(no._equal_type(nd)) # new object of same class is same class

        def test_nobj_equality_type_fail(self):
            no = NakedObject({'key': 'value'})
            nd = "test string"
            self.assertFalse(no._equal_type(nd)) # different classes are not equal classes

        def test_nobj_equals(self):
            no = NakedObject({'key': 'value'})
            nd = no
            self.assertTrue(no.equals(nd)) # variable that points to same object meets True condition on equals() method

        def test_nobj_equals_newobj(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'value'})
            self.assertTrue(no.equals(nd)) # new object that has same type and attributes meets True condition on equals() method

        def test_nobj_equals_newobj_diff_attrname(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'bogus': 'value'})
            self.assertFalse(no.equals(nd)) # new object with different attribute names meets False condition on equals() method

        def test_nobj_equals_newobj_diff_attrval(self):
            no = NakedObject({'key': 'value'})
            nd = NakedObject({'key': 'bogus'})
            self.assertFalse(no.equals(nd)) # new object with different attribute values meets False condition on equals() method

        def test_nobj_equals_newobj_diff_attrval_type(self):
            no = NakedObject({'key': '1'})
            nd = NakedObject({'key': 1})
            self.assertFalse(no.equals(nd)) # different attribute value types meets False condition on equals() method

        def test_nobj_equals_diffobj(self):
            no = NakedObject({'key': 'value'})
            nd = "test string"
            self.assertFalse(no.equals(nd)) # new object that is of different type meets False condition on equals() method

        def test_nobj_equals_emptyobjs(self):
            no = NakedObject()
            nd = NakedObject()
            self.assertTrue(no.equals(nd)) # NakedObjects that do not have attributes set at instantiation are equal

        def test_nobj_getattrdict_method(self):
            test_attr_dict = {'item1': 'val1', 'item2': 'val2'}
            no = NakedObject(test_attr_dict)
            self.assertEqual(no._getAttributeDict(), {'item1': 'val1', 'item2': 'val2', '_naked_type_': 'NakedObject'})

        def test_nobj_type_method(self):
            no = NakedObject({'key': 'value'})
            self.assertEqual(no.type(), 'NakedObject')

        #------------------------------------------------------------------------------
        # XDict class tests
        #------------------------------------------------------------------------------
        # constructors
        def test_xdict_constructor_empty(self):
            xd = XDict({'key': 'value'})
            self.assertTrue(xd)

        def test_xdict_constructor(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertTrue(xd)

        def test_xdict_constructor_empty_internal_type_attr(self):
            xd = XDict({'key': 'value'}) # test with no initial attribute assignment
            self.assertTrue(hasattr(xd, '_naked_type_'))
            self.assertEqual(xd._naked_type_, 'XDict')

        def test_xdict_constructor_internal_type_attr(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'}) # test with initial attribute assignment
            self.assertTrue(hasattr(xd, '_naked_type_'))
            self.assertEqual(xd._naked_type_, 'XDict')

        # type
        def test_xdict_constructor_type(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertEqual(type(xd), type(XDict({'test': 'att'})))

        def test_xdict_constructor_instanceof_XDict(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertTrue(isinstance(xd, XDict)) #instance of XDict

        def test_xdict_constructor_instanceof_dict(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertTrue(isinstance(xd, dict)) #instanace of dict

        # equality testing

        def test_xdict_equals_sameobj(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            xn = xd
            self.assertTrue(xd.equals(xn))
            self.assertTrue(xd == xn)
            self.assertFalse(xd != xn)

        def test_xdict_equals_newobj(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertTrue(xd.equals(xn))
            self.assertTrue(xd == xn)
            self.assertFalse(xd != xn)

        def test_xdict_equals_newobj_emptyattrs(self):
            xd = XDict({'key': 'value'})
            xn = XDict({'key': 'value'})
            self.assertTrue(xd.equals(xn))
            self.assertTrue(xd == xn)
            self.assertFalse(xd != xn)

        def test_xdict_equals_newobj_addattr(self):
            xd = XDict({'key': 'value'})
            xn = XDict({'key': 'value'})
            xd.test = 'testing'
            xn.test = 'testing'
            self.assertTrue(hasattr(xd, 'test'))
            self.assertTrue(hasattr(xn, 'test'))
            self.assertTrue(xd.equals(xn))
            self.assertTrue(xd == xn)
            self.assertFalse(xd != xn)

        def test_xdict_equals_newobj_diffdictkey(self):
            xd = XDict({'diff': 'value'}, {'attrkey': 'attrval'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diffdictval(self):
            xd = XDict({'key': 'diff'}, {'attrkey': 'attrval'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diffattr(self):
            xd = XDict({'key': 'value'}, {'diff': 'attrval'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diffattrval(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'diff'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diffattr_number(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval', 'another': 'test'})
            xn = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diff_attrtypes(self):
            xd = XDict({'key': 'value'}, {'attrkey': 1})
            xn = XDict({'key': 'value'}, {'attrkey': '1'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        def test_xdict_equals_newobj_diff_dicttypes(self):
            xd = XDict({'key': '1'}, {'attrkey': 'attrval'})
            xn = XDict({'key': 1}, {'attrkey': 'attrval'})
            self.assertFalse(xd.equals(xn))
            self.assertFalse(xd == xn)
            self.assertTrue(xd != xn)

        # dict values
        def test_xdict_dictionary_value(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertEqual(xd['key'], 'value')

        # attributes
        def test_xdict_attribute_value(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertEqual(xd.attrkey, 'attrval')

        def test_xdict_add_attribute(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            xd.newatt = 'the test'
            self.assertEqual(xd.newatt, 'the test')

        def test_xdict_has_attribute_true(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertTrue(hasattr(xd, 'attrkey'))

        def test_xdict_has_attribute_false(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            self.assertFalse(hasattr(xd, 'bogus'))

        # test that python dictionary method works
        def test_xdict_builtin_dictionary_method(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = {'another': 'value2'}
            xd.update(nd) # test a built in dictionary method on an XDict
            self.assertEqual(xd['another'], 'value2')
            self.assertEqual(xd.attrkey, 'attrval') # confirm that attribute remains

        # operator overloads
        def test_xdict_plus_overload_with_dict(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = {'another': 'value2'}
            ld = xd + nd
            self.assertEqual(type(ld), type(XDict({'test': 'string'}))) # is of type XDict after combine
            self.assertEqual(ld.attrkey, 'attrval') #attribute is maintained
            self.assertEqual(len(ld), 2) # includes two key:value pairs
            self.assertEqual(ld['key'], 'value') # test value of key 1
            self.assertEqual(ld['another'], 'value2') # test value of key 2

        def test_xdict_plus_overload_with_xdict(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = XDict({'another': 'value2'}, {'attrkey2': 'attrval2'})
            ld = xd + nd
            self.assertEqual(type(ld), type(XDict({'test': 'string'}))) # is of type XDict after combine
            self.assertEqual(ld.attrkey, 'attrval') #attribute from first XDict is maintained
            self.assertEqual(ld.attrkey2, 'attrval2') #attribute from second XDict is maintained
            self.assertEqual(len(ld), 2) # includes two key:value pairs
            self.assertEqual(ld['key'], 'value') # test value of key 1
            self.assertEqual(ld['another'], 'value2') # test value of key 2

        def test_xdict_plus_overload_dict_leftside(self):
            xd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = {'another': 'value2'}
            with self.assertRaises(TypeError): # python dictionary does not support + operator (dict + dict OR dict + XDict)
                ld = nd + xd

        def test_xdict_plusequal_overload(self):
            ld = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = {'another': 'value2'}
            ld += nd
            self.assertEqual(type(ld), type(XDict({'test': 'string'}))) # is of type XDict after combine
            self.assertEqual(ld.attrkey, 'attrval') #attribute is maintained
            self.assertEqual(len(ld), 2) # includes two key:value pairs
            self.assertEqual(ld['key'], 'value') # test value of key 1
            self.assertEqual(ld['another'], 'value2') # test value of key 2

        def test_xdict_plusequal_overload(self):
            ld = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            nd = XDict({'another': 'value2'}, {'attrkey2': 'attrval2'})
            ld += nd
            self.assertEqual(type(ld), type(XDict({'test': 'string'}))) # is of type XDict after combine
            self.assertEqual(ld.attrkey, 'attrval') #attribute from left side XDict is maintained
            self.assertEqual(ld.attrkey2, 'attrval2') #attribute from right side of XDict is added
            self.assertEqual(len(ld), 2) # includes two key:value pairs
            self.assertEqual(ld['key'], 'value') # test value of key from XDict 1
            self.assertEqual(ld['another'], 'value2') # test value of key from XDict 2

        def test_xdict_plusequal_dict_leftside(self):
            nd = XDict({'key': 'value'}, {'attrkey': 'attrval'})
            ld = {'another': 'value2'}
            with self.assertRaises(TypeError): # python does not support this operator for dicts
                ld += nd

        # XDict methods
        def test_xdict_conditional_map_to_vals(self):
            def true_a(xdict_key):
                return xdict_key.startswith('a')

            def cap_val(xdict_val):
                return xdict_val.upper()

            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'a_three': 'value_three'}, {'attrkey': 'attrval'})
            xd = xd.conditional_map_to_vals(true_a, cap_val)
            self.assertTrue(len(xd.values()) == 3)
            self.assertTrue('VALUE_ONE' in xd.values())
            self.assertTrue('VALUE_THREE' in xd.values())
            self.assertTrue('value_two' in xd.values())
            self.assertFalse('VALUE_TWO' in xd.values()) # the b_two value was not converted as per the conditional function

        def test_xdict_map_to_vals(self):
            def cap_val(xdict_val):
                return xdict_val.upper()

            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'a_three': 'value_three'}, {'attrkey': 'attrval'})
            xd = xd.map_to_vals(cap_val)
            self.assertEqual(type(xd), type(XDict({'test': 'dict'})))
            self.assertTrue(len(xd.values()) == 3)
            self.assertTrue('VALUE_ONE' in xd.values())
            self.assertTrue('VALUE_TWO' in xd.values())
            self.assertTrue('VALUE_THREE' in xd.values())
            self.assertEqual(xd.attrkey, 'attrval')

        def test_xdict_val_xlist(self):
            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'a_three': 'value_three'}, {'attrkey': 'attrval'})
            xl = xd.val_xlist()
            self.assertEqual(type(xl), type(XList(['item']))) #actually makes XList
            self.assertTrue(len(xl) == 3) # includes all items
            self.assertTrue('value_one' in xl) # includes appropriate items in XList
            self.assertTrue('value_two' in xl)
            self.assertTrue('value_three' in xl)
            self.assertEqual(xl.attrkey, 'attrval') # includes original attributes

        def test_xdict_max_val(self):
            xd = XDict({'one': 1, 'two': 2, 'three': 3})
            value, key = xd.max_val()
            self.assertEqual(xd.max_val(), (3, 'three')) # returns a tuple
            self.assertEqual(value, 3)
            self.assertEqual(key, 'three')

        def test_xdict_max_val_strings(self):
            xd = XDict({'one': '1', 'two': '2', 'three': '3'})
            value, key = xd.max_val()
            self.assertEqual(xd.max_val(), ('3', 'three')) # returns a tuple
            self.assertEqual(value, '3')
            self.assertEqual(key, 'three')

        def test_xdict_min_val(self):
            xd = XDict({'one': 1, 'two': 2, 'three': 3})
            value, key = xd.min_val()
            self.assertEqual(xd.min_val(), (1, 'one')) # returns a tuple
            self.assertEqual(value, 1)
            self.assertEqual(key, 'one')

        def test_xdict_min_val_strings(self):
            xd = XDict({'one': '1', 'two': '2', 'three': '3'}) # test numerals as strings, still works
            value, key = xd.min_val()
            self.assertEqual(xd.min_val(), ('1', 'one')) # returns a tuple
            self.assertEqual(value, '1')
            self.assertEqual(key, 'one') # note for non-numeral strings, uses alphabetic sorting

        def test_xdict_sum_vals(self):
            xd = XDict({'one': 1, 'two': 2, 'three': 3})
            self.assertEqual(xd.sum_vals(), 6)

        def test_xdict_sum_vals_string_type(self):
            xd = XDict({'one': '1', 'two': '2', 'three': '3'})
            with self.assertRaises(TypeError): # raises TypeError when inappropriate types in the XDict vals
                xd.sum_vals()

        def test_xdict_val_count_string(self):
            xd = XDict({'one': '1', 'two': '1', 'three': '3'})
            self.assertEqual(xd.val_count('1'), 2)
            self.assertEqual(xd.val_count('3'), 1)
            self.assertEqual(xd.val_count('10'), 0) # missing value count is 0

        def test_xdict_val_count_integer(self):
            xd = XDict({'one': 1, 'two': 1, 'three': 3})
            self.assertEqual(xd.val_count(1), 2)
            self.assertEqual(xd.val_count(3), 1)
            self.assertEqual(xd.val_count(10), 0) # missing value count is 0

        def test_xdict_val_count_ci(self):
            xd = XDict({'one': 'TEST', 'two': 'Test', 'int': 1})
            self.assertEqual(xd.val_count_ci('test'), 2)

        def test_xdict_key_difference(self):
            xd = XDict({'one': 1, 'two': 1, 'three': 3})
            xn = XDict({'one': 1, 'twotwo': 1, 'three': 3})
            self.assertEqual(len(xd.difference(xn)), 1)
            self.assertEqual(xd.difference(xn), set(['two']))

        def test_xdict_key_difference_when_none_present(self):
            xd = XDict({'one': 1, 'two': 1, 'three': 3})
            xn = XDict({'one': 1, 'two': 1, 'three': 3})
            self.assertEqual(xd.difference(xn), set([])) # returns empty set

        def test_xdict_key_intersection(self):
            xd = XDict({'one': 1, 'two': 1, 'three': 3})
            xn = XDict({'one': 1, 'twotwo': 1, 'three': 3})
            self.assertEqual(len(xd.intersection(xn)), 2)
            self.assertEqual(xd.intersection(xn), set(['one', 'three']))

        def test_xdict_key_intersection_when_none_present(self):
            xd = XDict({'one': 1, 'two': 1, 'three': 3})
            xn = XDict({'oneone': 1, 'twotwo': 1, 'threethree': 3})
            self.assertEqual(len(xd.intersection(xn)), 0)
            self.assertEqual(xd.intersection(xn), set([]))

        def test_xdict_key_xlist(self):
            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'c_three': 'value_three'}, {'attrkey': 'attrval'})
            xl = xd.key_xlist()
            self.assertEqual(type(xl), type(XList(['item']))) #actually makes XList
            self.assertTrue(len(xl) == 3) # includes all items
            self.assertTrue('a_one' in xl) # includes appropriate items in XList
            self.assertTrue('b_two' in xl)
            self.assertTrue('c_three' in xl)
            self.assertEqual(xl.attrkey, 'attrval') # includes original attributes

        def test_xdict_key_random(self):
            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'c_three': 'value_three'}, {'attrkey': 'attrval'})
            rand = xd.random()
            self.assertEqual(len(rand), 1)
            self.assertEqual(type({'test': 'val'}), type(rand)) # returns Python dictionary type
            self.assertTrue('a_one' in rand.keys() or 'b_two' in rand.keys() or 'c_three' in rand.keys()) # includes one of the key:val from XDict

        def test_xdict_key_random_sample(self):
            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'c_three': 'value_three'}, {'attrkey': 'attrval'})
            rand = xd.random_sample(2)
            self.assertEqual(len(rand), 2)
            self.assertEqual(type({'test': 'val'}), type(rand)) # returns Python dictionary type
            self.assertTrue('a_one' in rand.keys() or 'b_two' in rand.keys() or 'c_three' in rand.keys())

        def test_xdict_xitems(self):
            xd = XDict({'a_one': 'value_one', 'b_two': 'value_two', 'c_three': 'value_three'}, {'attrkey': 'attrval'})
            for keys, values in xd.xitems():
                self.assertTrue('a_one' in keys or 'b_two' in keys or 'c_three' in keys)
                self.assertTrue('value_one' in values or 'value_two' in values or 'value_three' in values)

        #------------------------------------------------------------------------------
        # XList class tests
        #------------------------------------------------------------------------------
        # XList constructors
        def test_xlist_constructor(self):
            xl = XList(['one', 'two', 'three'])
            self.assertTrue(hasattr(xl, '_naked_type_'))
            self.assertEqual(xl._naked_type_, 'XList')

        def test_xlist_constructor_withattr(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertTrue(hasattr(xl, '_naked_type_'))
            self.assertEqual(xl._naked_type_, 'XList')

        def test_xlist_constructor_itemcheck(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertEqual(xl[0], 'one')

        def test_xlist_constructor_attrcheck(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertEqual(xl.first_attr, 1)

        # XList type tests
        def test_xlist_constructor_type(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertEqual(type(xl), type(XList(['test', 'again'])))

        def test_xlist_constructor_instanceof_XList(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertTrue(isinstance(xl, XList)) #instance of XList

        def test_xlist_constructor_instanceof_list(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertTrue(isinstance(xl, list)) #instance of list

        # XList equality tests
        def test_xlist_equality_self(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertTrue(xl == xl)

        def test_xlist_equality_another_same_xlist(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['one', 'two', 'three'], {'first_attr': 1})
            self.assertTrue(xl == xl2)

        def test_xlist_equality_another_list(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_list = ['one', 'two', 'three']
            self.assertFalse(xl == a_list)

        def test_xlist_equality_different_xlist_item(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['different', 'two', 'three'], {'first_attr': 1})
            self.assertFalse(xl == xl2)

        def test_xlist_equality_different_attribute(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['one', 'two', 'three'], {'different_attr': 1})
            self.assertFalse(xl == xl2)

        def test_xlist_equality_different_attrval(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['one', 'two', 'three'], {'first_attr': 2})
            self.assertFalse(xl == xl2)

        def test_xlist_equality_set(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_set = {'one', 'two', 'three'}
            self.assertFalse(xl == a_set)

        def test_xlist_equality_tuple(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_tup = ('one', 'two', 'three')
            self.assertFalse(xl == a_tup)

        # + operator overload
        def test_xlist_add_overload_list(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_list = ['four', 'five']
            nl = xl + a_list    # note that xlist needs to be the left sided operand to include attributes
            self.assertTrue('four' in nl)
            self.assertTrue('one' in nl)
            self.assertEqual(nl.first_attr, 1)

        def test_xlist_add_overload_xlist(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['four', 'five'], {'second_attr': 2})
            nl = xl + xl2
            self.assertTrue('four' in nl)
            self.assertTrue('one' in nl)
            self.assertEqual(nl.first_attr, 1)
            self.assertEqual(nl.second_attr, 2)

        def test_xlist_add_overload_multiplelist(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_list = ['four', 'five']
            b_list = ['six', 'seven']
            nl = xl + a_list + b_list
            self.assertTrue('four' in nl)
            self.assertTrue('one' in nl)
            self.assertTrue('seven' in nl)
            self.assertEqual(nl.first_attr, 1)

        def test_xlist_add_overload_mutiple_xlist(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['four', 'five'], {'second_attr': 2})
            xl3 = XList(['six', 'seven'], {'third_attr': 3})
            nl = xl + xl2 + xl3
            self.assertTrue('one' in nl)
            self.assertTrue('five' in nl)
            self.assertTrue('seven' in nl)
            self.assertEqual(nl.first_attr, 1)
            self.assertEqual(nl.second_attr, 2)
            self.assertEqual(nl.third_attr, 3)

        # += operand
        def test_xlist_addeq_overload_list(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            a_list = ['four', 'five']
            xl += a_list
            self.assertTrue('four' in xl)
            self.assertTrue('one' in xl)
            self.assertEqual(xl.first_attr, 1)

        def test_xlist_addeq_overload_xlist(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            xl2 = XList(['four', 'five'], {'second_attr': 2})
            xl += xl2
            self.assertTrue('four' in xl)
            self.assertTrue('one' in xl)
            self.assertEqual(xl.first_attr, 1)
            self.assertEqual(xl.second_attr, 2)

        # XList string methods
        def test_xlist_join(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            mes = xl.join(" ")
            self.assertEqual(mes, 'one two three')

        def test_xlist_join_typeerror(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            with self.assertRaises(AttributeError): # incorrect type raises attribute error
                mes = xl.join(1)

        def test_xlist_join_diffstring(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            mes = xl.join(',')
            self.assertEqual(mes, 'one,two,three')

        def test_xlist_prefix_char(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.prefix('s')
            self.assertTrue('sone' in nl)
            self.assertTrue('stwo' in nl)
            self.assertTrue('sthree' in nl)

        def test_xlist_prefix_unicode_char(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.prefix('ত')
            self.assertTrue('তone' in nl)
            self.assertTrue('তtwo' in nl)
            self.assertTrue('তthree' in nl)

        def test_xlist_prefix_string(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.prefix('test')
            self.assertTrue('testone' in nl)
            self.assertTrue('testtwo' in nl)
            self.assertTrue('testthree' in nl)

        def test_xlist_postfix_char(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.postfix('s')
            self.assertTrue('ones' in nl)
            self.assertTrue('twos' in nl)
            self.assertTrue('threes' in nl)

        def test_xlist_postfix_unicode_char(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.postfix('ত')
            self.assertTrue('oneত' in nl)
            self.assertTrue('twoত' in nl)
            self.assertTrue('threeত' in nl)

        def test_xlist_postfix_string(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.postfix('test')
            self.assertTrue('onetest' in nl)
            self.assertTrue('twotest' in nl)
            self.assertTrue('threetest' in nl)

        def test_xlist_surround_one_string(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.surround('"')
            self.assertTrue('"one"' in nl)
            self.assertTrue('"two"' in nl)
            self.assertTrue('"three"' in nl)

        def test_xlist_surround_two_strings(self):
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.surround('<p>', '</p>')
            self.assertTrue('<p>one</p>' in nl)
            self.assertTrue('<p>two</p>' in nl)
            self.assertTrue('<p>three</p>' in nl)

        def test_xlist_max_int(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            max_num = xl.max()
            self.assertEqual(max_num, 3)

        def test_xlist_max_float(self):
            xl = XList([1.25123 , 2.5234, 3.73423], {'first_attr': 1})
            max_num = xl.max()
            self.assertEqual(max_num, 3.73423)

        def test_xlist_min_int(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            min_num = xl.min()
            self.assertEqual(min_num, 1)

        def test_xlist_min_float(self):
            xl = XList([1.25123 , 2.5234, 3.73423], {'first_attr': 1})
            min_num = xl.min()
            self.assertEqual(min_num, 1.25123)

        def test_xlist_sum_int(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            total = xl.sum()
            self.assertEqual(total, 6)

        def test_xlist_sum_float(self):
            xl = XList([1.2 , 2.5, 3.1], {'first_attr': 1})
            total = xl.sum()
            self.assertAlmostEqual(total, 6.8)

        def test_xlist_count_dupes_int(self):
            xl = XList([1, 2, 2, 3], {'first_attr': 1})
            dupes = xl.count_duplicates()
            self.assertEqual(dupes, 1)

        def test_xlist_count_dupes_int_twodupe(self):
            xl = XList([1, 2, 2, 3, 3, 3], {'first_attr': 1})
            dupes = xl.count_duplicates()
            self.assertEqual(dupes, 3)

        def test_xlist_count_dupes_string(self):
            xl = XList(['test', 'test', 'another'], {'first_attr': 1})
            dupes = xl.count_duplicates()
            self.assertEqual(dupes, 1)

        def test_xlist_count_dupes_string_twodupe(self):
            xl = XList(['test', 'test', 'another', 'another', 'last', 'last'], {'first_attr': 1})
            dupes = xl.count_duplicates()
            self.assertEqual(dupes, 3)

        def test_xlist_remove_dupes_int(self):
            xl = XList([1, 2, 2, 3, 3, 3], {'first_attr': 1})
            nodupe = xl.remove_duplicates()
            self.assertEqual(type(nodupe), type(XList(['test', 'again'])))
            self.assertEqual(nodupe.count(1), 1)
            self.assertEqual(nodupe.count(2), 1)
            self.assertEqual(nodupe.count(3), 1)

        def test_xlist_difference(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            xl2 = XList([2, 4, 5])
            diff = xl.difference(xl2)  # returns items in XList that are not in parameter list/XList as set
            self.assertTrue(1 in diff)
            self.assertTrue(3 in diff)
            self.assertFalse(2 in diff)
            self.assertFalse(4 in diff)
            self.assertFalse(5 in diff)

        def test_xlist_intersection(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            xl2 = XList([2, 4, 5])
            inter = xl.intersection(xl2) # returns items in both XList and parameter list/XList
            self.assertTrue(2 in inter)
            self.assertFalse(1 in inter)
            self.assertFalse(3 in inter)
            self.assertFalse(4 in inter)
            self.assertFalse(5 in inter)

        def test_xlist_map_items(self):
            def cap_val(xlist_item):
                return xlist_item.upper()
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.map_to_items(cap_val)
            self.assertTrue('ONE' in nl)
            self.assertTrue('TWO' in nl)
            self.assertTrue('THREE' in nl)
            self.assertFalse('one' in nl)
            self.assertFalse('two' in nl)
            self.assertFalse('three' in nl)

        def test_xlist_map_items_noreturn_value(self):
            def no_return(xlist_val):
                x = 1
            xl = XList(['one', 'two', 'three'], {'first_attr': 1})
            nl = xl.map_to_items(no_return)
            self.assertTrue(nl[0] == None)

        def test_xlist_conditional_map_items(self):
            def true_a(xdict_key):
                return xdict_key.startswith('a')

            def cap_val(xdict_val):
                return xdict_val.upper()

            xl = XList(['all', 'many', 'none'], {'first_attr': 1})
            nl = xl.conditional_map_to_items(true_a, cap_val)
            self.assertTrue('ALL' in nl)
            self.assertFalse('all' in nl)
            self.assertFalse('MANY' in nl)
            self.assertFalse('NONE' in nl)
            self.assertTrue(nl[0] == 'ALL')
            self.assertTrue(nl[1] == 'many')
            self.assertTrue(nl[2] == 'none')

        def test_xlist_count_case_insensitive(self):
            xl = XList(['MANY', 'many', 'Many'], {'first_attr': 1})
            nl = xl.count_ci('Many')
            self.assertTrue(nl == 3)

        def test_xlist_count_case_insensitive_withother(self):
            xl = XList(['MANY', 1, 'many'], {'first_attr': 1})
            nl = xl.count_ci('Many')
            self.assertTrue(nl == 2)

        def test_xlist_random_noexception(self): # just confirm that it does not raise exception, can't test result
            xl = XList([1 , 2, 3], {'first_attr': 1})
            nl = xl.random()
            self.assertTrue(type(nl) == type(1))

        def test_xlist_random_sample_noexception(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            nl = xl.random_sample(2)
            self.assertTrue(len(nl) == 2)

        def test_xlist_shuffle(self):
            xl = XList([1 , 2, 3], {'first_attr': 1})
            nl = xl.random_sample(2)
            # no test, just confirm no exception

        def test_xlist_wildcard_match_nonstring(self):
            xl = XList(['MANY', 1, 'many'], {'first_attr': 1})
            with self.assertRaises(TypeError):
                nl = xl.wildcard_match('m*') # when the list contains non-string types, TypeError is raised

        def test_xlist_wildcard_match(self):
            xl = XList(['MANY', 'many', 'Many'], {'first_attr': 1})
            nl = xl.wildcard_match('m*')
            self.assertTrue(len(nl) == 1)
            self.assertEqual(nl[0], 'many')

        def test_xlist_wildcard_match_nomatches(self):
            xl = XList(['MANY', 'many', 'Many'], {'first_attr': 1})
            nl = xl.wildcard_match('t*')
            self.assertTrue(len(nl) == 0)

        def test_xlist_multi_wildcard_match(self):
            xl = XList(['many', 'tom', 'Many'], {'first_attr': 1})
            nl = xl.multi_wildcard_match('m*|t*')
            self.assertTrue(len(nl) == 2)
            self.assertTrue('many' in nl)
            self.assertTrue('tom' in nl)
            self.assertFalse('Many' in nl)

        def test_xlist_multi_wildcard_match_nomatches(self):
            xl = XList(['many', 'tom', 'Many'], {'first_attr': 1})
            nl = xl.multi_wildcard_match('z*|*l')
            self.assertTrue(len(nl) == 0)

        def test_xlist_cast_xset(self):
            xl = XList(['many', 'tom', 'Many'], {'first_attr': 1})
            xs = xl.xset()
            self.assertEqual(type(xs), type(XSet({1,2})))

        def test_xlist_cast_xfset(self):
            xl = XList(['many', 'tom', 'Many'], {'first_attr': 1})
            xs = xl.xfset()
            self.assertEqual(type(xs), type(XFSet({1,2})))

        def test_xlist_cast_xtuple(self):
            xl = XList(['many', 'tom', 'Many'], {'first_attr': 1})
            xs = xl.xtuple()
            self.assertEqual( type(xs), type(XTuple((1,2))) )

        #------------------------------------------------------------------------------
        # XMaxHeap Tests
        #------------------------------------------------------------------------------

        def test_xmaxheap_contructor(self):
            mh = XMaxHeap()
            self.assertFalse(mh) # queue that is empty is False
            mh.push('first', 1)
            self.assertTrue(mh) # queue that contains item is True

        def test_xmaxheap_type(self):
            mh = XMaxHeap()
            self.assertTrue(type(mh) == type(XMaxHeap()))

        def test_xmaxheap_constructor_attributes(self):
            mh = XMaxHeap({'first': 'test'})
            self.assertEqual(mh.first, 'test')

        def test_xmaxheap_push_and_pop_items(self):
            mh = XMaxHeap({'first': 'test'})
            mh.push('first', 1)
            mh.push('second', 2)
            mh.push('third', 2)
            mh.push('fourth', 3)
            self.assertEqual(len(mh), 4)
            # pop first item off
            firstpop = mh.pop()
            self.assertEqual(len(mh), 3)
            self.assertEqual(firstpop, 'fourth')
            # pop second item off
            secondpop = mh.pop()
            self.assertEqual(len(mh), 2)
            self.assertEqual(secondpop, 'second') # when matching priority, uses FIFO
            # pop third item off
            thirdpop = mh.pop()
            self.assertEqual(len(mh), 1)
            self.assertEqual(thirdpop, 'third')  # FIFO sequence
            # pop fourth and last item
            fourthpop = mh.pop()
            self.assertEqual(len(mh), 0)
            self.assertEqual(fourthpop, 'first')
            # pop on an empty queue returns None
            fifthpop = mh.pop()
            self.assertEqual(len(mh), 0)
            self.assertEqual(fifthpop, None)

        def test_xmaxheap_pushpop_method(self):
            mh = XMaxHeap({'first': 'test'})
            mh.push('first', 1)
            result = mh.pushpop('second', 2)
            self.assertEqual(len(mh), 1)
            self.assertEqual(result, 'second') # get the highest priority item back, even if it is the one that was just placed on queue
            result2 = mh.pop()
            self.assertEqual(result2, 'first')

        def test_xmaxheap_pushpop_method_lower_priority(self):
            mh = XMaxHeap({'first': 'test'})
            mh.push('first', 2)
            result = mh.pushpop('second', 1)
            self.assertEqual(len(mh), 1)
            self.assertEqual(result, 'first') # get the highest priority item back
            result2 = mh.pop()
            self.assertEqual(result2, 'second')

        #------------------------------------------------------------------------------
        # XMinHeap tests
        #------------------------------------------------------------------------------

        def test_xminheap_constructor(self):
            mh = XMinHeap()
            self.assertFalse(mh) # queue that is empty is False
            mh.push('first', 1)
            self.assertTrue(mh) # queue that contains item is True

        def test_xminheap_type(self):
            mh = XMinHeap()
            self.assertTrue(type(mh) == type(XMinHeap()))

        def test_xminheap_constructor_attributes(self):
            mh = XMinHeap({'first': 'test'})
            self.assertEqual(mh.first, 'test')

        def test_xminheap_push_and_pop_items(self):
            mh = XMinHeap({'first': 'test'})
            mh.push('first', 1)
            mh.push('second', 2)
            mh.push('third', 2)
            mh.push('fourth', 3)
            self.assertEqual(len(mh), 4)
            # pop first item off
            firstpop = mh.pop()
            self.assertEqual(len(mh), 3)
            self.assertEqual(firstpop, 'first')
            # pop second item off
            secondpop = mh.pop()
            self.assertEqual(len(mh), 2)
            self.assertEqual(secondpop, 'second') # when matching priority, uses FIFO
            # pop third item off
            thirdpop = mh.pop()
            self.assertEqual(len(mh), 1)
            self.assertEqual(thirdpop, 'third')  # FIFO sequence
            # pop fourth and last item
            fourthpop = mh.pop()
            self.assertEqual(len(mh), 0)
            self.assertEqual(fourthpop, 'fourth')
            # pop on an empty queue returns None
            fifthpop = mh.pop()
            self.assertEqual(len(mh), 0)
            self.assertEqual(fifthpop, None)

        def test_xminheap_pushpop_method(self):
            mh = XMinHeap({'first': 'test'})
            mh.push('first', 2)
            result = mh.pushpop('second', 1)
            self.assertEqual(len(mh), 1)
            self.assertEqual(result, 'second') # get the lowest priority item back, even if it is the one that was just placed on queue
            result2 = mh.pop()
            self.assertEqual(result2, 'first')

        def test_xminheap_pushpop_method_lower_priority(self):
            mh = XMinHeap({'first': 'test'})
            mh.push('first', 1)
            result = mh.pushpop('second', 2)
            self.assertEqual(len(mh), 1)
            self.assertEqual(result, 'first') # get the lowest priority item back
            result2 = mh.pop()
            self.assertEqual(result2, 'second')


