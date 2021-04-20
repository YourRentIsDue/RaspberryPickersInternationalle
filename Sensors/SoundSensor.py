from Sensors.Sensor import Sensor


class SoundSensor(Sensor):
    NAME = "Sound Sensor"
    def __init__(self, id, location = None):
        Sensor.__init__(self, id, location)
        self.loudness = 0
    def getReading(self):
        return self.loudness