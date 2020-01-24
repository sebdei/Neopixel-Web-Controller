export default function hsl2rgbw(hue, saturation_percentage, lightness_percentage) {
  const hueRadian = Math.PI * hue / 180

  const saturation = saturation_percentage / 100
  const lightness = lightness_percentage / 100

  const result = {}
  if (hueRadian < 2.09439) {
    const cosHue = Math.cos(hueRadian)
    const cos1047Hue = Math.cos(1.047196667 - hueRadian);

    result.r = saturation * 255 * lightness / 3 * (1 + cosHue / cos1047Hue);
    result.g = saturation * 255 * lightness / 3 * (1 + (1 - cosHue / cos1047Hue));
    result.b = 0;
    result.w = 255 * (1 - saturation) * lightness
  } else if (hueRadian < 4.188787) {
    const hueRadianSubstracted = hueRadian - 2.09439;
    const cosHue = Math.cos(hueRadianSubstracted);
    const cos1047Hue = Math.cos(1.047196667 - hueRadianSubstracted);

    result.r = 0;
    result.g = saturation * 255 * lightness / 3 * (1 + cosHue / cos1047Hue);
    result.b = saturation * 255 * lightness / 3 * (1 + (1 - cosHue / cos1047Hue));
    result.w = 255 * (1 - saturation) * lightness;
  } else {
    const hueRadianSubstracted = hueRadian - 4.188787;
    const cosHue = Math.cos(hueRadianSubstracted);
    const cos1047Hue = Math.cos(1.047196667 - hueRadianSubstracted);

    result.r = saturation * 255 * lightness / 3 * (1 + (1 - cosHue / cos1047Hue));
    result.g = 0;
    result.b = saturation * 255 * lightness / 3 * (1 + cosHue / cos1047Hue);
    result.w = 255 * (1 - saturation) * lightness;
  }

  return result
}
