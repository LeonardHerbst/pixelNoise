import math

from Renderer import Renderer
import noise
import numpy as np
import matplotlib.pyplot as plt

from src.ColorPalette import ColorPalette


class MatplotlibRenderer(Renderer):

    def render(self, pixel_array: [[float]], color_palette: ColorPalette, output: str) -> None:
        plt.imshow(pixel_array, cmap='gray')
        plt.colorbar()
        plt.show()
