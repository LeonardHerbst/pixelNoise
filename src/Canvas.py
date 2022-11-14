from PixelFiller import PixelFiller
from ColorPalette import ColorPalette
from colour import Color


class Canvas:

    def __init__(self, x, y):
        self.pixel_array = [[0.0 for i in range(0, y)] for j in range(0, x)]

    def apply_filler(self, p_filler: PixelFiller) -> None:
        p_filler.fill(self.pixel_array)
    
    def get_pixel_array(self) -> [[float]]:
        return self.pixel_array

    def get_dimensions(self) -> (int, int):
        return len(self.pixel_array), len(self.pixel_array[0])
