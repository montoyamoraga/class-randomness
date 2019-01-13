# class-randomness-is-all-around

## About

*Randomness is all around* is a class by [Aarón Montoya-Moraga](http://montoyamoraga.io/).

*Randomness is all around* was taught at [School of Ma](http://schoolofma.org/), in an online non-presential way, over 4 weeks, one three-hour class every week, between Monday January 14th 2019 and Monday February 4th 2019.

## Contents

* [About](#about)
* [Code of conduct](#code-of-conduct)
* [Materials for the class](#materials-for-the-class)
* [Methodology](#methodology)
* [Installation](#installation)
* [Summary](#summary)
* [Week 1: Numbers with Python](#week-1)
* [Week 2: Audio with Pure Data](#week-2)
* [Week 3: Image with p5.js](#week-3)
* [Week 4: Video with VidPy](#week-4)
* [Additional resources](#additional-resources)
* [License](#license)

### Code of conduct

This class is part of School of Ma, and will be ruled by their code of conduct.

## Summary

Randomness is all around us and is what drives natural events such as the weather and dice-throwing. Randomness is behind noise, and noise is present in every sensor measurement, including our audiovisual perception of the world. Randomness is what makes vinyls sound different than digital audio and film look different than digital video. Randomness is the lack of pattern and or predictability in patterns.

Computers allows us to create mathematical models of randomness and incorporate to our art practice, rendering new exciting new generative and unpredictable artworks, like it has been done in genres such as [aleatoric music](https://en.wikipedia.org/wiki/Aleatoric_music) and [automatic drawing](https://en.wikipedia.org/wiki/Surrealist_automatism#Automatic_drawing), and by artists like [Lillian Schwartz](https://en.wikipedia.org/wiki/Lillian_Schwartz), [Max Hawkins](https://maxhawkins.me/) and [John Cage](https://en.wikipedia.org/wiki/John_Cage), and featured by institutions such as the [Random Institute](https://en.wikipedia.org/wiki/Random_Institute).

We will cover math for randomness and probabilities, programming with scripts, programming audio synthesis and manipulation, computer graphics, video manipulation, and web concepts.

Applicants from diverse backgrounds, with varied skillsets and interests are welcome.

Don't feel discouraged if you know nothing about any of these topics, if you can use a computer you will be able to follow and learn in every class.

If you are an expert in any of these topics, you will learn how to incorporate other disciplines to your practice.

## Methodology  

Each class includes explanations of theory and concepts, and practical examples with software.

Students are encouraged to ask questions and branch out from the proposed timeline for class.

All the notes and code written is included on this GitHub repository, so that students can focus on following along the coding examples and not worry about taking notes or missing out.

There are also several links for further reading and studying.

All the contents of this repository will be updated during the duration of this class.

## Materials for the class

The materials needed include:

* A computer running either Linux, MacOS, or Windows. (No tablets)
* Internet connection
* Headphones

We will use free libre open source software, including:

* [Audacity](https://www.audacityteam.org/), for editing audio.
* [ChucK](http://chuck.cs.princeton.edu/), software for computer music.
* [Command line interface](https://en.wikipedia.org/wiki/Command-line_interface), environment for executing code.
* [p5.js](https://p5js.org/), for interactive audiovisual web apps.
* [Processing](https://processing.org/), for programming interactive audiovisual apps.
* [Python3](https://www.python.org/), for math.
* [Pure Data](http://puredata.info/), for audio and sound manipulation.
* [Text editor](https://en.wikipedia.org/wiki/Text_editor), for writing code. I recommend [Atom](https://atom.io/) or [Sublime Text](https://www.sublimetext.com/).
* [VidPy](https://antiboredom.github.io/vidpy/), for video manipulation.

## Installation

Refer to the [installation.md](/installation.md) file to install the required free libre open source software we will use in this class.

All the material of this class is free, libre, open-source, and available on the web on a GitHub repository.

Iis highly encouraged to use GitHub to share the work you do and the notes you take for this class. If you are not sure what GitHub is, here are some links:

* [What is Git](TOOD)
* [What is GITHUB](TODO)
* [What is FLOSS](TODO)

I would love it if everyone would upload the code they write using GitHub to share it with all classmates but it is not mandatory, it is totally OK to not do it.

Maybe for real-time collaboration, we should set up a Google Doc so you call can take notes and share them?

## Week 1: Introduction to randomness and programming with Python

### Topics

* Randomness
* Randomness and computers
* Gaussian and uniform distributions
* Poisson and Markov chains
* Normalization of signals
* Python for math and randomness
* Randomness on the internet: random.org

### Week 1 notes

Today we will a text editor to write code using the language Python 3, and will execute our scripts using the command-line interface.

Before continuing, make sure to follow the instructions at [Python 3 installation](/installation.md/#python-3), on the companion file [installation.md](/installation.md).

Optionally, follow the instructions for setting up a [virtual environment](/virtual-environment.md). It is not neccessary but highly encouraged.

In my computer, a Macbook running macOS, *python* is for Python 2 and *python3* is for Python 3, so I will be using the latter throughout this text. Use the corresponding one for your setup.

Let's start writing Python code.

We will encourage good manners and good practices in programming, such as using comments to explain and document the code we are writing.

In programming languages, we can write comments: lines of code that are skipped by the computer and are only intended for human reading. They are useful for documentation and for explaining what each block of code does. In Python, if you type a "#" at the beginning of the line, it becomes a comment. Comments are also useful to skip lines of code that are buggy or we are testing, and instead of deleting we can keep them for future reference.

Write the following script:

```python
# 00-testing.py
# written by X
# runs with Python3
# date: yyymmdd

# print message on console
print("testing")
```

To run this code, execute it on the command-line with the python command:

```python
python3 00-testing.py
```

You should see the following on the command line:

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-00-testing.png "Testing script")

Now we will use the random functions of Python. We don't need to install them, but we do need to import them. We will use it to output a random number.

```python
# 01-random-number.py
# written by montoyamoraga
# runs with Python3
# date: 2019-01-11

# script that outputs a random number

# import Python modules
# random module documentation
# https://docs.python.org/3.7/library/random.html
import random

# use random module to get a random number
# use the random() function of the random module
# random() returns the next random floating point number in the range [0.0, 1.0).
number = random.random()

# print number on the command-line
print(number)
```

Let's now create several random numbers, and introduce the concept of seed.

For more info:
* [Pseudorandomness, Wikipedia](https://en.wikipedia.org/wiki/Pseudorandomness)
* [How computers generate random numbers, How-To Geek](https://www.howtogeek.com/183051/htg-explains-how-computers-generate-random-numbers/)
* [Introducion to randomness and random numbers, random.org](https://www.random.org/randomness/)

```python
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
```

This example was easy to expand, since we went from one variable to three of them, but it is a bad practice to copy and paste code. Also there are data structures that allow us to store related data in an easy way. In programming we call them [arrays](https://en.wikipedia.org/wiki/Array_data_structure), and in Python we call them [lists](https://docs.python.org/3.7/tutorial/datastructures.html).

Let's write a Python code that creates one thousand random numbers at a time.

```python
# 03-thousand-random-numbers.py
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
for i in range(quantity):
    # declare variable for new random number
    # random() returns the next random floating point number in the range [0.0, 1.0)
    newNumber = random.random()
    # append new number to the list
    numbers.append(newNumber)

# print list of numbers
print(numbers)
```

Bad news is that computers can't generate true random numbers on their own. Computer algorithms are only able to create pseudorandom numbers, which appear to be random but are not.

If we want to generate true random numbers, we need to access data from outside of our computer, such as the one at [random.org](https://www.random.org/).

Let's use random.org to get true random integer numbers.

```python
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
```

In this last example, we used an if statement, which allows our code to behave differently in every execution.

Let's expand this to include text, with the Python module [Tracery for Python](https://github.com/aparrish/pytracery) by [Allison Parrish](http://www.decontextualize.com/), a Python port of the original [Tracery](http://tracery.io/) by [Kate Compton](http://www.galaxykate.com/).




## Week 1 assignment

Write a Python script that outputs random numbers in a creative way. Write a blog post about the way your Python script works, include your inspiration, your successes, your shortcomings, and failures. Include also your research links, and bibliography, and any doubts you have about randomness, Python, or anything we have seen so far.

## Week 2: Introduction to randomness and sound art

Topics:
* Sound art and computer music
* Human sound perception
* Pure Data environment
* Oscillators
* White and pink noise
* Sequencers
* Sampling

Assignment:

Create a sound art piece that uses randomness.

## Week 3: Introduction to randomness and computer graphics

Topics:
* Human color perception
* Introduction to p5.js
* Drawing basic shapes
* RGB / HSB color models
* White and pink noise
* Perlin noise
* Interactivity with mouse and keyboard

Assignment:

Create a visual art piece that uses randomness.

## Week 4: Introduction to randomness and video manipulation

Topics:
* Human vision temporal sensitivity
* Introduction to VidPy
* Video format conversion
* Frame rate manipulation
* Stitching videos programmatically

Assignment:

Create a video art piece that uses randomness.

## Additional resources

* [Learn enough command line to be dangerous](https://www.learnenough.com/command-line-tutorial)
* [Python for beginners](https://www.pythonforbeginners.com/)
* [FLOSS Manuals: Pure Data](http://write.flossmanuals.net/pure-data/)
* [p5js reference](https://p5js.org/reference/)
* [p5.js tutorials](https://p5js.org/learn/)
* [p5.js editor](https://editor.p5js.org/)

## License

MIT
