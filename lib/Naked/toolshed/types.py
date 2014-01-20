#!/usr/bin/env python
# encoding: utf-8

##TODO : try/catch around the getter methods in case they are missing
from Naked.settings import debug as DEBUG_FLAG

#------------------------------------------------------------------------------
# [ NakedObject class ]
#   A generic Python object
#   Assigns object attributes by key in the dictionary argument
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
        return getattr(self, attribute)

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
# [ XDict class ]
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
    # + overload extends XDict with one or more other dictionaries
    #   overwrites existing keys with key:value pairs from new dictionaries if they are the same keys
    #   returns the updated XDict object
    #------------------------------------------------------------------------------
    def __add__(self, *other_dicts):
        for the_dict in other_dicts:
            self.update(the_dict)
        return self

    #------------------------------------------------------------------------------
    #  +- overload extends XDict with another dictionary
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
    # return XTuple of minimum value, key
    def min_val(self):
        result = min(zip(self.values(), self.keys()))
        return XTuple( result, {'val': result[0], 'key': result[1]} )

    # return XTuple of maximum value, key
    def max_val(self):
        result = max(zip(self.values(), self.keys()))
        return XTuple( result, {'val': result[0], 'key': result[1]} )

    # sum values
    def sum_vals(self):
        return sum(self.values())

    # case sensitive value counts
    def value_count(self, value_name):
        count = 0
        for test_string in self.values():
            if value_name == test_string:
                count += 1
        return count

    # case insensitive string value counts
    def value_count_ci(self, value_name):
        value_name = value_name.lower()
        lower_case_vals = [ x.lower() for x in self.values() ]
        count = 0
        for test_string in lower_case_vals:
            if value_name in test_string:
                count += 1
        return count

    # map a function to every value in the dictionary
    def map_to_vals(self, the_func):
        return XDict( zip(self, map(the_func, self.values())), self._getAttributeDict() )

    # map a function to dicitionary values conditional upon result of a function on keys
    def conditional_map_to_vals(self, conditional_function, result_function):
        for key, value in self.xitems():
            if conditional_function(key):
                self[key] = result_function(self[key])
        return self

    #------------------------------------------------------------------------------
    # XDict Key Methods
    #------------------------------------------------------------------------------
    def intersection(self, another_dict):
        return self.keys() & another_dict.keys()

    def difference(self, another_dict):
        return self.keys() - another_dict.keys()

    # union of one or more dictionaries, key: value overwrite for duplicate keys
    def union(self, *other_dicts):
        for new_dict in other_dicts:
            self.update(new_dict)
        return self

    # map a function to every key in the dictionary
    def map_to_keys(self, the_func):
        return XDict( zip(map(the_func, self.keys()), self.values()), self._getAttributeDict())

    #return random {key: value}
    def random(self):
        import random
        random_key = random.choice(self.keys())
        return {random_key: self[random_key]}

    # return a random sample of `number_of_items` {key:value} pairs as a new dict
    def random_sample(self, number_of_items):
        import random
        random_key_list = random.sample(self, number_of_items)
        new_dict = {}
        for item in random_key_list:
            new_dict[item] = self[item]
        return new_dict

    #------------------------------------------------------------------------------
    # [ xitems method ] (tuple of each key and value in dictionary)
    #   Generator method that returns tuples of key, value in dictionary
    #   uses appropriate method from Python 2 and 3
    #------------------------------------------------------------------------------
    def xitems(self):
        from Naked.toolshed.python import py_major_version
        if py_major_version() > 2:
            return self.items()
        else:
            return self.iteritems()

