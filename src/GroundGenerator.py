import math
import sys
from time import sleep

import png

from BasicRandomFiller import *
from SpacialAwareRandomFiller import *
from Canvas import *


class GroundGenerator:

    def __init__(self, x, y):
        self.canvas = Canvas(x, y)
    
    def generate_ground(self, color_palette: ColorPalette, p_filler: PixelFiller) -> None:
        self.canvas.apply_filler(p_filler, color_palette)

    def render(self, output: str) -> None:
        png_palette = []
        dimensions = self.canvas.get_dimensions()
        png_array = self.canvas.get_pixel_array()
        for idx, row in enumerate(png_array):
            for idy, pixel in enumerate(row):
                if pixel not in png_palette:
                    png_palette.append(pixel)
                png_array[idx][idy] = png_palette.index(pixel)

        # the palette length might need to be a power of two idk
        # for i in range(0, math.ceil(math.log2(len(png_palette)))):
        #     png_palette.append(Color('#FFFFFF'))
    
        palette = [(int(255 * c.rgb[0]), int(255 * c.rgb[1]), int(255 * c.rgb[2])) for c in png_palette]
        bit_depth = max(1, math.ceil(math.log2(len(palette))))
        print("Palette: {}\nBit_depth: {}".format(palette, bit_depth))
        # don't really know why the bit depth can only be 1, 2, 4, 8...
        w = png.Writer(dimensions[1], dimensions[0], palette=palette, bitdepth=8)
        f = open('../results/{}.png'.format(output), 'wb')
        w.write(f, png_array)


def main() -> int:
    gg = GroundGenerator(210, 140)
    color_palette = ColorPalette(Color('#8c3800'))
    br_filler = BasicRandomFiller(3)
    sar_filler = SpacialRandomFiller(3, 210, 140)
    gg.generate_ground(color_palette, sar_filler)
    gg.render("field_ground_210x140")
    gg.generate_ground(color_palette, br_filler)
    gg.render("basic_ground_210x140")

    return 0


if __name__ == '__main__':
    sys.exit(main())
