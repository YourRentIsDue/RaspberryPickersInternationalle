import xlrd

from Sensor import Sensor

class LightSensor(Sensor):

    def getReading(self):
        loc = ("")
        wb = xlrd.open_workbook()
        return