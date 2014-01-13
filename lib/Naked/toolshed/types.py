#!/usr/bin/env python

##TODO : try/catch around the getter methods in case they are missing

#------------------------------------------------------------------------------
# [ NakedObject class ]
#   A generic Python object
#   Assigns object attributes by key in the dictionary argument
#------------------------------------------------------------------------------
class NakedObject:
    # initialize with an attributes dictionary {attribute_name, attribute_value}
    def __init__(self, attributes={}):
        if len(attributes) > 0:
            self._addAttributes(attributes)
        from sys import version_info
        self.py_version = (version_info[0], version_info[1], version_info[2])  # add python version as metadata to the object

    def _addAttributes(self, attributes):
        for key in attributes:
            setattr(self, key, attributes[key])

    def getAttribute(self, attribute):
        return getattr(self, attribute)

    def setAttribute(self, attribute, value):
        setattr(self, attribute, value)

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
    #  +- overload extends XDict with another dictionary
    #  overwrites existing keys with another_dict keys if they are the same
    #------------------------------------------------------------------------------
    def __iadd__(self, another_dict):
        self.update(another_dict)
        return self

    #------------------------------------------------------------------------------
    # [ iter method ] (tuple of each key and value in dictionary)
    #   Generator method that returns a tuples of key, value in dictionary
    #   uses appropriate method from Python 2 and 3
    #------------------------------------------------------------------------------
    def iter(self):
        if self.py_version[0] > 2:
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


    #------------------------------------------------------------------------------
    # Numpy Array Methods
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
    # XList Iterables
    #------------------------------------------------------------------------------
    # [ chain_iter method ] (iterable items of type contained in multiple list arguments)
    #   Generator that returns iterable for each item in the multiple list arguments in sequence (does not require new list)
    #------------------------------------------------------------------------------
    def chain_iter(self, *lists):
        from itertools import chain
        return chain(*lists)

#------------------------------------------------------------------------------
# [ XString class ]
#   An inherited extension to the immutable string object that permits attributes
#   Immutable so there is no setter method, attributes must be set in the constructor
#------------------------------------------------------------------------------
class XString(str):
    def __new__(cls, string_text, attributes={}):
        str_obj = str.__new__(cls, string_text)
        if len(attributes) > 0:
            for key in attributes:
                setattr(str_obj, key, attributes[key])
        from sys import version_info
        self.py_version = (version_info[0], version_info[1], version_info[2]) #add python version as metadata to the object
        return str_obj

    def getAttribute(self, attribute):
        return getattr(self, attribute)


if __name__ == '__main__':
    # ns = XList(['a', 'b', 'c'], {"version":"1.0.1", "test":"code"})
    # print(ns << ['d', 'e', 'f'])
    # print(ns.surround("*", "!"))

    # xd = XDict({'test': 'testing', 'another': 'yep'}, {'a': '1', 'b': '2'})
    # ad = {'this': 'yes', 'is':'more'}
    # xd += ad
    # print(xd)
