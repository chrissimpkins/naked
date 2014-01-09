#!/usr/bin/env python

#------------------------------------------------------------------------------
# [ NakedObject class ]
#   A generic Python object
#   Assigns object attributes by key in the dictionary argument
#------------------------------------------------------------------------------
class NakedObject:
	# initialize with an attributes dictionary {attribute_name, attribute_value}
    def __init__(self, attributes):
        self._addAttributes(attributes)

    def _addAttributes(self, attributes):
        for key in attributes:
            setattr(self, key, attributes[key])

    def getAttribute(self, attribute):
        return getattr(self, attribute)

    def setAttribute(self, attribute, value):
    	setattr(self, attribute, value)


#------------------------------------------------------------------------------
# [ NakedList class ]
#  An inherited extension to the list object that permits attachment of attributes
#------------------------------------------------------------------------------
class NakedList(list, NakedObject):
	def __init__(self, attributes, *args):
		list.__init__(self, *args)
		NakedObject.__init__(self, attributes)

	# += operator overload to add two lists together
	def __iadd__(self, another_list):
		self.extend(another_list)
		return self



#------------------------------------------------------------------------------
# [ NakedString class ]
#   An inherited extension to the immutable string object that permits attributes
#   Immutable so there is no setter method, attributes must be set in the constructor
#------------------------------------------------------------------------------
class NakedString(str):
	def __new__(cls, string_text, attributes):
		str_obj = str.__new__(cls, string_text)
		for key in attributes:
			setattr(str_obj, key, attributes[key])
		return str_obj

	def getAttribute(self, attribute):
		return getattr(self, attribute)



if __name__ == '__main__':
	ns = NakedList({"version":"1.0.1", "test":"code"}, (1, 2, 3))
	ns += [5, 6, 7]
	print(ns.getAttribute("version"))

