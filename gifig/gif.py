"""
Main entrypoint for gif manipulation.
"""

import numpy as np
from imageio import mimread, mimwrite


class Gif(object):
    """
    @brief      Main object for opening a gif and modifying it.
                Starting off relatively stupid by reading all the data
                at once.
    """
    FORMAT = 'GIF'

    def __init__(self, path):
        self.path = path
        self.frames = [
            Frame(data, self, index)
            for index, data in enumerate(mimread(self.path, format=Gif.FORMAT))
        ]

    def save(self, path=None, **kwargs):
        """
        @brief      Saves the current cache of frames to `path`.
        @param      path  The path to save. If None, defaults to `self.path`.
        @return     The written path.
        """
        path = self.path if path is None else path
        frame_data = (frame.data for frame in self.frames)
        mimwrite(path, frame_data, format=Gif.FORMAT, **kwargs)
        return path


class Frame(object):
    def __init__(self, data, gif, index):
        self.data = data
        self.gif = gif
        self.index = index
        self.shape = self.data.shape[:2]

    def __iter__(self):
        for rgb_index in np.ndindex(self.data.shape[:-1]):
            self._rgb_index = rgb_index
            yield self.get_rgb(rgb_index)
        self._rgb_index = None

    def get_rgb(self, index=None):
        index = self._rgb_index if index is None else index
        return self.data[index]

    def set_rgb(self, val, index=None):
        index = self._rgb_index if index is None else index
        self.data[index] = val

    def has_next(self, after=1):
        return (self.index + after < len(self.gif.frames))

    def next(self, after=1):
        return self.gif.frames[self.index + after]

    def has_prev(self, after=1):
        return (self.index - after >= 0)

    def prev(self, after=1):
        return self.gif.frames[self.index - after]
