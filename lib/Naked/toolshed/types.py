#!/usr/bin/env python
# encoding: utf-8

from Naked.settings import debug as DEBUG_FLAG

#------------------------------------------------------------------------------
# [[ NakedObject class ]]
#   A generic Python object
#   Assigns object attributes by key name in the dictionary argument to the constructor
#   The methods are inherited by other mutable Naked object extension types
#------------------------------------------------------------------------------
class NakedObject:
    # initialize with an attributes dictionary {attribute_name, attribute_value}
    def __init__(self, attributes={}):
        if len(attributes) > 0:
            for key in attributes:
                setattr(self, key, attributes[key])

    #------------------------------------------------------------------------------
    # [ _getAttributeDict method ] (dictionary)
    #  returns a dictionary of the NakedObject instance attributes
    #------------------------------------------------------------------------------
    def _getAttributeDict(self):
        return self.__dict__

    #------------------------------------------------------------------------------
    # [ getAttribute method ] (attribute dependent type)
    #  returns the respective attribute for the `attribute` name on the NakedObject instance
    #------------------------------------------------------------------------------
    def getAttribute(self, attribute):
        if hasattr(self, attribute):
            return getattr(self, attribute)
        else:
            return None

    #------------------------------------------------------------------------------
    # [ setAttribute method ] (no return value)
    #  sets a NakedObject attribute `value` for the `attribute` name
    #------------------------------------------------------------------------------
    def setAttribute(self, attribute, value):
        setattr(self, attribute, value)

    #------------------------------------------------------------------------------
    # [ hasAttribute method ] (boolean)
    #  returns truth test for presence of an `attribute` name on the NakedObject
    #------------------------------------------------------------------------------
    def hasAttribute(self, attribute):
        return hasattr(self, attribute)

