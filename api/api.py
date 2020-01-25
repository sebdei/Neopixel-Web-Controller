from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS

import led.neopixel_service as neopixel_service


app = Flask(__name__, static_folder="static", template_folder="static")


def bind_routes(app):
    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/get_brightness', methods=['GET'])
    def get_brightness():
        brightness = neopixel_service.get_brightness()
        return jsonify(brightness)

    
    @app.route('/get_color/hsl', methods=['GET'])
    def get_color_hsl():
        hsl = neopixel_service.get_color_hsl()

        return jsonify(**hsl)

    @app.route('/set_brightness', methods=['POST'])
    def set_brightness():
        body = request.get_json()
        neopixel_service.set_brightness(body)

        resp = make_response()

        return resp

    @app.route('/set_color', methods=['POST'])
    def set_color_rgbw():
        body = request.get_json()
        rgbw = body['rgbw']
        hsl = body['hsl']

        neopixel_service.set_color_rgbw(rgbw)
        neopixel_service.set_color_hsl(hsl)

        resp = make_response()
        return resp

def setup():
    # for development purpose
    CORS(app)

    bind_routes(app)
    app.run(host='0.0.0.0')
