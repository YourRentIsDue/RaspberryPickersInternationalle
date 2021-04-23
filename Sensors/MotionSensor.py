from Sensors.Sensor import Sensor


class MotionSensor(Sensor):
    NAME = "Motion Sensor"
    MAX = 100

    def __init__(self, id, location=None, thresh=50, value=0):
        Sensor.__init__(self, id, location, thresh)
        self.value = value

    def getReading(self):
        if self.value >= self.thresh:
            return True
        else:
            return False

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
