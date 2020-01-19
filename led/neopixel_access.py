import board
import neopixel

GPIO_PIN = board.D18
INIT_BRIGHTNESS = 0.05
NUMBER_OF_PIXEL = 16
ORDER = neopixel.GRBW


class NeopixelAccess:
    def __init__(self, gpio_pin=GPIO_PIN, number_of_pixels=NUMBER_OF_PIXEL):
        self.pixels = neopixel.NeoPixel(pin=gpio_pin, n=number_of_pixels, brightness=INIT_BRIGHTNESS, auto_write=False, pixel_order=ORDER)

    def set_brightness(self, brightness):
        self.pixels.brightness = brightness
        self.show()

    def set_color(self, rgbw):
        self.pixels.fill(rgbw)
        self.show()

    def show(self):
        self.pixels.show()


neopixel_ring = NeopixelAccess(GPIO_PIN, NUMBER_OF_PIXEL)