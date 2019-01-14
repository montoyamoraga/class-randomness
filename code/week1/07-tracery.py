# 07-tracery.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-13

# script that outputs one thousand random numbers with an optional seed

# import Python modules
# we will use tracery, install with
# pip install tracery
# tracery documentation
# https://github.com/aparrish/pytracery
import tracery
# import english language stuff
from tracery.modifiers import base_english
# import random module
import random

# define tracery rules
rules = {
    "origin": "#hello.capitalize#, #when# #number# #color# #stuff#.",
    "hello": ["hello", "hi", "hey"],
    "when": ["yesterday", "today", "tomorrow"],
    "number": [str(random.randint(2, 100)), str(random.randint(2,4)) + " fifths"],
    "color": ["purple", "yellow", "green", "transparent"],
    "stuff": ["degrees", "suns", "clouds", "lamps"]
}

# create new tracery grammar with our rules
grammar = tracery.Grammar(rules)

# add modifiers to our grammar
grammar.add_modifiers(base_english)

# print result
print(grammar.flatten("#origin#"))
