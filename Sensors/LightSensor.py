from Sensors.Sensor import Sensor


class LightSensor(Sensor):

    def __init__(self, id, location, sheet):
        Sensor.__init__(self, id, location)
        self.sheet = sheet

    def getReading(self):
        return self.sheet['B4'].value
