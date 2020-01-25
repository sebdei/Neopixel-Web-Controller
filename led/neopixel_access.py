from typing import Tuple
from typing import Dict

import neopixel

INIT_BRIGHTNESS = 0.05
INIT_HSL = { 'h': 150, 's': 90, 'l': 50 }

class NeopixelContainer:
    __brightness = INIT_BRIGHTNESS
    __hsl = INIT_HSL
    __neo_pixels = None

    def __init__(self, gpio_pin=18, number_of_pixels=16, order=None):
        self.__neo_pixels = neopixel.NeoPixel(pin=gpio_pin, n=number_of_pixels, brightness=INIT_BRIGHTNESS, auto_write=False, pixel_order=order)

    def get_brightness(self):
        return self.__brightness

    def get_hsl(self):
        return self.__hsl

    def get_neo_pixel_list(self):
        return self.__neo_pixels

    def set_brightness(self, brightness: float):
        self.__brightness = brightness

    def set_hsl(self, hsl: Dict):
        self.__hsl = hsl
