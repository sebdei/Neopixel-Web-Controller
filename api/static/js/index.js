import hsl2rgbw from './hsl2rgbw.js'


window.onload = function () {
  setupBrightnessSlider()
  setupColorWheel()
}

function setupBrightnessSlider() {
  const slider = document.getElementById("range-slider");

  slider.addEventListener('input', function (event) {
    const effectiveBrightness = event.target.value / 100
    setBrightness(effectiveBrightness)
  })
}

function setupColorWheel() {
  const colorPicker = new iro.ColorPicker(".color-picker", {
    width: 280,
    color: { h: 180, s: 90, l: 50 },
    borderWidth: 1,
    borderColor: "#fff",
    layout: [
      {
        component: iro.ui.Wheel,
      }
    ]
  });


  const onColorChanged = function (color) {
    const hsl = color.hsl
    const rgbw = hsl2rgbw(hsl.h, hsl.s, hsl.l)

    setColor(rgbw)
  }

  colorPicker.on(["color:change"], onColorChanged)
}

function setBrightness(brightness) {
  post('/set_brightness', brightness)
}

function setColor(rgbw) {
  post('/set_color', rgbw)
}

function post(path, data) {
  const effectivePath = "http://192.168.0.32:5000" + path
  fetch(effectivePath, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
}