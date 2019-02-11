## example based on Filter Gallery example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import modules
from vidpy import Composition, Clip

vid = 'videos/video5.mp4'

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

clips = []
for f in filters:
    # create a clip one second long
    clip = Clip(vid, start=0, end=1)

    # mute it
    clip.volume(0)

    # retrieve the filters
    args = filters[f]

    if len(args) > 0:
        getattr(clip, f)(*args)
    else:
        getattr(clip, f)()

    # add the text of the filter
    clip.text(f, olcolor='#000000', outline=10)

    # append clip to the clips list
    clips.append(clip)

# make composition
comp = Composition(clips, singletrack=True)

# save file to hard drive
comp.save('filters.mp4')
