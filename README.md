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
* [Week 1](#week-1)
* [Week 2](#week-2)
* [Week 3](#week-3)
* [Week 4](#week-4)
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

Refer to the [installation.md](/installation.md) file.

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

Today we will a text editor to write code using the language Python3, and will execute our scripts using the command-line interface.

Let's open our command-line interface and check that we have Python3 installed.

Execute this command

```bash
python
```

This is what I see on my computer.

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python2-example.png "Python2 example")

In my computer, a Macbook running macOS, *python* is an alias for Python2.

If your computer shows Python3, then you are ready to go, and you will execute your code using the command *python*, yay.

To exit, execute the command

```bash
exit()
```

If *python* doesn't correspond to Python3, let's execute now the command python3.

```bash
python3
```

This is what I see on my computer, a Macbook running macOS.

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python3-example.png "Python3 example")

If your computer shows Python3, then you are ready to go, and you will execute your code using the command *python3*, yay.

To exit, type the command

```bash
exit()
```

I managed to install Python3 and made it available using the commmand python3 on my computer by installing [Homebrew](https://brew.sh/) and then installing Python3 by executing the command

```bash
brew install python3
```

If you still haven't been able to use Python3 on your machine, either via the command *python* or *python3*, you need to both install it and then making it available from the terminal.

In Windows, I suggest using the installer from the official [Python website](https://www.python.org/), and making sure that you select the option *Add Python 3.x to the PATH*. After installing I suggest restarting your Windows computer and checking if Python is accessible from the command-line.

Here are some additional [instructions for Windows](https://wsvincent.com/install-python3-windows/).

If you are running into trouble, contact the instructor of this class.

Let's start writing Python code.

Inside of the folder week1, create a file called script.py.

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

To run this code, execute it on the command-line:

```python
python3 00-testing.py
```

You should see the following on the command line:

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-00-testing.png "Testing script")

Now we will use the random functions of Python. We don't need to install them, but we do need to import them. We will use it to output a random number.

Here is the result:

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

Let's now create several random numbers, and introduce the concept of seed. Bad news is that computers can't generate true random numbers on their own. With an algorithm they are only able to create pseudorandom numbers, which appear to be random but are not.

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


Python can do math, but sometimes we will include libraries, which are snippets of code that other people wrote and that we can use. We can install them on our hard drive, but it is a lot of clutter and also it's easy to break things when all your Python scripts share their dependencies. We will use virtual environments instead, so that each project we write, will only use its own libraries, and not the ones that are installed globally in your computer. This is called scope limiting.

Let's setup our virtual environment yay.

Let's open the terminal and navigate to the folder of this class.

```bash
cd Desktop/class-randomness-is-all-around-master/
```

To check that we are in the right folder, list the contents of the terminal.

```bash
ls
```

Let's use week1 and navigate to this folder.

```bash
cd week1/
```

Create a virtual environment on it with Python3

```bash
python3 -m venv env
```

If it is successful, you should see a new folder called env/ inside of the folder week1/.

Now activate the virtual environment by executing the command.

```
source env/bin/activate
```

You should see *(env)* appear on your command-line.

We will the library [Tracery for Python](https://github.com/aparrish/pytracery) by [Allison Parrish](http://www.decontextualize.com/), a Python port of the original [Tracery](http://tracery.io/) by [Kate Compton](http://www.galaxykate.com/).

To install it we will use pip, by executing the following command.

```bash
pip install tracery
```



Pseudo-randomness



## Assignment

Write a Python script that outputs random numbers in a creative way. Write Write a blog post about the way your Python script works, include your inspiration, your successes, your shortcomings and failures, and include your research and doubts about randomness.

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
