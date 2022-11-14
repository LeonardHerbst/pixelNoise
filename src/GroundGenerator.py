import sys

from BasicRandomFiller import *
from SpacialRandomFiller import *
from Canvas import *
from PngRenderer import PngRenderer
from Gui import Gui


class GroundGenerator:

    def __init__(self, x, y):
        self.canvas = Canvas(x, y)
    
    def generate_ground(self, p_filler: PixelFiller) -> None:
        self.canvas.apply_filler(p_filler)


def main() -> int:
    gg = GroundGenerator(1470, 595)  # (294, 119)
    color_palette = ColorPalette(Color("#874007"), Color("#743400"), Color("#81400c"), Color("#954e14"), Color("#a1561c"))
    color_palette_with_stone = ColorPalette(primary=Color('#bd7e4a'), darker=Color('#603800'),
                                            dark=Color('#83502e'), light=Color('#1f6d04'), lighter=Color('#bd7e4a'))
    test_palette = ColorPalette(primary=Color('#000'), darker=Color('#f00'),
                                dark=Color('#0f0'), light=Color('#00f'), lighter=Color('#fff'))
    gui = Gui()
    gui.start_gui(gg.canvas.pixel_array, color_palette, "gui_test")

    return 0


if __name__ == '__main__':
    sys.exit(main())





