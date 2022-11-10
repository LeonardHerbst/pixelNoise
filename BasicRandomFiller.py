from ColorPalette import ColorPalette
from PixelFiller import PixelFiller
from colour import Color
import random


class BasicRandomFiller(PixelFiller):
    def __init__(self, seed):
        random.seed(seed)

    def fill(self, colorPalette: ColorPalette) -> Color:
        return colorPalette.getColor(random.randint(2, 4))