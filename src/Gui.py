from src.ColorPalette import ColorPalette
from src.SpacialRandomFiller import SpacialRandomFiller
from src.PngRenderer import PngRenderer
from colour import Color
from src.MatplotlibRenderer import MatplotlibRenderer

import dearpygui.dearpygui as dpg


class Gui:
    img_data = []
    tmp_color_palette: ColorPalette = ColorPalette(Color('#ffffff'))

    scale = 1
    octaves = 1
    persistence = 0.5
    lacunarity = 0.5
    repeatx = 210
    repeaty = 140
    base = 1
    offset = 0

    # setter and getter for parameters used by the specially aware random filler mostly there for convenience
    def set_params(self, params: (float, int, float, float, int, int, int, float)) -> None:
        Gui.scale, Gui.octaves, Gui.persistence, Gui.lacunarity, Gui.repeatx, Gui.repeaty, Gui.base, Gui.offset = params

    def get_params(self) -> (float, int, float, float, int, int, int, float):
        return Gui.scale, Gui.octaves, Gui.persistence, Gui.lacunarity, Gui.repeatx, Gui.repeaty, Gui.base, Gui.offset

    def combine_pixel_array_with_color_palette(self, pixel_array: [[float]], color_palette: ColorPalette) -> [float]:
        result = []
        for row in pixel_array:
            for pixel in row:
                for rgb_color_value in color_palette.map_float_to_color(pixel).rgb:
                    result.append(rgb_color_value)
                # alpha channel
                result.append(1.0)
        return result

    def start_gui(self, pixel_array: [[float]], color_palette: ColorPalette, output: str) -> None:
        self.config_revision = 0
        # DearPyGui setup
        dpg.create_context()

        # creating the filler which is to be configured
        srf = SpacialRandomFiller(pixel_array=pixel_array)
        # setting the params to the value hardcoded in the filler
        self.set_params(srf.get_params())
        self.set_params((3.3589999675750732, 2, 0.21899999678134918, 0.05900000035762787, 210, 140, 0, 0.7071067811865476))
        srf.fill(pixel_array)

        rgb_list = color_palette.get_rgb_list()

        # generating the data displayed by the gui
        Gui.img_data = self.combine_pixel_array_with_color_palette(pixel_array, color_palette)

        def go_callback(sender, data):
            Gui.scale = dpg.get_value("scale")
            Gui.octaves = dpg.get_value("octaves")
            Gui.persistence = dpg.get_value("persistence")
            Gui.lacunarity = dpg.get_value("lacunarity")
            Gui.base = dpg.get_value("base")
            darker = Color(rgb=(v/255 for v in list(dpg.get_value("darker"))[:3]))
            dark = Color(rgb=(v/255 for v in list(dpg.get_value("dark"))[:3]))
            primary = Color(rgb=(v/255 for v in list(dpg.get_value("primary"))[:3]))
            light = Color(rgb=(v/255 for v in list(dpg.get_value("light"))[:3]))
            lighter = Color(rgb=(v/255 for v in list(dpg.get_value("lighter"))[:3]))
            srf.set_params(self.get_params())
            srf.fill(pixel_array)
            Gui.tmp_color_palette = ColorPalette(primary, darker, dark, light, lighter)
            Gui.img_data = self.combine_pixel_array_with_color_palette(pixel_array, Gui.tmp_color_palette)
            dpg.set_value("texture_tag", Gui.img_data)

        def save_callback(sender, data):
            PngRenderer().render(pixel_array, Gui.tmp_color_palette, output)
            with open('../results/{}_config'.format(output), "w") as config_file:
                config_file.write(str(self.get_params()) + '\n')
                config_file.write(Gui.tmp_color_palette.to_string() + '\n')

        def save_as_new_config_callback(sender, data):
            with open('../results/{}_config_new_{}'.format(output, self.config_revision), "w") as config_file:
                config_file.write(str(self.get_params()) + '\n')
                config_file.write(Gui.tmp_color_palette.to_string() + '\n')
            self.config_revision += 1

        def matplotlib_callback(sender, data):
            MatplotlibRenderer().render(pixel_array, ColorPalette(Color('#ffffff')), "")

        with dpg.texture_registry(show=False):
            dpg.add_dynamic_texture(width=len(pixel_array[0]), height=len(pixel_array), default_value=Gui.img_data, tag="texture_tag")

        # setting up the gui
        with dpg.window(label="Garden Master Texture Creator", tag="main"):
            with dpg.group(horizontal=True, tag="main_group"):
                with dpg.group(tag="controls"):
                    dpg.add_slider_float(tag="scale", label="scale", min_value=0.0, max_value=20.0, default_value=Gui.scale)
                    dpg.add_slider_int(tag="octaves", label="octaves", min_value=1, max_value=10, default_value=Gui.octaves)
                    dpg.add_slider_float(tag="persistence", label="persistence", min_value=0.0, max_value=10.0, default_value=Gui.persistence)
                    dpg.add_slider_float(tag="lacunarity", label="lacunarity", min_value=0.0, max_value=10.0, default_value=Gui.lacunarity)
                    dpg.add_slider_int(tag="base", label="base", min_value=0, max_value=10, default_value=Gui.base)
                    dpg.add_color_edit(tag="darker", label="darker", default_value=rgb_list[0] + (1,))
                    dpg.add_color_edit(tag="dark", label="dark", default_value=rgb_list[1] + (1,))
                    dpg.add_color_edit(tag="primary", label="primary", default_value=rgb_list[2] + (1,))
                    dpg.add_color_edit(tag="light", label="light", default_value=rgb_list[3] + (1,))
                    dpg.add_color_edit(tag="lighter", label="lighter", default_value=rgb_list[4] + (1,))
                    with dpg.group(horizontal=True, tag="buttons"):
                        dpg.add_button(label="Go!", tag="go", callback=go_callback, width=200, height=40)
                        dpg.add_button(label="Save", tag="save", callback=save_callback, width=200, height=40)
                        dpg.add_button(label="Save new config", tag="save_as_new_config", callback=save_as_new_config_callback, width=200, height=40)
                        dpg.add_button(label="Matplotlib", tag="matplotlib", callback=matplotlib_callback, width=200, height=40)

                with dpg.group(tag="view"):
                    dpg.add_image("texture_tag", width=600, height=840)

        dpg.create_viewport(title='Custom Title', width=1920, height=1080)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main", True)
        dpg.start_dearpygui()
        dpg.destroy_context()
