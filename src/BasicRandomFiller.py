from ColorPalette import ColorPalette
from PixelFiller import PixelFiller
from colour import Color
import random


class BasicRandomFiller(PixelFiller):
    def __init__(self, seed):
        random.seed(seed)

    def fill(self, pixel_array: [[Color]]) -> [[float]]:
        for x in range(len(pixel_array)):
            for y in range(len(pixel_array[0])):
                pixel_array[x][y] = random.randint(2, 4) / 10
        return pixel_array