#------------------------------------------------------------------------------
# [[ XDict class ]]
#   An inherited extension to the dictionary object that permits attachment of attributes
#------------------------------------------------------------------------------
class XDict(dict, NakedObject):
    def __init__(self, dict_obj, attributes={}):
        dict.__init__(self, dict_obj)
        NakedObject.__init__(self, attributes)

    #------------------------------------------------------------------------------
    # XDict Operator Overloads
    #------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    # + overload
    #   overwrites existing keys with key:value pairs from new dictionaries if they are the same keys
    #   returns the updated XDict object
    #------------------------------------------------------------------------------
    def __add__(self, other_dict):
        self.update(other_dict)
        return self

    #------------------------------------------------------------------------------
    #  +- overload
    #  overwrites existing keys with another_dict (right sided argument) keys if they are the same keys
    #  returns the updated XDict object
    #------------------------------------------------------------------------------
    def __iadd__(self, another_dict):
        self.update(another_dict)
        return self

    #------------------------------------------------------------------------------
    # << overload extends XDict with another dictionary
    #  overwrites existing keys with another_dict (right sided argument) keys if they are the same
    #------------------------------------------------------------------------------
    def __lshift__(self, another_dict):
        self.update(another_dict)
        return self

    #------------------------------------------------------------------------------
    # XDict Value Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ conditional_map_to_vals method ] (XDict)
    #  returns the original XDict with values that meet True condition in `conditional_function`
    #  modified as per the `mapped_function` with single value argument call
    #------------------------------------------------------------------------------
    def conditional_map_to_vals(self, conditional_function, mapped_function):
        for key, value in self.xitems():
            if conditional_function(key):
                self[key] = mapped_function(value)
        return self

    #------------------------------------------------------------------------------
    # [ map_to_vals method ] (XDict)
    #  returns the original XDict with all values modified as per the `mapped_function`
    #------------------------------------------------------------------------------
    def map_to_vals(self, mapped_function):
        # return XDict( zip(self, map(mapped_function, self.values())), self._getAttributeDict() ) - slower in Py2
        for key, value in self.xitems():
            self[key] = mapped_function(value)
        return self

    #------------------------------------------------------------------------------
    # [ val_xlist method ] (XList)
    #  return an XList of the values in the XDict
    #------------------------------------------------------------------------------
    def val_xlist(self):
        return XList(self.values(), self._getAttributeDict())

    #------------------------------------------------------------------------------
    # [ max_val method ] (tuple of maximum value and associated key)
    #------------------------------------------------------------------------------
    def max_val(self):
        return max(zip(self.values(), self.keys()))

    #------------------------------------------------------------------------------
    # [ min_val method ] (tuple of minimum value and associated key)
    #------------------------------------------------------------------------------
    def min_val(self):
        return min(zip(self.values(), self.keys()))

    #------------------------------------------------------------------------------
    # [ sum_vals method ] (numeric return type dependent upon original value type)
    #  returns sum of all values in the dictionary
    #------------------------------------------------------------------------------
    def sum_vals(self):
        return sum(self.values())

    #------------------------------------------------------------------------------
    # [ val_count method ] (integer)
    #  returns an integer value for the total count of `value_name` in the dictionary values
    #  Case sensitive test for strings
    #------------------------------------------------------------------------------
    def val_count(self, value_name):
        count = 0
        for test_string in self.values():
            if value_name == test_string:
                count += 1
        return count

    #------------------------------------------------------------------------------
    # [ value_count_ci method ] (integer)
    #  returns an integer value for the total count of case insensitive `value_name`
    #  strings/char in the dictionary values.  This is a string only search method
    #------------------------------------------------------------------------------
    def val_count_ci(self, value_name):
        value_name = value_name.lower()
        lower_case_vals = [ x.lower() for x in self.values() ]
        count = 0
        for test_string in lower_case_vals:
            if value_name in test_string:
                count += 1
        return count


    #------------------------------------------------------------------------------
    # XDict Key Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ difference method ] (difference set of keys)
    #  definition: keys that are included in self, but not in `another_dict`
    #------------------------------------------------------------------------------
    def difference(self, another_dict):
        return set(self.keys()) - set(another_dict.keys())

    #------------------------------------------------------------------------------
    # [ intersection method ] (intersection set of keys)
    #   definition: keys that are included in both self and `another_dict`
    #------------------------------------------------------------------------------
    def intersection(self, another_dict):
        return set(self.keys()) & set(another_dict.keys())

    #------------------------------------------------------------------------------
    # [ key_xlist method ] (XList)
    #  returns an XList of the keys in the XDict
    #------------------------------------------------------------------------------
    def key_xlist(self):
        return XList(self.keys(), self._getAttributeDict())

    #------------------------------------------------------------------------------
    # [ random method ] (dictionary)
    #  return new Python dictionary with single, random key:value pair
    #------------------------------------------------------------------------------
    def random(self):
        import random
        random_key = random.choice(self.keys())
        return {random_key: self[random_key]}

    #------------------------------------------------------------------------------
    # [ random_sample method ] (dictionary)
    #  return new Python dictionary with `number_of_items` random key:value pairs
    #------------------------------------------------------------------------------
    def random_sample(self, number_of_items):
        import random
        random_key_list = random.sample(self, number_of_items)
        new_dict = {}
        for item in random_key_list:
            new_dict[item] = self[item]
        return new_dict

    #------------------------------------------------------------------------------
    # [ xitems method ] (tuple)
    #   Generator method that returns tuples of every key, value in dictionary
    #   uses appropriate method from Python 2 and 3 interpreters
    #------------------------------------------------------------------------------
    def xitems(self):
        from Naked.toolshed.python import py_major_version
        if py_major_version() > 2:
            return self.items()
        else:
            return self.iteritems()

