## example based on Camera example from VidPy website
## https://antiboredom.github.io/vidpy/examples.html

# import python module
from vidpy import Composition, Camera

# camera setup
clip = Camera(width=1280, height=720, start=0, end=5)

# spin effect
clip.spin(2)

# save to hard drive
Composition([clip]).save('camera.mp4')
