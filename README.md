# pio_ws2812b

## MP3 audio

The firmware embeds `slow.mp3` in flash as `generated/slow_mp3.h` during the
CMake build. MP3 decoding and PWM playback run on core 1; the WS2812 animation
and button handling remain on core 0.

Connect the PAM8302 as follows:

- PAM8302 A+ to Pico GP0
- PAM8302 A- to Pico GND
- PAM8302 VIN to Pico 3V3
- PAM8302 GND to Pico GND
- PAM8302 speaker outputs to the speaker

From Git Bash, build with:

```sh
cmake --build build --target pio_ws2812 --parallel 4
```
