from Sensors.Sensor import Sensor


class MotionSensor(Sensor):

    def __init__(self, id, location = None):
        Sensor.__init__(self, id, location)
        self.motion = 0