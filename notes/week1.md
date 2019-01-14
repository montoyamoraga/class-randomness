# class-randomness-is-all-around

## Week 1: Introduction to randomness for numbers and text with Python

### Randomness

[Randomness, Wikipedia](https://en.wikipedia.org/wiki/Randomness)

[John Cage - Chance, Wikipedia](https://en.wikipedia.org/wiki/John_Cage#Chance)

[Papá o 36 mil juicios de un mismo suceso (2008), film by Leonardo Medel](https://www.imdb.com/title/tt1334552/)



### Randomness and computers

* [Pseudorandomness, Wikipedia](https://en.wikipedia.org/wiki/Pseudorandomness)
* [How computers generate random numbers, How-To Geek](https://www.howtogeek.com/183051/htg-explains-how-computers-generate-random-numbers/)
* [Introducion to randomness and random numbers, random.org](https://www.random.org/randomness/)

### Uniform and normal (Gaussian) distributions

[Uniform distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)):

random.uniform(a, b)

Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.

[Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)

random.gauss(mu, sigma)

Gaussian distribution. mu is the mean, and sigma is the standard deviation.

### Poisson and Markov chains



### Python for math and randomness

Today we will a text editor to write code using the language Python 3, and will execute our scripts using the command-line interface.

Before continuing, make sure to follow the instructions at [Python 3 installation](/installation.md/#python-3), on the companion file [installation.md](/installation.md).

Optionally, follow the instructions for setting up a [virtual environment](/virtual-environment.md). It is not neccessary but highly encouraged.

In my computer, a Macbook running macOS, *python* is for Python 2 and *python3* is for Python 3, so I will be using the latter throughout this text. Use the corresponding one for your setup.

Let's start writing Python code.

We will encourage good manners and good practices in programming, such as using comments to explain and document the code we are writing.

In programming languages, we can write comments: lines of code that are skipped by the computer and are only intended for human reading. They are useful for documentation and for explaining what each block of code does. In Python, if you type a "#" at the beginning of the line, it becomes a comment. Comments are also useful to skip lines of code that are buggy or we are testing, and instead of deleting we can keep them for future reference.

Write the following script: [00-testing.py](./../code/week1/00-testing.py)

To run this code, execute it on the command-line with the *python* command:

```python
python3 00-testing.py
```

You should see the following on the command line:

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-00-testing.png "Testing script")

Now we will use the random functions of Python. We don't need to install them, but we do need to import them. We will use it to output a random number.

[01-random-number.py](./../code/week1/01-random-number.py)

Let's now create several random numbers, and introduce the concept of seed.

[02-random-seed.py](./../code/week1/02-random-seed.py)

This example was easy to expand, since we went from one variable to three of them, but it is a bad practice to copy and paste code. Also there are data structures that allow us to store related data in an easy way. In programming we call them [arrays](https://en.wikipedia.org/wiki/Array_data_structure), and in Python we call them [lists](https://docs.python.org/3.7/tutorial/datastructures.html).

Let's write a Python code that creates one thousand random numbers at a time.

[03-thousand-random-numbers](./../code/week1/03-thousand-random-numbers.py)

### Randomness on the internet: [random.org](https://www.random.org/)

Bad news is that computers can't generate true random numbers on their own. Computer algorithms are only able to create pseudorandom numbers, which appear to be random but are not.

If we want to generate true random numbers, we need to access data from outside of our computer, such as the one at [random.org](https://www.random.org/).

Let's use random.org to get true random integer numbers.

[04-random-org](./../code/week1/04-random-org.py)

In this example, we used an if statement, which allows our code to behave differently in every execution.

### Randomness and text: [Tracery for Python](https://github.com/aparrish/pytracery)

Let's expand this to include text, with the Python module [Tracery for Python](https://github.com/aparrish/pytracery) by [Allison Parrish](http://www.decontextualize.com/), a Python port of the original [Tracery](http://tracery.io/) by [Kate Compton](http://www.galaxykate.com/).

[05-tracery](./../code/week1/05-tracery.py)