#------------------------------------------------------------------------------
# [[ XList class ]]
#  An inherited extension to the list object that permits attachment of attributes
#------------------------------------------------------------------------------
class XList(list, NakedObject):
    def __init__(self, list_obj, attributes={}):
        list.__init__(self, list_obj)
        NakedObject.__init__(self, attributes)

    #------------------------------------------------------------------------------
    # XList Operator Overloads
    #------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    # + operator overload
    #   extends XList with one or more other lists (`*other_lists`)
    #------------------------------------------------------------------------------
    def __add__(self, *other_lists):
        for the_list in other_lists:
            self.extend(the_list)
        return self

    #------------------------------------------------------------------------------
    # += overload
    #  extends XList with one other list (`another_list`)
    #------------------------------------------------------------------------------
    def __iadd__(self, another_list):
        self.extend(another_list)
        return self

    #------------------------------------------------------------------------------
    # >> overload
    #  extends the argument list with the self list (left extends right side)
    #------------------------------------------------------------------------------
    def __rshift__(self, another_list):
        another_list.extend(self)
        return another_list

    #------------------------------------------------------------------------------
    # << overload
    #  extends self list with the argument list (right extends left side)
    #------------------------------------------------------------------------------
    def __lshift__(self, another_list):
        self.extend(another_list)
        return self

    #------------------------------------------------------------------------------
    # XList Methods
    #------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    # XList String Methods
    #------------------------------------------------------------------------------
    # [ join method ] (string)
    #  Concatenate strings in the list and return
    #  Default separator between string list values is an empty string
    #  Pass separator character(s) as an argument to the method
    #------------------------------------------------------------------------------
    def join(self, separator=""):
        return separator.join(self)

    #------------------------------------------------------------------------------
    # [ postfix method ] (list of strings)
    #  Append a string to each list item string
    #------------------------------------------------------------------------------
    def postfix(self, after):
        return [ "".join([x, after]) for x in self ]

    #------------------------------------------------------------------------------
    # [ prefix method ] (list of strings)
    #  Prepend a string to each list item string
    #------------------------------------------------------------------------------
    def prefix(self, before):
        return [ "".join([before, x]) for x in self ]

    #------------------------------------------------------------------------------
    # [ surround method ] (list of strings)
    #  Surround each list item string with a before and after string argument passed to the method
    #------------------------------------------------------------------------------
    def surround(self, before, after):
        return [ "".join([before, x, after]) for x in self ]

    #------------------------------------------------------------------------------
    # XList Numeric Methods
    #------------------------------------------------------------------------------
    # [ max method ] (list dependent type, single value)
    #  return maximum value from the list items
    #------------------------------------------------------------------------------
    def max(self):
        return max(self)

    #------------------------------------------------------------------------------
    # [ min method ] (list dependent type, single value)
    #  return minimum value from the list items
    #------------------------------------------------------------------------------
    def min(self):
        return min(self)

    #------------------------------------------------------------------------------
    # [ sum method ] (list dependent type, single value)
    #  return the sum of all list items
    #------------------------------------------------------------------------------
    def sum(self):
        return sum(self)

    #------------------------------------------------------------------------------
    # XList Data Management Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ count_duplicates method ] (integer)
    #   returns an integer count of number of duplicate values
    #------------------------------------------------------------------------------
    def count_duplicates(self):
        length = len(self)
        length_wo_dupes = len(set(self))
        return length - length_wo_dupes

    #------------------------------------------------------------------------------
    # [ remove_duplicates ] (XList)
    #  returns a new XList with duplicates removed
    #------------------------------------------------------------------------------
    def remove_duplicates(self):
        return XList( set(self), self._getAttributeDict() )

    #------------------------------------------------------------------------------
    # XList Function Mapping Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ map_to_items method ] (XList)
    #  returns original XList with modification of each item based upon `mapped_function`
    #------------------------------------------------------------------------------
    def map_to_items(self, mapped_function):
        # return XList( map(mapped_function, self), self._getAttributeDict() ) - slower
        for index, item in enumerate(self):
            self[index] = mapped_function(item)
        return self

    #------------------------------------------------------------------------------
    # [ conditional_map_to_items method ] (XList)
    #  returns original XList with modification of items that meet True condition in
    #  `conditional_function` with change performed as defined in `mapped_function`
    #------------------------------------------------------------------------------
    def conditional_map_to_items(self, conditional_function, mapped_function):
        for index, item in enumerate(self):
            if conditional_function(item):
                self[index] = mapped_function(item)
        return self

    #------------------------------------------------------------------------------
    # XList Stats/Distribution Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ count_item method ] (integer)
    #  returns an integer count of the number of items in the list that == `test_obj`
    #------------------------------------------------------------------------------
    def count_item(self, test_obj):
        count = 0
        for item_value in self:
            if test_obj == item_value:
                count += 1
        return count

    ## TODO : add a case-insensitive count_item method for strings

    #------------------------------------------------------------------------------
    # [ random method ] (list)
    #  returns a single item list with a random element from the original XList
    #------------------------------------------------------------------------------
    def random(self):
        import random
        return random.choice(self)

    #------------------------------------------------------------------------------
    # [ random_sample method ] (list)
    #  returns a list with one or more random items from the original XList
    #  number of items determined by the `number_of_items` argument
    #------------------------------------------------------------------------------
    def random_sample(self, number_of_items):
        import random
        return random.sample(self, number_of_items)

    #------------------------------------------------------------------------------
    # [ shuffle method ] (XList)
    #   randomly shuffle the contents of the list
    #------------------------------------------------------------------------------
    def shuffle(self):
        import random
        random.shuffle(self)
        return self

    #------------------------------------------------------------------------------
    # XList Match Methods
    #------------------------------------------------------------------------------
    #------------------------------------------------------------------------------
    # [ wildcard_match method ] (list)
    #  returns a list of items that match the `wildcard` argument
    #------------------------------------------------------------------------------
    def wildcard_match(self, wildcard):
        if self.hasAttribute('nkd_fnmatchcase'):
            fnmatchcase = self.nkd_fnmatchcase
        else:
            from fnmatch import fnmatchcase
            self.nkd_fnmatchcase = fnmatchcase
        return [ x for x in self if fnmatchcase(x, wildcard) ]

    #------------------------------------------------------------------------------
    # [ multi_wildcard_match method ] (list)
    #  returns a list of items that match one or more | separated wildcards passed as string
    #------------------------------------------------------------------------------
    def multi_wildcard_match(self, wildcards):
        if self.hasAttribute('nkd_fnmatchcase'):
            fnmatchcase = self.nkd_fnmatchcase
        else:
            from fnmatch import fnmatchcase
            self.nkd_fnmatchcase = fnmatchcase
        wc_list = wildcards.split('|')
        return_list = []
        for wc in wc_list:
            temp_list = [ x for x in self if fnmatchcase(x, wc) ]
            for result in temp_list:
                return_list.append(result)
        return return_list

    #------------------------------------------------------------------------------
    # XList Conversion Methods
    #------------------------------------------------------------------------------
    # [ ndarray method ] (Numpy ndarray object)
    #  returns a Numby ndarray object by conversion from the XList object
    #  user must have Numpy installed or ImportError is raised
    #------------------------------------------------------------------------------
    def ndarray(self):
        try:
            import numpy as np
            return np.array(self)
        except ImportError as ie:
            if DEBUG_FLAG:
                sys.stderr.write("Naked Framework Error: unable to return base filename from filename() function (Naked.toolshed.system).")
            raise ie

    #------------------------------------------------------------------------------
    # [ xset method ] (XSet)
    #  return an XSet with unique XList item values and XList attributes
    #------------------------------------------------------------------------------
    def xset(self):
        attr_dict = self._getAttributeDict()
        return XSet(set(self), attr_dict)

    #------------------------------------------------------------------------------
    # [ xfset method ] (XFSet)
    #  return an XFSet with unique XList item values and XList attributes
    #------------------------------------------------------------------------------
    def xfset(self):
        attr_dict = self._getAttributeDict()
        return XFSet(set(self), attr_dict)

    #------------------------------------------------------------------------------
    # [ xtuple method ] (XTuple)
    #  returns an XTuple with XList item values and XList attributes
    #------------------------------------------------------------------------------
    def xtuple(self):
        attr_dict = self._getAttributeDict()
        return XTuple(tuple(self), attr_dict)

    #------------------------------------------------------------------------------
    # XList Iterables
    #------------------------------------------------------------------------------
    # [ chain_iter method ] (iterable items of type contained in multiple list arguments)
    #   Generator that returns iterable for each item in the multiple list arguments in sequence (does not require new list)
    #------------------------------------------------------------------------------
    def chain_iter(self, *lists):
        from itertools import chain
        return chain(*lists)


