#!/usr/bin/env python

class Set:
	
	## member function
	## first parameter is _self_, it refers to Object itself

	def __init__(self, values=None):
		""" constructor
		    called when construct it
		    be called by:
			s1 = Set()
			s2 = Set([1, 2, 2, 3])
		"""
		self.dict={} # has dict memeber
		
		if values is not None:
			for value in values:
				self.add(value)

	def __repr__(self):
		"""this is the string representation of Set"""
		return "Sets:" + str(self.dict.keys())

	def add(self, value):
		self.dict[value] = True

	def contains(self, value):
		return value in self.dict

	def remove(self, value):
		del self.dict[value]

s = Set([1, 2, 3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)
