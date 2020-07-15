from flask import Flask
from ledStrip import LedStrip

app: Flask = Flask(__name__)


@app.route('/')
def index():
    return 'LedStrip Servere is running'


@app.route('/color/<hue>/<saturation>/<brightness>')
def setColor(hue, saturation, brightness):
    currentHue = float(hue)
    currentSaturation = float(saturation)/100
    currentBrightness = float(brightness)/100
    ledStrip.setColor(currentHue,saturation,brightness)
    return 'Hue {}, Saturation {}, Brigthness {}'.format(hue, saturation, brightness)
    
# general LED functions
@app.route('/led/on')
def ledOn():
    ledStrip.status = True
    return 'LED is now on'


@app.route('/led/off')
def ledOff():
    ledStrip.status = False
    return 'LED is now off'


@app.route('/led/status')
def ledStatus():
    return 'Current LED Status is: {}'.format(ledStrip.getStatus())


# HUE functions
@app.route('/led/hue/get')
def getHue():
    return 'Current Hue is: {}'.format(ledStrip.hue)


@app.route('/led/hue/set/<hue>')
def setHue(hue):
    ledStrip.hue = hue
    return 'Hue is now set to: {}'.format(hue)


# Saturation functions
@app.route('/led/saturation/get')
def getSaturation():
    return 'Current Saturation is: {}'.format(ledStrip.saturation)


@app.route('/led/saturation/set/<saturation>')
def setSaturation(saturation):
    ledStrip.saturation = saturation
    return 'Saturation is now set to: {}'.format(saturation)


# Brightness functions
@app.route('/led/brigthness/get')
def getBrightness():
    return 'Current Brigthness is: {}'.format(ledStrip.brigthness)


@app.route('/led/brigthness/set/<saturation>')
def setBrigthness(brigthness):
    ledStrip.brigthness = brigthness
    return 'Brigthness is now set to: {}'.format(brigthness)


if __name__ == "__main__":
    ledStrip = LedStrip()
    app.run(debug=True, host='0.0.0.0', port=8080)