#------------------------------------------------------------------------------
# [[ XPriorityQueue class ]]
#
#------------------------------------------------------------------------------
from heapq import heappush, heappop
class XPriorityQueue(NakedObject):
    def __init__(self, initial_iterable=[], attributes={}):
        NakedObject.__init__(self, attributes)
        self._queue = []
        self._index = 0

    # O(log n) complexity
    def push(self, the_object, priority):
        heappush(self._queue, (-priority, self._index, the_object))
        self._index += 1

    # O(log n) complexity
    def pop(self):
        return heappop(self._queue)[-1]

    # push new object and return the highest priority object
    def push_and_pop(self, the_object, priority):
        heappush(self._queue, (-priority, self._index, the_object))
        self._index += 1
        return heappop(self._queue)[-1]


#------------------------------------------------------------------------------
# [[ XQueue class ]]
#
#------------------------------------------------------------------------------
from collections import deque
class XQueue(deque, NakedObject):
    def __init__(self, initial_iterable=[], attributes={}, max_length=10):
        deque.__init__(self, initial_iterable, max_length)
        NakedObject.__init__(self, attributes)


#------------------------------------------------------------------------------
# [[ XSet class ]]
#  An inherited extension to the mutable set object that permits attribute assignment
#  Inherits from set and from NakedObject (see methods in NakedObject at top of this module
#------------------------------------------------------------------------------
class XSet(set, NakedObject):
    def __init__(self, set_obj, attributes={}):
        set.__init__(self, set_obj)
        NakedObject.__init__(self, attributes)

    #   << operator is overloaded to extend the XSet with a second set
    def __lshift__(self, another_set):
        self.update(another_set)
        return self

    #   += operator overload to extend the XSet with a second set
    def __iadd__(self, another_set):
        self.update(another_set)
        return self

    def xlist(self):
        attr_dict = self._getAttributeDict()
        return XList(list(self), attr_dict)

    def xfset(self):
        attr_dict = self._getAttributeDict()
        return XFSet(self, attr_dict)

