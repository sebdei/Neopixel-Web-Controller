Neopixel-Controller
==================

Simple docker-based web controller for [Adafruit's neopixels](https://www.adafruit.com/category/168) made for raspberry pis and similar SOCs.

Built with [Adafruit CircuitPython Neopixel](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel), [flask](https://github.com/pallets/flask) and [iro](https://iro.js.org/).



--------------------------------------
`docker-compose up` starts up tiny flask server on the raspi. The web controller is then available at `http://<ip -adresse>:5000`.

Calculation of HSL to RGB+W values are done on clientside due to the limited computing capacity of the PI. Special thanks to [SaikoLED](https://blog.saikoled.com/post/44677718712/how-to-convert-from-hsi-to-rgb-white)


<img src="https://raw.githubusercontent.com/sebdei/Neopixel-Web-Controller/master/screenshot.png" width="50%">