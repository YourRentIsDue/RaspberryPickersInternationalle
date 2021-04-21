from Sensors.Sensor import Sensor


class SoundSensor(Sensor):
    NAME = "Sound Sensor"

    def __init__(self, id, location=None, value=0):
        Sensor.__init__(self, id, location)
        self.value = value

    def getReading(self):
        return self.value

    def setValue(self, value):
        self.value = value
