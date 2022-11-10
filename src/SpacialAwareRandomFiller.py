from ColorPalette import ColorPalette
from PixelFiller import PixelFiller
from colour import Color
import numpy as np


class SpacialRandomFiller(PixelFiller):
    def __init__(self, seed, x_size: int, y_size: int):
        # the filler needs to know the current position which cant be passed as an argument
        self.x, self.y = 0, 0
        self.x_size = x_size
        self.y_size = y_size

    def fill(self, color_palette: ColorPalette) -> Color:
        # interpolate between the colors based on self.x and apply some kind of noise
        return_color = Color('#161')
        self.advance()
        return return_color

    def advance(self):
        tmp = self.y
        self.y = (self.y + 1) % self.y_size
        self.x += (self.y < tmp)

