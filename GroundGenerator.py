import numpy as np
from colour import Color
import png
import sys
import math
from time import sleep

from ColorPalette import *
from BasicRandomFiller import *
from PixelFiller import PixelFiller
from Canvas import *

class GroundGenerator:

    def __init__(self, x, y):
        self.canvas = Canvas(x, y)
    
    def generateGround(self, color_palette: ColorPalette, p_filler: PixelFiller) -> None:
        self.canvas.applyFiller(p_filler, color_palette)

    def render(self) -> None:
        png_palette = []
        dimensions = self.canvas.getDimensions()
        png_array = self.canvas.getPixelArray()
        for idx, row in enumerate(png_array):
            for idy, pixel in enumerate(row):
                if pixel not in png_palette:
                    png_palette.append(pixel)
                png_array[idx][idy] = png_palette.index(pixel)

        # the palette length might need to be a power of two idk
        # for i in range(0, math.ceil(math.log2(len(png_palette)))):
        #     png_palette.append(Color('#FFFFFF'))
    
        palette = [(int(255 * c.rgb[0]), int(255 * c.rgb[1]), int(255 * c.rgb[2])) for c in png_palette]
        bit_depth = max(1,math.ceil(math.log2(len(palette))))
        sleep(1)
        w = png.Writer(dimensions[1], dimensions[0], palette=palette, bitdepth=bit_depth)
        f = open('res.png', 'wb')
        w.write(f, png_array)

def main() -> int:
    gg = GroundGenerator(210, 140)
    color_palette = ColorPalette(Color('#8c3800'))
    br_filler = BasicRandomFiller(3)
    gg.generateGround(color_palette, br_filler)
    gg.render()

if __name__ == '__main__':
    sys.exit(main())
