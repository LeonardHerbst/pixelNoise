import math

from ColorPalette import ColorPalette
from Renderer import Renderer
import png


class PngRenderer(Renderer):
    def render(self, pixel_array: [[float]], color_palette: ColorPalette, output: str) -> None:
        png_palette = []
        dimensions = (len(pixel_array), len(pixel_array[0]))

        palette = color_palette.get_rgb_list()

        bit_depth = math.pow(2, math.ceil(math.log2(len(palette))))
        png_array = [[color_palette.get_color_index(color_palette.map_float_to_color(pixel_array[x][y])) for y in range(dimensions[1])] for x in range(dimensions[0])]
        # print("Palette: {}\nBit_depth: {}".format(palette, bit_depth))
        # don't really know why the bit depth can only be 1, 2, 4, 8...
        w = png.Writer(dimensions[1], dimensions[0], palette=palette, bitdepth=bit_depth)
        f = open('../results/{}.png'.format(output), 'wb')
        w.write(f, png_array)
