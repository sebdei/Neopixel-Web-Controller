from typing import Tuple

from .neopixel_access import NeopixelAccess

from config import GPIO_PIN, NUMBER_OF_PIXEL, ORDER

neopixel_ring = NeopixelAccess(GPIO_PIN, NUMBER_OF_PIXEL, ORDER)


def get_brightness():
    return neopixel_ring.get_brightness()


def set_brightness(brightness: float):
    neopixel_ring.get_neo_pixel_list().brigthness = brightness
    neopixel_ring.get_neo_pixel_list().show()

    neopixel_ring.set_brightness(brightness)


def set_color_rgbw(rgbw: Tuple):
    rgbw_rounded = [int(round(number)) for number in rgbw]
    neopixel_ring.get_neo_pixel_list().fill(rgbw_rounded)
    neopixel_ring.pixels.show()

    # neopixel_ring.setHsl(hsl)
