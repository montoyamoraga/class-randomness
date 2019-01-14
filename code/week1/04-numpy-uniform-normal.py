# 04-numpy-uniform-normal.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-14

# script that plots an uniform or normal distribution

# import random, numppy and matplotlib.pyplot python modules
import random
import numpy
import matplotlib.pyplot

# list for storing distribution
randomDistribution = list()
# list for storing time
randomTime = list()

# number of samples
quantity = 1000

# iterate through every sample
for i in range(quantity):

    # either create new value from uniform distribution
    # where random.uniform(a, b)
    newNumber = random.uniform(-1, 1)

    # or create new value from normal distribution
    # where random.gauss(mu, sigma)
    # newNumber = random.gauss(0, 1)

    # append new number to the list
    randomDistribution.append(newNumber)
    # append sample number to time
    randomTime.append(i)

# convert lists generated with random to numpy arrays
numpyDistribution = numpy.array(randomDistribution)
numpyTime = numpy.array(randomTime)

# generate plot with matplotlib
matplotlib.pyplot.plot(numpyTime, numpyDistribution, 'bo')

# show the window with the plot
matplotlib.pyplot.show()
