from typing import Tuple

import neopixel

INIT_BRIGHTNESS = 0.05


class NeopixelAccess:
    brightness = INIT_BRIGHTNESS
    hsl = None
    neo_pixels = None

    def __init__(self, gpio_pin=18, number_of_pixels=16, order=None):
        self.neo_pixels = neopixel.NeoPixel(pin=gpio_pin, n=number_of_pixels, brightness=INIT_BRIGHTNESS, auto_write=False, pixel_order=order)

    def get_brightness(self):
        return self.brightness

    def get_hsl(self):
        return self.hsl

    def get_neo_pixel_list(self):
        return self.neo_pixels

    def set_brightness(self, brightness: float):
        self.brightness = brightness

    def set_hsl(self, hsl: Tuple):
        self.hsl = hsl