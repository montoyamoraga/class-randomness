# class-randomness-is-all-around

## Week 4:  Introduction to randomness for video with Python

This week we will

### Human vision temporal sensitivity

### Introduction to [VidPy](https://antiboredom.github.io/vidpy/)

VidPy is a Python library by [Sam Lavigne](http://lav.io/).

### Video format conversion

Compressed vs uncompressed

### Frame rate manipulation

30 fps, 10 fps, variable frame rate

### Stitching videos programmatically

### youtube-dl command-line tool

youtube-dl is a cool tool that can be used for downloading videos from the internet, by specifying URLs. It can download not only from Youtube, but also Vimeo and [a ton of other sites](https://rg3.github.io/youtube-dl/supportedsites.html).

To check the documentation of youtube-dl execute the following command.

```bash
youtube-dl --help
```

To download a YouTube video use the URL as argument. Let's download three videos from YouTube:


[The White Stripes - The Hardest Button to Button](https://www.youtube.com/watch?v=K4dx42YzQCE)

```bash
youtube-dl https://www.youtube.com/watch?v=K4dx42YzQCE
```

[Björk - Hunter](https://www.youtube.com/watch?v=DnW77jmr-Xg)

```bash
youtube-dl https://www.youtube.com/watch?v=DnW77jmr-Xg
```

[St. Vincent - Los Ageless](https://www.youtube.com/watch?v=h9TlaYxoOO8)

```bash
youtube-dl https://www.youtube.com/watch?v=h9TlaYxoOO8
```

After executing these commands, you will end up with three videos, maybe in [webm](https://en.wikipedia.org/wiki/WebM) or [mkv](https://en.wikipedia.org/wiki/Matroska) formats.

Let's convert these videos to the [mp4](https://en.wikipedia.org/wiki/MPEG-4_Part_14) format with the ffmpeg command-line tool.

Show ffmpeg and youtube-dl

### ffmpeg command-line tool

ffmpeg is cool for converting from one file format to another one. To achieve it, use the *ffmpeg* command, followed by the *-i* flag, then the original filename and format, and then the desired filename and format

```bash
ffmpeg -i original.format desired.format
```

To convert the videos downloaded to mp4, use the ffmpeg command, followed by the *-i* flag, the original filename and then the desired filename and format.

```bash
ffmpeg -i The\ White\ Stripes-Hardest\ Button\ To\ Button-K4dx42YzQCE.mkv whitestripes.mp4
```

```bash
ffmpeg -i björk\ -\ hunter-DnW77jmr-Xg.webm bjork.mp4
```

```bash
ffmpeg -i St.\ Vincent\ -\ \'Los\ Ageless\'\ \(Official\ Video\)-h9TlaYxoOO8.mkv stvincent.mp4
```

### Lyric videos

Download a poem and make a random lyric video with VidPy
