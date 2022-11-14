from abc import ABC, abstractmethod
from ColorPalette import ColorPalette
from colour import Color


class PixelFiller(ABC):

    @abstractmethod
    def fill(self, pixel_array: [[Color]]) -> [[float]]:
        pass


