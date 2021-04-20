from Sensors.Sensor import Sensor


class LightSensor(Sensor):
    NAME = "Light Sensor"
    def __init__(self, id, location = None, sheet = ""):
        Sensor.__init__(self, id, location)
        self.sheet = sheet
        self.lux = 0

    def getReading(self):
        #return self.sheet['B4'].value
        return self.lux
