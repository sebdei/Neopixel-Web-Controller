from typing import Dict, Tuple

from .neopixel_access import NeopixelContainer

from config import GPIO_PIN, NUMBER_OF_PIXEL, ORDER

neopixel_ring = NeopixelContainer(GPIO_PIN, NUMBER_OF_PIXEL, ORDER)


def get_brightness():
    return neopixel_ring.get_brightness()

def get_color_hsl():
    return neopixel_ring.get_hsl()

def set_brightness(brightness: float):
    neopixel_ring.get_neo_pixel_list().brightness = brightness
    neopixel_ring.get_neo_pixel_list().show()

    neopixel_ring.set_brightness(brightness)

def set_color_hsl(hsl: Dict):
    neopixel_ring.set_hsl(hsl)

def set_color_rgbw(rgbw: Dict):
    rgbw_tuple = rgbw['r'], rgbw['g'], rgbw['b'], rgbw['w']
    rgbw_rounded = [int(round(number)) for number in rgbw_tuple]

    neopixel_ring.get_neo_pixel_list().fill(rgbw_rounded)
    neopixel_ring.get_neo_pixel_list().show()
