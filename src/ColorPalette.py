import random

from colour import Color


class ColorPalette:

    def __init__(self, primary, darker=None, dark=None, light=None, lighter=None):
        if darker is None:
            darker = Color(rgb=tuple(c * 0.7 for c in primary.rgb))
        if dark is None:
            dark = Color(rgb=tuple(c * 0.9 for c in primary.rgb))
        if light is None:
            light = Color(rgb=tuple((1 - c) * 0.1 + c for c in primary.rgb))
        if lighter is None:  
            lighter = Color(rgb=tuple((1 - c) * 0.3 + c for c in primary.rgb))
        self.p_colors = [darker, dark, primary, light, lighter]

    def shade(self, c: Color) -> Color:
        if c not in self.p_colors:
            raise ValueError("The color you are trying to shade "
                             "is not part of the palette. {} is not in {}".format(c, self.p_colors))
        index = self.p_colors.index(c)
        if index > 0:
            index -= 1
        return self.p_colors[index]

    def tint(self, c: Color) -> Color:
        if c not in self.p_colors:
            raise ValueError("The color you are trying to tint "
                             "is not part of the palette. {} is not in {}".format(c, self.p_colors))
        index = self.p_colors.index(c)
        if index < 4:
            index += 1
        return self.p_colors[index]

    def hsl_shade_or_tint(self, c: Color, value: float):
        hsl = c.hsl
        return Color(hsl=(hsl[0], hsl[1], hsl[2] + value))

    def get_color(self, i: int) -> Color:
        if i < 0 or i > 4:
            raise ValueError("Illegal index " + str(i) + "!")
        return self.p_colors[i]

    def get_rgb_list(self) -> [(int, int, int)]:
        return [(int(255 * c.rgb[0]), int(255 * c.rgb[1]), int(255 * c.rgb[2])) for c in self.p_colors]

    def get_color_index(self, c: Color) -> int:
        if c not in self.p_colors:
            raise ValueError("Color not in Palette!")
        else:
            return self.p_colors.index(c)

    def map_float_to_color(self, value: float) -> Color:
        if random.randint(0, 1):
            return self.shade(self.get_color(round(value * 4)))
        else:
            return self.tint(self.get_color(round(value * 4)))
        return self.hsl_shade_or_tint(self.get_color(round(value * 4)), random.randint(-1, 1)/50)

    def to_string(self):
        return 'Color("{2}"), Color("{0}"), Color("{1}"), Color("{3}"), Color("{4}")'.format(*[color for color in self.p_colors])
