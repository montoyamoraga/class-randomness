## example based on stitch Videos example from VidPy website
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

# maximum length is sixty seconds
# try also 10 seconds, 1 second, 0.1 second
remainingTime = 60

# iterate through each clip
for clip in range(len(clips)):
    # select a random start
    randomStart = random() * clips[clip].duration
    # select a random duration
    randomDuration = random() * remainingTime
    # if the duration is possible
    if randomStart + randomDuration < clips[clip].duration:
        # calculate randomEnd
        randomEnd = randomStart + randomDuration
    # if the duration is not posible
    else:
        # randomEnd is the original duration of clip
        randomEnd = clips[clip].duration

    # update remainingTime
    remainingTime = remainingTime  - (randomEnd - randomStart)

    # cut at the desired position
    clips[clip].cut(start=randomStart, end=randomEnd)

# stitch all the cuts together
stiched = Composition(clips, singletrack=True)
stiched.save('randomMinute.mp4')
