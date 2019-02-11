## example based on Stitch Videos example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import vidpy module
from vidpy import Clip, Composition
# import random module
from random import random

# load clips
clip1 = Clip('videos/video1.mp4')
clip2 = Clip('videos/video2.mp4')
clip3 = Clip('videos/video3.mp4')

# list of videos
clips = [clip1, clip2, clip3]

# iterate through each clip
for clip in clips:
    # select a random start
    randomStart = random() * clip.duration
    # select a random end
    randomEnd = randomStart + random() * (clip.duration - randomStart)

    # cut at the desired position
    clip.cut(start=randomStart, end=randomEnd)

# stitch all the cuts together
stiched = Composition(clips, singletrack=True)
stiched.save('randomStitch.mp4')
