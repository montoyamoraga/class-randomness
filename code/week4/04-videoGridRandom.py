## example based on Video Grid example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import vidpy module
from vidpy import Clip, Composition
# import random module
import random

# video location in hard drive
video = 'videos/video4.mp4'

# canvas width and height
# this matches the dimensions of the original clip
canvasWidth = 1280
canvasHeight = 720

# number of videos in x axis
horizontalVideos = 3
# width of each video
vidWidth = canvasWidth / horizontalVideos
# height of each video
vidHeight = (vidWidth/canvasWidth) * canvasHeight

# start position
x = 0
y = 0

# variable for introducing randomness
delta = 5

# empty list of clips
clips = []

# while y is inside of canvas
while y < canvasHeight:

    # create a clip
    clip = Clip(video)

    # set clip position
    # add random offsets to each variable
    randomX = x + random.uniform(-delta, delta)
    randomY = y + random.uniform(-delta, delta)
    randomWidth = vidWidth + random.uniform(-delta, delta)
    randomHeight = vidHeight + random.uniform(-delta, delta)
    clip.position(x=randomX, y=randomY, w=randomWidth, h=randomHeight)

    # fade in for 0.1 second
    clip.fadein(0.1)

     # repeat the clip three times
    clip.repeat(3)

    # start the clip based on existing clips
    # add a random offset
    clip.set_offset(len(clips)*random.random())

    # add clip to list of clips
    clips.append(clip)

    # increment the x and y position
    x += vidWidth
    # if x is outside of canvas
    if x > canvasWidth:
        # update y
        y += vidHeight
        # reset x
        x = 0


grid = Composition(clips, width=canvasWidth, height=canvasHeight)
# save to hard disk
grid.save('gridRandom.mp4')
