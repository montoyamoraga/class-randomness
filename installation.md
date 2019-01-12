# Installation

This document details the installation of software required for the class [Randomness is all around us](https://github.com/montoyamoraga/class-randomness-is-all-around) by [Aarón Montoya-Moraga](http://montoyamoraga.io/).

## ChucK

ChucK is a programming language for real-time sound synthesis and music creation. It is open-source and freely available on MacOS X, Windows, and Linux. ChucK presents a unique time-based, concurrent programming model that's precise and expressive (we call this strongly-timed), dynamic control rates, and the ability to add and modify code on-the-fly. In addition, ChucK supports MIDI, OpenSoundControl, HID device, and multi-channel audio. It's fun and easy to learn, and offers composers, researchers, and performers a powerful programming tool for building and experimenting with complex audio synthesis/analysis programs, and real-time interactive music. (Source: [chuck.cs.princeton.edu/](http://chuck.cs.princeton.edu/)).

* Go to [chuck.cs.princeton.edu/](http://chuck.cs.princeton.edu/).
* Go to [download ChucK](http://chuck.cs.princeton.edu/release/).
* Download the correct installer for your operating system, either Linux, Mac or Windows.
* Follow the instructions of the installer.
* The name of the application installed is *miniAudicle*.

## Processing

Processing is a flexible software sketchbook and a language for learning how to code within the context of the visual arts. Since 2001, Processing has promoted software literacy within the visual arts and visual literacy within technology. There are tens of thousands of students, artists, designers, researchers, and hobbyists who use Processing for learning and prototyping. (Source: [processing.org](https://processing.org/)).

* Go to [processing.org/](https://processing.org/).
* Go to the [Download section](https://processing.org/download/).
* Download the correct installer for your operating system, either Linux, Mac or Windows.
* Follow the instructions of the installer.
* The name of the application installed is *Processing*.

## Pure Data

Pure Data (or just Pd) is an open source visual programming language for multimedia. Its main distribution (aka Pd Vanilla) is developed by Miller Puckette. (Source: [puredata.info/](http://puredata.info/)).

* Go to [puredata.info/](http://puredata.info/).
* Go to [Downloads](http://puredata.info/downloads).
* Go to [http://puredata.info/downloads/pure-data](http://puredata.info/downloads).
* Download the correct installer for your operating system, either Linux, Mac or Windows.
* Follow the instructions of the installer.
* The name of the application installed is *Pd-0.49-1*.

## Python 3

Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. (Source: [Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))).

Python 2.0 was released on 2000 and Python 3.0 was released on 2008. Python 3.0 was was a major revision of the language that is not completely backward-compatible, and for this class we will use Python 3.

We will now install Python 3 and make it available to use from our [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface).

### Python 3 installation for Linux

Go to [python.org/](https://www.python.org/) and download the latest Python 3 release from [Python source releases section](https://www.python.org/downloads/source/).

Another option I recommend is installing the [Anaconda Python distribution](https://www.anaconda.com/).

### Python 3 installation for Mac

Mac computers come with Python 2 already installed. Open the Terminal app on your Mac and execute the following command.

```bash
python
```

You should see this on your terminal

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python2-example.png "Python2 example")

To exit the Python 2 environment and go back to Terminal. enter the following command.

```python
exit()
```

To check if you already have installed Python 3 in your computer, try running the following command.

```bash
python3
```

If you see the following screen, you already have Python 3 installed and you are done, yay.

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python3-example.png "Python3 example")

If not, continue with these instructions to install Python3.

I recommend installing first the package manager [homebrew](https://brew.sh), which will be helpful for other tools we will use later in the class.

After installing homebrew, install Python3 using the following command.

```bash
brew install python3
```

After installing it, you can now open the Terminal application and run Python 3 with the command.

```python
python3
```

You should now see this on your computer. If not, try restarting the computer and trying again.

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python3-example.png "Python3 example")

### Python 3 installation for Windows

Windows usually doesn't have Python installed. We will install Python 3 and use it with our [command-line interface](https://en.wikipedia.org/wiki/Command-line_interface).

Depending on your Windows version, you may have different softwares for  command-line interface, including [Command prompt](https://en.wikipedia.org/wiki/Cmd.exe) and [PowerShell](https://en.wikipedia.org/wiki/PowerShell). If you have both, I recommend using PowerShell over Command prompt, but both are fine.

During this class I will refer to commands with UNIX syntax that work in both Mac and Linux, but have a different syntax in Windows. You can optionally install [Gow](https://github.com/bmatzelle/gow/releases), in order to be able to use UNIX syntax on Windows.

To check if you have Python installed, open your command prompt and execute the command.

```bash
python
```

If you see this, yay, you have Python 3 installed and you will be using the command *python* during this class.

TODO

If you see this screen, that means that the command *python* is tied to Python 2, so let's check if you have Python 3 installed by executing the following command.

```bash
python3
```

If you see this, yay, you have Python 3 installed and you will be using the command *python3* during this class.

TODO

If you see this screen, you don't have Python3 installed yet, so let's continue with the installation.

TODO

Go to [python.org/](https://www.python.org/) and continue to the [Python Releses for Windows](https://www.python.org/downloads/windows/) section available in the Downloads Menu.

Download the installer for the latest Python 3 release, which would be 3.7.2 as of today, January 12th 2019.

When you are going through the installation, make sure to select the option "Add Python 3 to PATH", in order to make Python 3 available to execute from the Command prompt.

![alt text](https://github.com/montoyamoraga/class-randomness-is-all-around/raw/master/pics/week1-python-windows.png "Python Windows")

After installing I suggest restarting your Windows computer and checking if Python is accessible from the command prompt, either with the command *python* or *python3*.

Here are some additional [instructions for Windows](https://wsvincent.com/install-python3-windows/).

If you are running into trouble, contact the instructor of this class.
