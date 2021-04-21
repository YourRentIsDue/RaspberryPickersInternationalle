import Sensors
import Devices
from openpyxl import load_workbook
loc = r'Sensors/Test-Data-1.xlsx'

wb = load_workbook(loc)
sheet = wb['Sheet2']

sensor1 = Sensors.LightSensor.LightSensor("Light_" + str(sheet['B3'].value), str(sheet['B2'].value), sheet)

print(sensor1.getReading())

