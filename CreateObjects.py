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
        self.biggest = 0

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

        return lightSensors, motionSensors, soundSensors

    def createDevices(self, noOfLamps, noOfCurtains):  # creates devices
        lamps = []
        curtainss = []
        for i in range(noOfLamps):
            lamps.append(Lamp.Lamp(str(i + 1)))
        for i in range(noOfCurtains):
            curtainss.append(Curtain.Curtain(str(i + 1)))

        return lamps, curtainss

    def populateWorksheet(self, room, roomNumber):
        self.sheet['A1'] = "Room name:"  # Adds label for room name in the excel sheet

        if len(room.lightSensors) > len(room.motionSensors) and len(room.lightSensors) > len(room.soundSensors):
            # there is the most
            biggest = len(room.lightSensors)
        else:
            if len(room.motionSensors) > len(room.lightSensors) and len(room.motionSensors) > len(room.soundSensors):
                biggest = len(room.motionSensors)
            else:
                biggest = len(room.soundSensors)

        if len(room.lamps) > biggest:
            biggest = len(room.lamps)
        else:
            biggest = len(room.curtains)

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
            self.sheet['A' + str(counter)] = "Lamp ID:"
            counter += 1
            self.sheet['A' + str(counter)] = "Brightness:"
            counter += 1
            self.sheet['A' + str(counter)] = "R:"
            counter += 1
            self.sheet['A' + str(counter)] = "G:"
            counter += 1
            self.sheet['A' + str(counter)] = "B:"
            counter += 1
            self.sheet['A' + str(counter)] = "Curtains ID : "
            counter += 1
            self.sheet['A' + str(counter)] = ""
            counter += 1

        column = chr(65 + roomNumber + 1)  # Calculates the correct column number for the room

        self.sheet[column + str(1)] = room.getName()  # put the room name where it's supposed to go

        counter = 0  # counter back to 0

        for lS in room.lightSensors:
            self.sheet[column + str(2 + counter * 13)] = lS.getID()  # Puts Light sensor id in the excel sheet
            self.sheet[column + str(3 + counter * 13)] = lS.getReading()  # puts Light sensor reading in excel sheet
            counter += 1

        counter = 0

        for sS in room.soundSensors:
            self.sheet[column + str(4 + counter * 13)] = sS.getID()  # same as above except for sound sensors
            self.sheet[column + str(5 + counter * 13)] = sS.getReading()  # ^^
            counter += 1

        counter = 0

        for mS in room.motionSensors:
            self.sheet[column + str(6 + counter * 13)] = mS.getID()
            self.sheet[column + str(7 + counter * 13)] = mS.getValue()  # ^^
            counter += 1

        counter = 0

        for lamp in room.lamps:
            self.sheet[column + str(8 + counter * 13)] = lamp.getID()  # ^^
            counter += 1

        counter = 0

        for curtain in room.curtains:
            self.sheet[column + str(13 + counter * 13)] = curtain.getID()  # ^^
            counter += 1

        try:
            self.wb.save(filename="test.xlsx")  # Tries to save the file as "test.xlsx"
        except PermissionError:  # If it encounters a Permission Error, the file is almost certainly open
            print("There was an error generating the data storage file, perhaps an old instance of the file is already "
                  "open?")

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

        counter = 1

        for room in self.rooms:
            self.populateWorksheet(room, counter)

        return self.rooms  # Returns rooms
