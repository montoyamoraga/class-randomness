# 04-random-org.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-13

# script that outputs one random integer from random.org

# import Python modules
# we will use requests, install with
# pip install requests
# requests module documentation
# http://docs.python-requests.org/en/master/
import requests

# example to request integers where
# num is quantity of integers
# min is minimum value
# max is maximum value
# col is how many per column
# base means numbers base 10
# format is plain instead of html
# https://www.random.org/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new

# variables for request
num = 1
min = 1
max = 6

# build random.org request with the variables
randomOrgRequest = "https://www.random.org/integers/?num=" + str(num) + "&min=" + str(min) + "&max=" + str(max) + "&col=1&base=10&format=plain&rnd=new"

# make the request and store result in response
response = requests.get(randomOrgRequest)

# parse the response to string and then to int
randomNumber = int(response.text)

# print random number to console
print(randomNumber)

# print if random number is even or odd
if randomNumber % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")
