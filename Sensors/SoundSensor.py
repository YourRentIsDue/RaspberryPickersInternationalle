from Sensors.Sensor import Sensor


class SoundSensor(Sensor):
    NAME = "Sound Sensor"
    MAX = 100  # db

    def __init__(self, id, location=None, value=0, thresh=50):
        Sensor.__init__(self, id, location, thresh)
        self.value = value

    def getReading(self):
        return self.value

    def setValue(self, value):
        self.value = value
