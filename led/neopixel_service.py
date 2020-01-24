from typing import Tuple

from .neopixel_access import NeopixelAccess

from config import GPIO_PIN, NUMBER_OF_PIXEL, ORDER

neopixel_ring = NeopixelAccess(GPIO_PIN, NUMBER_OF_PIXEL, ORDER)


def __fill_color(rgbw: Tuple):
    neopixel_ring.pixels.fill(rgbw)
    neopixel_ring.pixels.show()

    # neopixel_ring.setHsl(hsl)


def get_brightness():
    return neopixel_ring.get_brightness()


def get_color():
    return neopixel_ring.get_color()


def set_brightness(brightness: float):
    neopixel_ring.brightness = brightness


def set_color_rgbw(rgbw: Tuple):
    rgbw_rounded = [int(round(number)) for number in rgbw]
    __fill_color(rgbw_rounded)