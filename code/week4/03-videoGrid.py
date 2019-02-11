## example based on Video Grid example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html
from vidpy import Clip, Composition

# video location in hard drive
video = 'videos/video5.mp4'

# canvas width and height
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

# empty list of clips
clips = []

# while y is inside of canvas
while y < canvasHeight:

    # create a clip
    clip = Clip(video)

    # set clip position
    clip.position(x=x, y=y, w=vidWidth, h=vidHeight)

    # fade in for 1/2 second
    clip.fadein(0.5)

     # repeat the clip three times
    clip.repeat(3)

    # start the clip based on existing clips
    # add an offset of 10%
    clip.set_offset(len(clips)*0.10)

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
grid.save('grid.mp4')
