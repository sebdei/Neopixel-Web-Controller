import hsl2rgbw from './hsl2rgbw.js'


window.onload = function () {
  setupBrightnessSlider()
  setupColorWheel()
}

async function setupBrightnessSlider() {
  const slider = document.getElementById("range-slider");

  const brightness = await get('/get_brightness')
  slider.value = brightness

  slider.addEventListener('input', (event) => {
    const effectiveBrightness = event.target.valueAsNumber
    setBrightness(effectiveBrightness)
  })
}

async function setupColorWheel() {
  const currentHsl = await get('/get_color/hsl')

  const colorPicker = new iro.ColorPicker(".color-picker", {
    width: 280,
    color: currentHsl,
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
  
    setColor(rgbw, hsl)
  })
}

function setBrightness(brightness) {
  post('/set_brightness', brightness)
}

function setColor(rgbw, hsl) {
  post('/set_color', { rgbw, hsl })
}

function post(path, body) {
  const effectivePath = "http://192.168.0.32:5000" + path
  fetch(effectivePath, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  })
}

async function get(path) {
  const effectivePath = "http://192.168.0.32:5000" + path
  const resp = await fetch(effectivePath, {
    method: 'GET',
    mode: 'cors',
    cache: 'no-cache',
  })
  const body = await resp.json()

  return body
}