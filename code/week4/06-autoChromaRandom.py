## example based on Auto Chroma Key example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import vidpy module
from vidpy import Clip, Composition
# import random module
import random

# video location in hard drive
video = "videos/video5.mp4"

# empty list of clips
clips = []

# variable for introducing randomness
delta = 5

# variable for number of copies
numberCopies = 100

for i in range(0, numberCopies):
    clip = Clip(video)

    # attempt to automatically remove background color
    # you can also specify a color with color='#00ff00'
    clip.chroma(amount=0.2, color="#000000")

    # start the clips 1/2 second after last clip
    clip.set_offset(i * 0.5)

    # change the clips x coordinate
    clip.position(x=(i*10*random.random())-30)

    # loop the clip 3 times
    clip.repeat(3)

    clips.append(clip)

# composition made out of clips
# bgcolor picks background color
# duration picks duration of video
comp = Composition(clips, bgcolor='#ff4dff', duration=10.0)
comp.save('chromaRandom.mp4')
