from .neopixel_access import neopixel_ring


def set_color(rgbw_dict):
    rgbw_tuple = (rgbw_dict['r'], rgbw_dict['g'], rgbw_dict['b'], rgbw_dict['w'])
    rgbw_tuple_rounded = [int(round(number)) for number in rgbw_tuple]

    neopixel_ring.set_color(rgbw_tuple_rounded)

def set_brightness(brightness):
    neopixel_ring.set_brightness(brightness)
