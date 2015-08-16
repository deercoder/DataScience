#!/usr/bin/env python
import math

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

def scalar_multiply(c, v):
	""" c is a number, v is a vector"""
	return [c * v_i for v_i in v]

def vector_mean(vectors):
	""" compute the vector whose ith element is the mean of the
	ith elements of the input vectors"""
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):
	"" v1*w1+v2*w2+...+v3*w3
	return sum(v_i * w_i for v_i, w_i in zip(v,w))


def sum_of_squares(v):
	"""v_1 * v_1 + ... + v_n * v_n"""
	return dot(v, v)


def magnitude(v):
	return math.sqrt(sum_of_square(v)) # square root function

def squared_distance(v, w):
	"""(v_1-w_1)**2 + ... + (v_n-w_n)**2"""
	return sum_of_squares(vector_substract(v, w))

def distance(v, w):
	return math.sqrt(squared_distance(v, w))
