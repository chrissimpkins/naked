#!/usr/bin/env python
# encoding: utf-8

import sys
if sys.version_info[0] == 2 and sys.version_info[1] == 7: # do not run with tox in non-2.7 versions (fails because not building the C files)

    import unittest
    from Naked.toolshed.c.types import NakedObject, XDict, XList

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





