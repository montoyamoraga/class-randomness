# Virtual environment

This document details the setup of virtual environments using Python3, which is heavily encouraged for the class [Randomness is all around us](https://github.com/montoyamoraga/class-randomness-is-all-around) by [Aarón Montoya-Moraga](http://montoyamoraga.io/).

This document is intended to be used on a machine with Python 3 installed.

Python can do math, but sometimes we will include Python modules, which are snippets of code that other people wrote and that we can use. We can install them on our hard drive, but it is a lot of clutter and also it's easy to break things when all your Python scripts share their dependencies.

Virtual environments are containers for each project we write, where we can install our modules and make them only available for one particular Python project, and invisible to the rest of them. Virtual environments allow us to use Python modules without having to instal them globally, and also makes the deinstallation process smooth, since virtual environments are folders in our computers we can easily delete.

Virtual environments avoid conflicts and errors between differen Python projects, yay.

## Setup

Let's setup our virtual environment yay.

Let's open the terminal and navigate to a folder, in this case Desktop.

```bash
cd Desktop
```

Execute the command *ls* to see the contents of the desktop folder.

```bash
ls
```

To create a virtual environment with python3 on this folder, execute the following command.

```bash
python3 -m venv env
```

If this command is successful, it will create a new folder *env/* in your desktop.

In order to use the virtual environment folder, you need to activate it with the following command.

```
source env/bin/activate
```

Now You should see *(env)* appear on your command-line.

TODO: insert picture.

Let's install a library. Libraries are scripts, text files with code on them, that we didn't write but we can use to expand the functionalities of plain Python.

We will install in our virtual environment the library [Tracery for Python](https://github.com/aparrish/pytracery) by [Allison Parrish](http://www.decontextualize.com/), a Python port of the original [Tracery](http://tracery.io/) by [Kate Compton](http://www.galaxykate.com/).

To install it we will use pip, the Python package manager that is able to go to the internet and download and install the Python libraries we request. In Python, we call libraries modules.

Let's instal Tracery for Python. making sure our virtual environment is activated, with the following command.

```bash
pip install tracery
```

With the virtual environment still activated, execute the command *python3* to open an interactive Python shell.

```bash
python3
```

After that, try importing tracery

```Python
import tracery
```

Success, yay. Now let's check that Tracery is not installed globally on our machine. First, close the Python shell.

```python
exit()
```

Then let's deactivate the virtual environment, after which you will no longer see the *(env)* in your command-line interface.

```bash
deactivate
```


Let's open the Python shell again with the *python* command.

```bash
python3
```

 Now let's try and fail to import tracery.

```python
import tracery
```

If you see an error message, that means that tracery was successfully installed locally in your virtual environment, and not globally in your machine.
