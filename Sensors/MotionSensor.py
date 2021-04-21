from Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    NAME = "Motion Sensor"

    def __init__(self, id, location=None, thresh=1, movement=0):
        Sensor.__init__(self, id, location)
        self.thresh = thresh
        self.movement = movement

    def getReading(self):
        if self.movement >= self.thresh:
            return True
        else:
            return False
