class LedStrip:
    def __init__(self):
        self.status : bool = 0 # Temp
        self.hue: float = 360
        self.saturation : float = 0
        self.brigthness : float = 1
    
    def setColor(self, hue, saturation, brigthness):
        self.hue = hue
        self.saturation = saturation
        self.brigthness = brigthness

    def getStatus(self):
        return 'on' if self.status else 'off'