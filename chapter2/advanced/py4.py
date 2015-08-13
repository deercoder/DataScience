#!/usr/bin/env python
# Randomness

import random
four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms

# produce the random by seed's value, so if seed is same, then random number is the same
#random.seed(10)
print random.random()
#random.seed(10)
print random.random()

### comment the seed() function above, otherwise always the same

# random range setting
print random.randrange(10)	# from [0,1,...9]
print random.randrange(3, 6)	# from [3, 4, 5], not including 6

# random shuffle
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

# random choose
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print my_best_friend

# choose from without replacing, no duplicate
lottery_number = range(60)
winning_number = random.sample(lottery_number, 6) # choose 6 numbers

## with replacing, has duplicate
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
## genreate [9, 4, 4, 2], can duplicate since it will replace the 4, so next time we can still select it

print four_with_replacement, winning_number
