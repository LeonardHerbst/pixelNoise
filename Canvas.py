from PixelFiller import PixelFiller
from ColorPalette import ColorPalette
from colour import Color

class Canvas:

    def __init__(self, x, y):
        self.pixel_array = [[Color('#FFFFFF') for i in range(0, y)] for j in range(0, x)]

    def applyFiller(self, p_filler: PixelFiller, color_palette: ColorPalette) -> None:
        dimensions = self.getDimensions()
        for x in range(0, dimensions[0]):
            for y in range(0, dimensions[1]):
                self.pixel_array[x][y] =  p_filler.fill(color_palette)
    
    def getPixelArray(self) -> [[Color]]:
        return self.pixel_array

    def getDimensions(self) -> (int, int):
        return (len(self.pixel_array), len(self.pixel_array[0]))