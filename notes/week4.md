# class-randomness-is-all-around

## Week 4:  Introduction to randomness for video with Python

This week we will manipulate video material with software tools and randomness concepts, and we will review some concepts regarding human vision and digital animation.

### Frame rate

[Frame rate](https://en.wikipedia.org/wiki/Frame_rate) is the rate (frequency) at which consecutive frames (images) appear on a display. Frame rate is measured in frames per second (fps).

Human vision has a temporal sensitivity and resolution which varies depending on the type and characteristics of visual stimulus.

10-12 fps are perceived individually, and higher frame rates are perceived as motion.

Computer displays with a frame rate higher than 50 fps are perceived as stable. This is called the [flicker fusion threshold](https://en.wikipedia.org/wiki/Flicker_fusion_threshold).

People have been found to recognize a specific image in an unbroken series of different images, each of which lasts as little as 13 milliseconds.

Multiple stimuli that are very short are sometimes perceived as a single stimulus: a 10 ms green flash of light followed by a 10 ms red flash of light can be perceived as a single yellow flash of light.

### Silent films

Early silent films had frame rates between 16-24 fps but since the cameras were hand-cranked, the rate often changed during the scene to fit the mood. These frame rates were enough for the sense of motion, but it was perceived as jerky motion.

To minimize the perceived flicker, projectors employed dual- and triple-blade shutters, so each frame was displayed two or three times, increasing the flicker rate to 48 - 72 fps and reducing eye strain.

Thomas Edison said that 46 frames per second was the minimum needed for the eye to perceive motion. In the 1920s, the frame rate for silent films increased to 20-26 fps.

### Sound films

When sound film was introduced in 1926, variations in film speed were no longer tolerated, as the human ear is more sensitive to changes in audio frequency. 24 fps was chosen as the standard for 35mm sound film.

Two-blade shutters thus achieve 48 fps and three-blade shutters achieve 72 fps, both satisfying Edison's suggestion.

### Modern video standards

Due to the mains frequency of electric grids, analog television broadcast was developed with frame rates of 50 Hz (most of the world) or 60 Hz (US, Japan, South Korea). Circuits were developed for television cameras to lock onto the mains frequency as their primary reference.

The introduction of color TV technology made it necessary to lower that 60 fps frequency to avoid [dot crawl](https://en.wikipedia.org/wiki/Dot_crawl), an annoying display artifact appearing on legacy black-and-white displays, showing up on highly-color-saturated surfaces. It was found that by lowering the frame rate by .1%, that undesirable effect was highly minimized.

Today's North America, Japan, and South Korea's video transmission standards are still based on 60÷1.001 or ≈59.94 images per second. Confusingly, [interlaced](https://en.wikipedia.org/wiki/Interlaced_video) formats are customarily stated at 1/2 their image rate, 29.97 fps, and double their image height, but these statements are purely custom; in each format, 59.94 images per second are produced.

This confusion was industry-wide in the early days of digital video software, with much software being written incorrectly -- the coders believing that only 29.97 images were expected each second, which was incorrect. While it was true that each picture element was polled and sent only 29.97 times per second, the pixel location immediately below that one was polled 1/60th of a second later -- part of a completely separate image for the next 1/60 second frame.

Further reading: Facebook/Oculus created a new unit of time called flicker: [article](https://techcrunch.com/2018/01/22/facebook-invented-a-new-time-unit-called-the-flick-and-its-truly-amazing/), [GitHub](https://github.com/OculusVR/Flicks)

### Video file formats

A [video file format](https://en.wikipedia.org/wiki/Video_file_format) is  is a type of file format for storing digital video data on a digital system. Video is almost always stored using lossy compression to reduce the file size.

We will be using for today's class [webm](https://en.wikipedia.org/wiki/WebM), [mp4](https://en.wikipedia.org/wiki/MPEG-4_Part_14), [mov](https://en.wikipedia.org/wiki/QuickTime_File_Format), among others.

For playback of the videos we will use today, I suggest downloading the tool [VLC](https://www.videolan.org/vlc/index.html), a free and open source cross-platform multimedia player.

### youtube-dl command-line tool

youtube-dl is a cool tool that can be used for downloading videos from the internet, by specifying URLs. It can download not only from Youtube, but also Vimeo and [a ton of other sites](https://rg3.github.io/youtube-dl/supportedsites.html).

To check the documentation of youtube-dl execute the following command.

```bash
youtube-dl --help
```

To download a YouTube video use the URL as argument.

```bash
youtube-dl [URL]
```

If you want to check the available formats and resolutions, use the *-F* flag.

```bash
youtube-dl [URL] -F
```

You can use the *-f* flag and the code for that format to download it.

```bash
youtube-dl [URL] -f 4
```

To decide the output filename use the *-o* flag.

```bash
youtube-dl [URL] -o [FILENAME]
```

Let's download three videos from YouTube:

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

### Introduction to [VidPy](https://antiboredom.github.io/vidpy/)

VidPy is a Python module created by [Sam Lavigne](http://lav.io/), based on the [MLT Multimedia Framework](https://www.mltframework.org/), and draws heavily from [MoviePy](https://github.com/Zulko/moviepy) by [Zulko](https://github.com/Zulko).