#------------------------------------------------------------------------------
# [ XList class ]
#  An inherited extension to the list object that permits attachment of attributes
#------------------------------------------------------------------------------
class XList(list, NakedObject):
    def __init__(self, list_obj, attributes={}):
        list.__init__(self, list_obj)
        NakedObject.__init__(self, attributes)

    #------------------------------------------------------------------------------
    # Operator Overloads/Defs
    #------------------------------------------------------------------------------

    # + operator overload extends the XList with one or more lists
    def __add__(self, *other_lists):
        for the_list in other_lists:
            self.extend(the_list)
        return self

    #   += operator overload to extend the XList with the argument list
    def __iadd__(self, another_list):
        self.extend(another_list)
        return self

    #   >> operator is overloaded to extend the argument list with the XList
    def __rshift__(self, another_list):
        another_list.extend(self)
        return another_list

    #   << operator is overloaded to extend the XList with the argument list
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
    # [ prefix method ] (list of strings)
    #  Prepend a string to each list item string
    #------------------------------------------------------------------------------
    def prefix(self, before):
        return [ "".join([before, x]) for x in self ]

    #------------------------------------------------------------------------------
    # [ postfix method ] (list of strings)
    #  Append a string to each list item string
    #------------------------------------------------------------------------------
    def postfix(self, after):
        return [ "".join([x, after]) for x in self ]

    #------------------------------------------------------------------------------
    # [ surround method ] (list of strings)
    #  Surround each list item with a before and after string argument passed to the method
    #------------------------------------------------------------------------------
    def surround(self, before, after):
        return [ "".join([before, x, after]) for x in self ]

    # Numeric methods
    def max(self):
        return max(self)

    def min(self):
        return min(self)

    def sum(self):
        return sum(self)

    # remove duplicate items in an XList
    def remove_duplicates(self):
        return XList( set(self), self._getAttributeDict() )

    # map a function to every item in the XList
    def map_to_items(self, the_func):
        return XList( map(the_func, self), self._getAttributeDict() )

    # map a function to items that return True on `conditional_function`
    def conditional_map_to_items(self, conditional_function, result_function):
        for index, item in enumerate(self):
            if conditional_function(item):
                self[index] = result_function(item)
        return self

    # count of an item of `test_string`
    def count_item(self, test_string):
        count = 0
        for item_value in self:
            if test_string == item_value:
                count += 1
        return count

    # return a random item from list
    def random(self):
        import random
        return random.choice(self)

    # return random sample of `number_of_items` items from list
    def random_sample(self, number_of_items):
        import random
        return random.sample(self, number_of_items)

    # randomly shuffle the items in the list
    def shuffle(self):
        import random
        random.shuffle(self)
        return self

    # single wildcard match
    def wildcard_match(self, wildcard):
        if self.hasAttribute('nkd_fnmatchcase'):
            fnmatchcase = self.nkd_fnmatchcase
        else:
            from fnmatch import fnmatchcase
            self.nkd_fnmatchcase = fnmatchcase
        return [ x for x in self if fnmatchcase(x, wildcard) ]

    # multiple wildcard match, separate wildcards with | symbol in the argument
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
    # Conversion Methods
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

    def xset(self):
        attr_dict = self._getAttributeDict()
        return XSet(set(self), attr_dict)

    def xfset(self):
        attr_dict = self._getAttributeDict()
        return XFSet(set(self), attr_dict)

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
# [ XPriorityQueue class ]
#
#------------------------------------------------------------------------------
import heapq
class XPriorityQueue(NakedObject):
    def __init__(self, initial_iterable=[], attributes={}):
        NakedObject.__init__(self, attributes)
        self._queue = []
        self._index = 0

    # O(log n) complexity
    def push(self, the_object, priority):
        heapq.heappush(self._queue, (-priority, self._index, the_object))
        self._index += 1

    # O(log n) complexity
    def pop(self):
        return heapq.heappop(self._queue)[-1]

    # push new object and return the highest priority object
    def push_and_pop(self, the_object, priority):
        heapq.heappush(self._queue, (-priority, self._index, the_object))
        self._index += 1
        return heapq.heappop(self._queue)[-1]


#------------------------------------------------------------------------------
# [ XQueue class ]
#
#------------------------------------------------------------------------------
from collections import deque
class XQueue(deque, NakedObject):
    def __init__(self, initial_iterable=[], attributes={}, max_length=10):
        deque.__init__(self, initial_iterable, max_length)
        NakedObject.__init__(self, attributes)


#------------------------------------------------------------------------------
# [ XSet class ]
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
# [ XFSet class ]
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
        return getattr(self, attribute)

    def xlist(self):
        attr_dict = self._getAttributeDict()
        return XList(list(self), attr_dict)

    def xset(self):
        attr_dict = self._getAttributeDict()
        return XSet(self, attr_dict)

# TODO: test for unicode and use it instead of str in Py2
#------------------------------------------------------------------------------
# [ XString class ]
#   An inherited extension to the immutable string object that permits attributes
#   Immutable so there is no setter method, attributes must be set in the constructor
#   Python 2: byte string by default, can cast to normalized UTF-8 with unicode() method
#   Python 3: unicode Py3 string by default, can normalize with unicode() method
#------------------------------------------------------------------------------
class XString(str):
    def __new__(cls, string_text, attributes={}):
        str_obj = str.__new__(cls, string_text)
        if len(attributes) > 0:
            for key in attributes:
                setattr(str_obj, key, attributes[key])
        return str_obj

    def getAttribute(self, attribute):
        return getattr(self, attribute)

    # fastest substring search truth test
    def contains(self, substring):
        return substring in self

    # split the string on one or more delimiters, return list
    # if single char, then uses str.split(), if multiple chars then uses re.split
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

#------------------------------------------------------------------------------
# [ XTuple class ]
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
    # pass
    # nl = XList(['a', 'b', 'c'], {"version":"1.0.1", "test":"code"})
    # nl = nl + ['d', 'e', 'f'] + ['g', 'h', 'i']
    # print(nl)
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

    # xd = XDict({'test': 0, 'another': 0}, {'a': '1', 'b': '2'})
    # ad = {'test2': 0, 'is': 0}
    # ld = {'last': 0}
    # xd = xd + ad + ld
    # print(xd)
    # print(xd.conditional_map_to_vals(matcher, resulter))

    # nl = XList([ 'test.txt', 'bogus.txt', 'test.py', 'another.rb', 'est.doc', 'est.py' ])
    # print(nl.multi_wildcard_match('*.py|*.txt|*.doc'))

    # xstr = XString("Hey! Cœur It's Bengali ব য,\nand here is some more ২")
    # ustr = xstr.unicode()
    # print(isinstance(ustr, bytes))
    # print(xstr)

