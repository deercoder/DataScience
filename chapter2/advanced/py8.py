#!/usr/bin/env python
# enumerate
# not pythonic
for i range(len(documents)):
	document = document[i]
	do_something(i, document)

# also not pythonic
i = 0
for document in documents:
	do_something(i, document)
	i += 1

# enumerate the document
for i, document in enumerate(documents):
	do_something(i, document)

# not pythonic
for i in range(len(documents)):
	do_something(i)

# pythonic
for i, _ in enumerate(documents):
	do_something(i)
