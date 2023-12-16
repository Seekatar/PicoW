# Raspberry Pi Pico W Tests

## Prerequisites

- MicroPython is installed on Pico
- Pico-W-Go VSCode extension is installed

Note the Pico uses the Raspberry RP2040 chip, often referred to as RP2.

## The App

main.py is the default file that is run on boot.  It is stored in the Pico's flash memory. It can be edited and saved from VSCode. The Pico will automatically reboot and run the new code.

The test listens on port 80 and has the following endpoints:

| Page          | Description                      |
| ------------- | -------------------------------- |
| /             | Displays LED status (True/False) |
| /light/on     | Turns LED on                     |
| /light/off    | Turns LED off                    |
| /light/toggle | Toggles LED                      |
| /exit         | Exits the app                    |

You can use the Arduino Serial monitor at 115200 baud to view the output of the print statements. On each request it will log out the HTTP request and variables.

## Using the Python REPL

1. Attach to the Serial Port, using Arduino Serial Monitor at 115200 baud, or something
2. Press Ctrl-C stop the app and enter REPL mode
3. In Arduino Serial Monitor, click `Toggle Terminal Mode`
4. Enter Python commands. For example:

    ```python
    # dump MicroPython version
    import sys
    sys.implementation
    ```

5. Press Ctrl-D to exit REPL mode and return to the app


## Links

- [RPi: Getting started with your Raspberry Pi Pico W](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
- [RPi: Pico W](https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html#raspberry-pi-pico-w)
- [RPi: MicroPython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
  - [RPi: MicroPython SDK Pdf](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
- [RPi: Pico W Pinout Pdf](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf)
- [MicroPython RP2 Quick Reference](https://docs.micropython.org/en/latest/rp2/quickref.html#hardware-spi-bus)
- [Element 14: VSCode and MicroPython for the Pi Pico](https://community.element14.com/products/raspberry-pi/b/blog/posts/vscode-and-micropython-for-the-pi-pico)