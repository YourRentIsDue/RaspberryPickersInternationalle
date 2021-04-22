from Room import Room
from random import randint
from Sensors import LightSensor, MotionSensor, SoundSensor
from Devices import Lamp, Curtain
from openpyxl import Workbook


class CreateObjects:

    def __init__(self):
        self.rooms = []
        self.wb = Workbook()
        self.sheet = self.wb.active

    def createSensors(self, noOfLight, noOfMotion, noOfSound):
        lightSensors = []
        motionSensors = []
        soundSensors = []

        for i in range(noOfLight):
            lightSensors.append(LightSensor.LightSensor(str(i + 1)))
        for i in range(noOfMotion):
            motionSensors.append(MotionSensor.MotionSensor(str(i + 1)))
        for i in range(noOfSound):
            soundSensors.append(SoundSensor.SoundSensor(str(i + 1)))

        if noOfLight > noOfMotion and noOfLight > noOfSound:
            biggest = noOfLight
        else:
            if noOfMotion > noOfLight and noOfMotion > noOfSound:
                biggest = noOfMotion
            else:
                biggest = noOfSound

        self.sheet['A1'] = "Room name:"

        counter = 2

        for i in range(biggest):
            self.sheet['A' + str(counter)] = "Light sensor ID:"
            counter += 1
            self.sheet['A' + str(counter)] = "Light level in lux:"
            counter += 1
            self.sheet['A' + str(counter)] = "Sound sensor ID:"
            counter += 1
            self.sheet['A' + str(counter)] = "Volume in dB:"
            counter += 1
            self.sheet['A' + str(counter)] = "Motion sensor ID:"
            counter += 1
            self.sheet['A' + str(counter)] = "Motion:"
            counter += 1
            self.sheet['A' + str(counter)] = ""
            counter += 1

        return lightSensors, motionSensors, soundSensors

    def createDevices(self, noOfLamps, noOfCurtains):
        lamps = []
        curtainss = []
        for i in range(noOfLamps):
            lamps.append(Lamp.Lamp(str(i)))
        for i in range(noOfCurtains):
            curtainss.append(Curtain.Curtain(str(i)))

        return lamps, curtainss

    def createRoom(self, noOfLight, noOfMotion, noOfSound, noOfLamps, noOfCurtains, roomName):
        lightSensors, motionSensors, soundSensors = self.createSensors(noOfLight, noOfMotion, noOfSound)
        lamps, curtainss = self.createDevices(noOfLamps, noOfCurtains)

        for lS in lightSensors:
            lS.setValue(randint(500, 1000))
            lS.setLocation(roomName)

        for mS in motionSensors:
            mS.setValue(randint(0, 100))
            mS.setLocation(roomName)

        for sS in soundSensors:
            sS.setValue(randint(30, 100)) 
            sS.setLocation(roomName)

        self.rooms.append(Room(roomName, lamps, curtainss, lightSensors, soundSensors, motionSensors))

        column = chr(65 + len(self.rooms) + 1)

        self.sheet[column + str(1)] = roomName

        counter = 0

        for lS in lightSensors:
            self.sheet[column + str(2 + counter * 7)] = lS.getID()
            self.sheet[column + str(3 + counter * 7)] = lS.getReading()
            counter += 1

        counter = 0

        for sS in soundSensors:
            self.sheet[column + str(4 + counter * 7)] = sS.getID()
            self.sheet[column + str(5 + counter * 7)] = sS.getReading()
            counter += 1

        counter = 0

        for mS in motionSensors:
            self.sheet[column + str(6 + counter * 7)] = mS.getID()
            self.sheet[column + str(7 + counter * 7)] = mS.getValue()
            counter += 1

        try:
            self.wb.save(filename="text.xlsx")
        except PermissionError:
            print("There was an error generating the data storage file, perhaps an old instance of the file is already "
                  "open?")

        return self.rooms
