from Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    NAME = "Motion Sensor"

    def __init__(self, id, location=None, thresh=1, value=0):
        Sensor.__init__(self, id, location)
        self.thresh = thresh
        self.value = value

    def getReading(self):
        if self.value >= self.thresh:
            return True
        else:
            return False

    def setValue(self, value):
        self.value = value
