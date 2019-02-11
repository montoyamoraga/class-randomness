## example based on stitch Videos example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import vidpy module
from vidpy import Clip, Composition

# load clips
clip1 = Clip('videos/video1.mp4')
clip2 = Clip('videos/video2.mp4')
clip3 = Clip('videos/video3.mp4')

# list of videos
clips = [clip1, clip2, clip3]

# stitch all clips together
stiched = Composition(clips, singletrack=True)
stiched.save('allVids.mp4')
