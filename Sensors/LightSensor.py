from Sensors.Sensor import Sensor


class LightSensor(Sensor):
    NAME = "Light Sensor"
    MAX = 1000 #lux
    def __init__(self, id, location=None, value=None):
        Sensor.__init__(self, id, location)
        self.value = value

    def getReading(self):
        return self.value

    def setValue(self, value):
        self.value = value
