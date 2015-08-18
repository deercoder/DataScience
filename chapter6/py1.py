#!/usr/bin/env python
import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girl = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girl += 1
    if older == "girl" or younger == "girl":
        either_girl += 1


print both_girl, older_girl, either_girl
# fix a bug in the book, that has to be float point
print "P(both|older):", both_girl * 1.0 / older_girl  # the probability of both are girls under the condition that older is girl
print "P(both|either):", both_girl * 1.0 / either_girl # the probability of both are girls under the condition that either is girl
