from Room import Room
from random import randint
from Sensors import LightSensor, MotionSensor, SoundSensor
from Devices import Lamp, Curtain
from openpyxl import Workbook


# creates random data and rooms
class CreateObjects:

    def __init__(self):
        self.rooms = []  # Creates an array to store rooms
        self.wb = Workbook()  # Creates an excel workbook object
        self.sheet = self.wb.active  # Creates a sheet object inside the workbook

    def createSensors(self, noOfLight, noOfMotion, noOfSound):  # creates sensors
        lightSensors = []
        motionSensors = []
        soundSensors = []

        for i in range(noOfLight):
            lightSensors.append(LightSensor.LightSensor(str(i + 1)))
        for i in range(noOfMotion):
            motionSensors.append(MotionSensor.MotionSensor(str(i + 1)))
        for i in range(noOfSound):
            soundSensors.append(SoundSensor.SoundSensor(str(i + 1)))

        if noOfLight > noOfMotion and noOfLight > noOfSound:  # Finds of which sensor there is the most
            biggest = noOfLight
        else:
            if noOfMotion > noOfLight and noOfMotion > noOfSound:
                biggest = noOfMotion
            else:
                biggest = noOfSound

        self.sheet['A1'] = "Room name:"  # Adds label for room name in the excel sheet

        counter = 2  # counter variable for loop

        for i in range(biggest):  # Creates labels for everything in the excel sheet
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

    def createDevices(self, noOfLamps, noOfCurtains):  # creates devices
        lamps = []
        curtainss = []
        for i in range(noOfLamps):
            lamps.append(Lamp.Lamp(str(i)))
        for i in range(noOfCurtains):
            curtainss.append(Curtain.Curtain(str(i)))

        return lamps, curtainss

    def createRoom(self, noOfLight, noOfMotion, noOfSound, noOfLamps, noOfCurtains, roomName):  # creates a room object
        lightSensors, motionSensors, soundSensors = self.createSensors(noOfLight, noOfMotion, noOfSound)  # creates
        # local arrays to store sensors, and calls the create sensors method
        lamps, curtainss = self.createDevices(noOfLamps, noOfCurtains)  # does same thing as above except for devices

        for lS in lightSensors:  # gives the light sensors a value and a location
            lS.setValue(randint(500, 1000))
            lS.setLocation(roomName)

        for mS in motionSensors:  # same as above except for motion
            mS.setValue(randint(0, 100))
            mS.setLocation(roomName)

        for sS in soundSensors:  # ^^
            sS.setValue(randint(30, 100))
            sS.setLocation(roomName)

        self.rooms.append(Room(roomName, lamps, curtainss, lightSensors, soundSensors, motionSensors))  # Creates a
        # room and appends it to the room array

        column = chr(65 + len(self.rooms) + 1)  # Calculates the correct column to put things in based on how many
        # rooms there are

        self.sheet[column + str(1)] = roomName  # Puts room name in excel sheet

        counter = 0  # counter variable for tracking row

        for lS in lightSensors:
            self.sheet[column + str(2 + counter * 7)] = lS.getID()  # Puts Light sensor id in the excel sheet
            self.sheet[column + str(3 + counter * 7)] = lS.getReading()  # puts Light sensor reading in excel sheet
            counter += 1

        counter = 0

        for sS in soundSensors:
            self.sheet[column + str(4 + counter * 7)] = sS.getID()  # same as above except for sound sensors
            self.sheet[column + str(5 + counter * 7)] = sS.getReading()  # ^^
            counter += 1

        counter = 0

        for mS in motionSensors:
            self.sheet[column + str(6 + counter * 7)] = mS.getID()
            self.sheet[column + str(7 + counter * 7)] = mS.getValue()  # ^^
            counter += 1

        try:
            self.wb.save(filename="text.xlsx")  # Tries to save the file as "test.xlsx"
        except PermissionError:  # If it encounters a Permission Error, the file is almost certainly open
            print("There was an error generating the data storage file, perhaps an old instance of the file is already "
                  "open?")

        return self.rooms  # Returns rooms
