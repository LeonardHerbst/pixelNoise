from colour import Color

class ColorPalette:

    def __init__(self, primary, darker=None, dark=None, light=None, lighter=None):
        if darker is None:
            darker = Color(rgb=tuple((1 - c) * 0.7 + c for c in primary.rgb))
        if dark is None:
            dark = Color(rgb=tuple((1 - c) * 0.9 + c for c in primary.rgb))
        if light is None:
            light = Color(rgb=tuple(c * 0.9 for c in primary.rgb))
        if lighter is None:  
            lighter = Color(rgb=tuple(c * 0.7 for c in primary.rgb))
        self.p_colors = [darker, dark, primary, light, lighter]
    
    def shade(self, c: Color) -> Color:
        if color not in p_colors:
            raise ValueError("The color you are trying to shade is not part of the palette. {} is not in {}".format(c, p_colors))
        index = p_colors.index(c)
        if index > 0:
            index -= 1
        return p_colors[index]

    def tint(self, c: Color) -> Color:
        if color not in p_colors:
            raise ValueError("The color you are trying to tint is not part of the palette. {} is not in {}".format(c, p_colors))
        index = p_colors.index(c)
        if index < 4:
            index += 1
        return p_colors[index]

    def getColor(self, i: int) -> Color:
        if i < 0 or i > 4:
            raise ValueError("Illegal index!")
        return self.p_colors[i]