#------------------------------------------------------------------------------
# [[ XFSet class ]]
#  An inherited extension to the immutable frozenset object that permits attribute assignment
#  Immutable so there is no setter method, attributes must be set in the constructor
#------------------------------------------------------------------------------
class XFSet(frozenset):
    def __new__(cls, the_set, attributes={}):
        set_obj = frozenset.__new__(cls, the_set)
        if len(attributes) > 0:
            for key in attributes:
                setattr(set_obj, key, attributes[key])
        return set_obj

    def _getAttributeDict(self):
        return self.__dict__

    def getAttribute(self, attribute):
        if hasattr(self, attribute):
            return getattr(self, attribute)
        else:
            return None

    def xlist(self):
        attr_dict = self._getAttributeDict()
        return XList(list(self), attr_dict)

    def xset(self):
        attr_dict = self._getAttributeDict()
        return XSet(self, attr_dict)


#------------------------------------------------------------------------------
# [[ XString class ]]
#   An inherited extension to the immutable string object that permits attribute assignment
#   Immutable so there is no setter method, attributes must be set in the constructor
#   Python 2: byte string by default, can cast to normalized UTF-8 with XString().unicode() method
#   Python 3: string (that permits unicode) by default, can normalize with XString().unicode() method
#------------------------------------------------------------------------------
class XString(str):
    def __new__(cls, string_text, attributes={}):
        str_obj = str.__new__(cls, string_text)
        if len(attributes) > 0:
            for key in attributes:
                setattr(str_obj, key, attributes[key])
        return str_obj

    def getAttribute(self, attribute):
        if hasattr(self, attribute):
            return getattr(self, attribute)
        else:
            return None

    ## TODO: see where + vs. join breakpoint becomes important
    def concat(self, *strings):
        str_list = []
        for x in strings:
            str_list.append(x)
        return "".join(str_list)

    # fastest substring search truth test
    def contains(self, substring):
        return substring in self

    # split the string on one or more delimiters, return list
    # if up to two chars, then uses str.split(), if more chars then use re.split
    def xsplit(self, split_delimiter):
        length = len(split_delimiter)
        if length > 2:
            import re
            split_delimiter = "".join([ '[', split_delimiter, ']' ])
            return re.split(split_delimiter, self)
        elif length > 1:
            delim2 = split_delimiter[1]
            first_list = self.split(split_delimiter[0])
            result_list = []
            for item in first_list:
                for subitem in item.split(delim2):
                    result_list.append(subitem)
            return result_list
        else:
            return self.split(split_delimiter)

    # split the string on one or more characters and return items in set
    def xsplit_set(self, split_delimiter):
        return set(self.xsplit(split_delimiter))

    # str begins with substring - faster than str.startswith()
    def begins(self, begin_string):
        return begin_string in self[0:len(begin_string)]

    # str ends with substring - faster than str.endswith()
    def ends(self, end_string):
        return end_string in self[-len(end_string):]

    # case sensitive wildcard match on the XString (boolean returned)
    def wildcard_match(self, wildcard):
        from fnmatch import fnmatchcase
        return fnmatchcase(self, wildcard)

    # convert string to normalized UTF-8 in Python 2 and 3
    def unicode(self):
        from sys import version_info
        from unicodedata import normalize
        if version_info[0] == 2:
            return normalize('NFKD', self.decode('UTF-8'))
        else:
            return normalize('NFKD', self)


