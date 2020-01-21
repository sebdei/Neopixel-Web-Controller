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
        return jsonify(brightness=brightness)

    @app.route('/get_color', methods=['GET'])
    def get_color():
        r, g, b, w = neopixel_service.get_color()
        return jsonify(r=r, g=g, b=b, w=w)

    @app.route('/set_brightness', methods=['POST'])
    def set_brightness():
        brightness = request.get_json()
        neopixel_service.set_brightness(brightness)

        resp = make_response()
        return resp

    @app.route('/set_color_rgbw', methods=['POST'])
    def set_color():
        rgbw_dict = request.get_json()
        neopixel_service.set_color(rgbw_dict)

        resp = make_response()
        return resp


def setup():
    # for development purpose
    CORS(app)

    bind_routes(app)
    app.run(host='0.0.0.0')
