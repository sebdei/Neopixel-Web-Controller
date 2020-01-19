import board
import neopixel
import time


pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRBW
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False, pixel_order=ORDER)

for i in range(-255):
    pixels.fill((i, 255-i, i, 255-i))
    pixels.show()

for i in range(255):
    pixels.fill((255-i, i, 255-i, i))
    pixels.show()
