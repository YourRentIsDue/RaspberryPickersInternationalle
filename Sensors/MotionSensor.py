from Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    NAME = "Motion Sensor"
    def __init__(self, id, location = None):
        Sensor.__init__(self, id, location)
        self.motion = 0
    def getReading(self):
        return self.motion