# 04-random-org.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-13

# script that outputs one thousand random numbers with an optional seed

# import Python modules
# random module documentation
# https://docs.python.org/3.7/library/random.html
import random

# use boolean variable to decide the use of seed
# useSeed = True
useSeed = False

# if useSeed is True, set a random seed
if (useSeed):
    # set random seed
    # random.seed() initializes the random number generator.
    # https://en.wikipedia.org/wiki/Random_seed
    random.seed(11)

# declare variable to specify how many random numbers
quantity = 1000

# declare empty list for the numbers
numbers = list()

# iterate to fill the empty list
# check documentation of range() in Python
for i in range(quantity):
    # declare variable for new random number
    # random() returns the next random floating point number in the range [0.0, 1.0)
    newNumber = random.random()
    # append new number to the list
    numbers.append(newNumber)

# print list of numbers
print(numbers)
