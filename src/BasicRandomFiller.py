from ColorPalette import ColorPalette
from PixelFiller import PixelFiller
from colour import Color
import random


class BasicRandomFiller(PixelFiller):
    def __init__(self, seed):
        random.seed(seed)

    def fill(self, color_palette: ColorPalette) -> Color:
        return color_palette.get_color(random.randint(2, 4))
