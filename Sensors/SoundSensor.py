from Sensors.Sensor import Sensor


class SoundSensor(Sensor):

    def __init__(self, id, location = None):
        Sensor.__init__(self, id, location)
        self.loudness = 0