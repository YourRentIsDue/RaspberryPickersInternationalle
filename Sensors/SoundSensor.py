from Sensors.Sensor import Sensor


class SoundSensor(Sensor):
    NAME = "Sound Sensor"

    def __init__(self, id, location=None, loudness=0):
        Sensor.__init__(self, id, location)
        self.loudness = loudness

    def getReading(self):
        return self.loudness
