## example based on Filter Gallery example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import modules
from vidpy import Composition, Clip
import random

# retrieve video
vid = 'videos/video5.mp4'

# python dictionary
filters = {
    'brightness': [.8],
    'contrast': [.9],
    'opacity': [.1],
    'hue': [.8],
    'saturate': [.9],
    'grayscale': [],
    'threshold': [],
    'dynamic_threshold': [],
    'invert': [],
    'extract_color': [],
    'glow': [],
    'softglow': [],
}

# empty list of clips
clips = []

# number of videos to be stitched
videos = 10

# iterate through every video
for video in range(videos):
    # create a clip one second long
    clip = Clip(vid, start=0, end=random.random()*10)

    # mute it
    clip.volume(0)

    # pick random key from the dictionary
    f = random.choice(list(filters.keys()))

    # retrieve the arguments from the dictionary
    args = filters[f]

    if len(args) > 0:
        getattr(clip, f)(*args)
    else:
        getattr(clip, f)()

    # add the text of the filter
    # clip.text(f, olcolor='#000000', outline=10)

    # append clip to the clips list
    clips.append(clip)

# make composition
comp = Composition(clips, singletrack=True)

# save file to hard drive
comp.save('filtersRandom.mp4')
