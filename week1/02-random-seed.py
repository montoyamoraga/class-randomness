# 02-random-seed.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-11

# script that outputs three random numbers using a seed

# import Python modules
# random module documentation
# https://docs.python.org/3.7/library/random.html
import random

# set random seed
# check what happens when you comment it out
# random.seed() initializes the random number generator.
# https://en.wikipedia.org/wiki/Random_seed
random.seed(11)

# declare three variables
# and assign random numbers to them
# use the random() function of the random module
# random() returns the next random floating point number in the range [0.0, 1.0).
number0 = random.random()
number1 = random.random()
number2 = random.random()

# print numbers on the command-line
print(number0)
print(number1)
print(number2)
