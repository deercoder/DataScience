#!/usr/bin/env python
# dictionary, key and value
empty_dict = {}		# Pythonic
empty_dict2 = dict()	# less Pythonic, using constructor
grades = { "Joel":80, "Tim":95 }

# get the value using key
joel_grade = grades["Joel"]

# get KeyError if key is not in the dict
try:
	kates_grade = grades["Kate"]
except KeyError:
	print "no grade for Kate"


# using `in` operator
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False

# get function with default value to avoid exception
joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_one_grade = grades.get("No One")

# assign the value
grades["Tim"] = 99 # replace the old value
grades["Kate"] = 100 # add a third entry
num_students = len(grades)

tweet = {
"user" : "joelgrus",
"text" : "Data Science is Awesome",
"retweet_count" : 100,
"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.key()
tweet_values 


