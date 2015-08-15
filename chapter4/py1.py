#!/usr/bin/env python

height_weight_age = [ 70,	# inches,
			170, 	# pounds
			40]	# years

grades = [95,	# exam1
	 80,	# exam2
	 75,	# exam3
	 62]	# exam4

# vectors add componentwise, that means add v[0]+w[0], correspondingly

def vector_add(v, w):
	""" add corresponding elements"""
	return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_substrct(v, w):
	""" substract corresponding elements"""
	return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
	""" sum all corresponding elements"""
	result = vector[0]	# start from first element
	for vector in vectors[1:]:
		result = vector_add(result, vector)	# add them by a loop	
	return result
