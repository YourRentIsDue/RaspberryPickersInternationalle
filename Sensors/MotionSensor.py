from Sensors.Sensor import Sensor


class MotionSensor(Sensor):

    def __init__(self, id, location):
        Sensor.__init__(self, id, location)