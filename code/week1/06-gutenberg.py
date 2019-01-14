# 06-gutenberg.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-14

# script that downloads a random book from the Gutenberg projet

# import Python modules
# we will use requests, install with
# pip install requests
# requests module documentation
# http://docs.python-requests.org/en/master/
import requests
# import random module
import random

# sample request, where XXXX is a number between 0-9999
# http://www.gutenberg.org/cache/epub/XXXX/pgXXXX.txt

# variable for request
randomNumber = random.randint(0,9999)

# build gutenberg project request with the variables
gutenbergRequest = "http://www.gutenberg.org/cache/epub/" + str(randomNumber) + "/pg" + str(randomNumber) + ".txt"

# make the request and store result in response
response = requests.get(gutenbergRequest)

# parse the response to string
text = response.text

# print book to console
print(text)
