import neopixel

INIT_BRIGHTNESS = 0.05


class NeopixelAccess:
    def __init__(self, gpio_pin=18, number_of_pixels=16, order=None):
        self.pixels = neopixel.NeoPixel(pin=gpio_pin, n=number_of_pixels, brightness=INIT_BRIGHTNESS, auto_write=False, pixel_order=order)

    def get_brightness(self):
        return self.pixels.brightness

    def get_color(self):
        return self.pixels[0]

    def set_brightness(self, brightness):
        self.pixels.brightness = brightness
        self.show()

    def set_color(self, rgbw):
        self.pixels.fill(rgbw)
        self.show()

    def show(self):
        self.pixels.show()