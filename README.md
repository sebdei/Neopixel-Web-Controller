Neopixel-Controller
==================

Simple web-based controller for [Adafruit's neopixel](https://www.adafruit.com/category/168) made for raspberry pis or similar SOCs.

Made with [Adafruit CircuitPython Neopixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel), [flask](https://github.com/pallets/flask) and [iro](iro.js.org/).



-------------------
`docker-compose up` starts up tiny flask server on the raspi. The Web-based Controller is then available at `http://<raspberry pi ip adresse>:5000`.

Calulation of HSL to RGB+W values are done on clientside due to the limited computing capacity of the PI. Special thanks to [SaikoLED](https://blog.saikoled.com/post/44677718712/how-to-convert-from-hsi-to-rgb-white)