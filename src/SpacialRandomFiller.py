from ColorPalette import ColorPalette
from PixelFiller import PixelFiller
import noise
from colour import Color
import math


class SpacialRandomFiller(PixelFiller):

    def __init__(self, pixel_array: [[float]]):
        self.x_size, self.y_size = len(pixel_array), len(pixel_array[0])
        self.scale       = 20
        self.octaves     = 2
        self.persistence = 0.25
        self.lacunarity  = 7.0
        self.repeatx     = 210
        self.repeaty     = 140
        self.base        = 0
        self.offset      = math.sqrt(2)/2

    def fill(self, pixel_array: [[float]]) -> [[float]]:
        for x in range(len(pixel_array)):
            for y in range(len(pixel_array[0])):
                noise_value = noise.pnoise2(
                                x / self.scale, y / self.scale,
                                octaves=self.octaves,
                                persistence=self.persistence,
                                lacunarity=self.lacunarity,
                                repeatx=self.repeatx,
                                repeaty=self.repeaty,
                                base=self.base)
                pixel_array[x][y] = (noise_value + self.offset) / (2 * self.offset)
        return pixel_array

    def set_params(self, params: (float, int, float, float, int, int, int, float)) -> None:
        self.scale, self.octaves, self.persistence, self.lacunarity,  self.repeatx, self.repeaty, self.base, self.offset = params

    def get_params(self) -> (float, int, float, float, int, int, int, float):
        return self.scale, self.octaves, self.persistence, self.lacunarity, self.repeatx, self.repeaty, self.base, self.offset

