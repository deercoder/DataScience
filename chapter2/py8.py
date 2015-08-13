#!/usr/bin/env python
# Sets, distinct value

s = set()
s.add(1)
s.add(2)
print s # here it is [1, 2]
s.add(2)
print s # here it prints [1, 2]

x = len(s)
print x # equals 2
y =  2 in s
z =  3 in s
print y, z # y = True, z = False


hundreds_of_other_words = range(0, 100)
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

y = "zip" in stopwords_list # False, but have to check every element

stopwords_set = set(stopwords_list)
z = "zip" in stopwords_set

print y, z

## find a distinct value in the collection
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)	# 6, has repeated value
item_set = set(item_list)
num_distinct_items = len(item_set) # 3,
distinct_item_list = list(item_set) #[1, 2, 3]
print item_set, item_list, distinct_item_list

