# VidPy testing

This tutorial is for week 4. Let me know if you have any trouble installing the software and running this example.

Fo week 4 we will use:
* [VidPy](https://antiboredom.github.io/vidpy/) Python module *(MANDATORY)*
* [ffmpeg](https://www.ffmpeg.org/) command-line tool *(OPTIONAL)*
* [youtube-dl](https://rg3.github.io/youtube-dl/) command-line tool *(OPTIONAL)*

## Installation and testing for Linux

### VidPy

If you want to follow the instructions from the VidPy official website, click here: [https://antiboredom.github.io/vidpy/installation.html#ubuntu-debian](https://antiboredom.github.io/vidpy/installation.html#ubuntu-debian).

To install VidPy, you will need to first install [melt](https://www.mltframework.org/docs/melt/):

```bash
sudo apt-get install melt
```

After installing melt, you can install VidPy with pip. Optionally you can first create a [virtual environment](virtual-environment.md) and install VidPy on it. Here are the instructions for creating a virtual environment for Python3, activating it and then installing vidpy on it.

```bash
python3 -m venv env
```

```
source env/bin/activate
```

```bash
pip3 install vidpy
```

### ffmpeg

To install ffmpeg on Linux, follow the instructions of their website: [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html).

### youtube-dl

To install youtube-dl on Linux, follow the instructions of their website: [https://rg3.github.io/youtube-dl/download.html](https://rg3.github.io/youtube-dl/download.html).

---

## Installation and testing for Mac

### VidPy

If you want to follow the instructions from the VidPy official website, click here: [https://antiboredom.github.io/vidpy/installation.html#mac-windows](https://antiboredom.github.io/vidpy/installation.html#mac-windows).

To install VidPy, you will need to first install [Shotcut](https://www.shotcut.org/). You can either install it from their [website](https://www.shotcut.org/download/) or with homebrew:

```bash
brew cask install shotcut
```

After installing ShotCut, you can install VidPy with pip. Optionally you can first create a [virtual environment](virtual-environment.md) and install VidPy on it. Here are the instructions for creating a virtual environment for Python3, activating it and then installing vidpy on it.

```bash
python3 -m venv env
```

```
source env/bin/activate
```

```bash
pip3 install vidpy
```

### youtube-dl

You can install youtube-dl with homebrew,, using the terminal command:

```bash
brew install youtube-dl
```

You can also install it

### ffmpeg

You can install ffmpeg with homebrew, using the terminal command:

```bash
brew install ffmpeg
```

---

## Installation and testing for Windows

### VidPy

If you want to follow the instructions from the VidPy official website, click here: [https://antiboredom.github.io/vidpy/installation.html#mac-windows](https://antiboredom.github.io/vidpy/installation.html#mac-windows).

To install VidPy, you will need to first install [Shotcut](https://www.shotcut.org/). You can install it from their [website](https://www.shotcut.org/download/).


After installing ShotCut, you can install VidPy with pip. Optionally you can first create a [virtual environment](virtual-environment.md) and install VidPy on it. Here are the instructions for creating a virtual environment for Python3, activating it and then installing vidpy on it.

```bash
python3 -m venv env
```

```
source env/bin/activate
```

```bash
pip3 install vidpy
```

### ffmpeg

To install ffmpeg on Windows, follow the instructions of their website: [https://www.ffmpeg.org/download.html](https://www.ffmpeg.org/download.html).

### youtube-dl

To install youtube-dl on Windows, follow the instructions of their website: [https://rg3.github.io/youtube-dl/download.html](https://rg3.github.io/youtube-dl/download.html).
