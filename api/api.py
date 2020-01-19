from flask import Flask, render_template, make_response, request
from flask_cors import CORS

import led.neopixel_service as neopixel_service

app = Flask(__name__, static_folder="static", template_folder = "static")

def bind_routes(app):
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/set_brightness', methods=['POST'])
    def set_brightness():
        brightness = request.get_json()
        neopixel_service.set_brightness(brightness)
        
        resp = make_response()
        resp.status_code = 200
        return resp

    @app.route('/set_color_rgbw', methods=['POST'])
    def set_color():
        rgbw_dict = request.get_json()
        neopixel_service.set_color(rgbw_dict)
        
        resp = make_response()
        resp.status_code = 200
        return resp


def setup():
    # for development purpose
    CORS(app)

    bind_routes(app)
    app.run(host='0.0.0.0')