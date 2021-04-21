from Sensors.Sensor import Sensor


class LightSensor(Sensor):
    NAME = "Light Sensor"

    def __init__(self, id, location=None, sheet=""):
        Sensor.__init__(self, id, location)

        if sheet is not None:
            self.sheet = sheet
            self.lux = self.sheet['B4'].value

    def getReading(self):
        return self.lux
