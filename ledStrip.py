from rpi_ws281x import *
import colorsys

# LED strip configuration:
LED_COUNT = 150       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).

class LedStrip:
    def __init__(self):
        self.strip : PixelStrip = PixelStrip(LED_COUNT, LED_PIN)
        self.status : bool = False
        self.hue: float = 360
        self.saturation : float = 0
        self.brigthness : float = 1

    def turnOn(self):
        self.strip.setBrightness(255)
        self.strip.show()
        self.status = True

    def turnOff(self):
        self.strip.setBrightness(0)
        self.strip.show()
        self.status = False
    
    def setColor(self, hue, saturation, brigthness):
        self.hue = hue
        self.saturation = saturation
        self.brigthness = brigthness

    def getStatus(self):
        return 'on' if self.status else 'off'