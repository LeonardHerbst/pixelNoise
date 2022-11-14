from abc import ABC, abstractmethod
from ColorPalette import ColorPalette


class Renderer(ABC):

    @abstractmethod
    def render(self, pixel_array: [[float]], color_palette: ColorPalette, output: str) -> None:
        pass
