import hsl2rgbw from './hsl2rgbw.js'


window.onload = function () {
  setupBrightnessSlider()
  setupColorWheel()

  getCurrentLEDState()
}

function getCurrentLEDState() {
  const brightness = get('/get_brightness')
  const color = get('/get_color')

  console.log(brightness);
  console.log(color)
}

function setupBrightnessSlider() {
  const slider = document.getElementById("range-slider");

  slider.addEventListener('input', (event) => {
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

  colorPicker.on(["color:change"], (color) => {
    const hsl = color.hsl
    const rgbw = hsl2rgbw(hsl.h, hsl.s, hsl.l)
  
    setColor(rgbw)
  })
}

function setBrightness(brightness) {
  post('/set_brightness', brightness)
}

function setColor(rgbw) {
  post('/set_color_rgbw', rgbw)
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

function get(path) {
  const effectivePath = "http://192.168.0.32:5000" + path
  fetch(effectivePath, {
    method: 'GET',
    mode: 'cors',
    cache: 'no-cache',
  })
}