# this version works
class XUnicode:
    def __init__(self, string_text, attributes={}):
        import sys
        import unicodedata
        norm_text = unicodedata.normalize('NFKD', string_text)

        class XUnicode_2(unicode):
            def __new__(cls, the_string_text, attributes={}):
                str_obj = unicode.__new__(cls, the_string_text)
                if len(attributes) > 0:
                    for key in attributes:
                        setattr(str_obj, key, attributes[key])
                return str_obj

        class XUnicode_3(str):
            def __new__(cls, the_string_text, attributes={}):
                str_obj = str.__new__(cls, the_string_text)
                if len(attributes) > 0:
                    for key in attributes:
                        setattr(str_obj, key, attributes[key])
                return str_obj


        if sys.version_info[0] == 2:
            self.obj = XUnicode_2(norm_text, attributes)
            self.norm_unicode = norm_text
            self.naked_u_string = self.obj.encode('utf-8') # utf-8 encoded byte string
        elif sys.version_info[0] == 3:
            self.naked_u_string = XUnicode_3(norm_text, attributes).encode('utf-8') # ?

    def __str__(self):
        # return self.naked_u_string
        return self.obj

    def __repr__(self):
        return self.naked_u_string

    def __getattr__(self, the_attribute):
        return self.obj.__dict__[the_attribute]

    def __cmp__(self, other_string):
        return hash(self.naked_u_string) ==  hash(other_string)


#------------------------------------------------------------------------------
# [[ XTuple class ]]
#
#------------------------------------------------------------------------------
class XTuple(tuple):
    def __new__(cls, the_tuple, attributes={}):
        tup_obj = tuple.__new__(cls, the_tuple)
        if len(attributes) > 0:
            for key in attributes:
                setattr(tup_obj, key, attributes[key])
        return tup_obj


if __name__ == '__main__':
    pass
    # no = nobj({"version":"1.0.1", "test":"code"})
    # print(no)
    # print(no.version)
    # print(no.test)
    # nl = XList([1, 2, 3, 1, 2, 5], {"version":"1.0.1", "test":"code"})
    # print(nl.count_duplicates())
    # the_list = list(range(5000))
    # nl = XList(the_list)
    # nq = XPriorityQueue()
    # nq.push('test', 5)
    # nq.push('one', 3)
    # nq.push('another', 4)
    # print(nq.pop())
    # print(nq.pop())
    # print(nq.pop())

    # nl = XList([2, 2, 2, 'another'], {'p': 'attribute'})
    # print(nl)
    # print(nl.count_item(2))
    # nq = XQueue(nl, max_length=2)
    # print(nq)

    # xs = XSet({'test', 'true', 'false'}, {'bonus': 'candy', 'test': 'another'})
    # xs += {'bogus', 'yep'}
    # print(xs)

    # xd = XDict({'test2': 0, 'is': 1}, {'a': '1', 'b': '2'})
    # ad = {'test': 0, 'is': 2}
    # ld = xd.intersection(ad)
    # print(ld)
    # xd = xd + ad + ld
    # print(xd.map_to_vals(pr))
    # print(xd.a)
    # print(xd)
    # print(xd.a)
    # print(xd.min_val())
    # print(xd.conditional_map_to_vals(matcher, resulter))

    # nl = XList([ 'test.txt', 'bogus.txt', 'test.py', 'another.rb', 'est.doc', 'est.py' ])
    # print(nl.multi_wildcard_match('*.py|*.txt|*.doc'))

    # xstr = XString("Hey! Cœur It's Bengali ব য,\nand here is some more ২")
    # ustr = xstr.unicode()
    # print(isinstance(ustr, bytes))
    # print(xstr)

