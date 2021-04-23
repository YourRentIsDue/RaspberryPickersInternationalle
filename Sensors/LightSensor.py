from Sensors.Sensor import Sensor


class LightSensor(Sensor):
    NAME = "Light Sensor"
    MAX = 1000  # lux

    def __init__(self, id, location=None, value=0, thresh=100):
        Sensor.__init__(self, id, location, thresh)
        self.value = value

    def getReading(self):
        return self.value

    def setValue(self, value):
        self.value = value
