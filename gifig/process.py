"""
Main entrypoint for gif manipulation.
"""

# Pillow
from PIL import (
    Image,
    ImageSequence,
    ImageDraw,
)


def open_gif(filename):
    gif = Gif(Image.open(filename))
    return gif

class Gif(object):
    def __init__(self, image):
        self.image = image
        self.frames = [frame for frame in
                       ImageSequence.Iterator(self.image)]

    def save(self, path):
        if self.image.mode != 'P':
            self.image = self.image.convert(mode='P')
        self.image.save(path,
            save_all=True, append_images=self.frames)

    def close(self):
        self.image.close()

def draw_black_line(gif):
    for frame in gif.frames:
        draw = ImageDraw.Draw(frame)
        draw.line([(0, 0), frame.size], fill=0, width=5)