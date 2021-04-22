import Sensors
import Devices


class Room:

    # Creating the room
    def __init__(self, name, lamps=[], curtains=[], lightSensors=[], soundSensors=[], motionSensors=[]):
        self.name = name
        self.lamps = lamps
        self.curtains = curtains
        self.lightSensors = lightSensors
        self.soundSensors = soundSensors
        self.motionSensors = motionSensors

    # Method to return the room name
    def getName(self):
        return self.name

    # Method to return the array of lamps
    def getLamps(self):
        return self.lamps

    # Method to return the array of curtains
    def getCurtains(self):
        return self.curtains

    # Method to return the array of sensors
    def getSensors(self):
        return self.sensors

    # Method to find a specified lamp via ID
    def findLamp(self, lampID):
        # Looping through the array of lamps
        for i in self.lamps:
            # Checking if the specified ID matches the lamp ID
            if i.getID() == lampID:
                return i

        # Printing out an error message if the lamp could not be found
        print("Could not find specified lamp")

    # Method to find a specified curtain via ID
    def findCurtain(self, curtainID):
        # Looping through the array of curtains
        for i in self.curtains:
            # Checking if the specified ID matches the curtain ID
            if i.getID == curtainID:
                return i

        # Printing out an error message if the curtain could not be found
        print("Could not find specified curtain")

    # Method to find the specified sensor via ID
    def findSensor(self, sensorID):
        # Looping through the array of sensors
        for i in self.sensors:
            # Checking if the specified ID matches the sensor ID
            if i.getID == sensorID:
                return i

        # Printing out an error message if the sensor could not be found
        print("Could not find specified sensor")

    def getAllSensors(self):
        sensors = self.lightSensors+self.soundSensors+self.motionSensors
        return sensors

    def __str__(self):
        #empty string
        output = ""
        #add name
        output += "The name is " + self.name + "\n"
        #add lamp
        output += "The Lamp Details are " 
        for i in self.lamps:
            output += "ID: " + i.getID() + ", Activated: " + i.isActivated() + ", Colour: " + i.getColour() + ", Brightness: " + i.getBrightness() + "\n"
        #add curtain
        output += "The Curtain Details are " 
        for i in self.curtains:
            output += "ID: " + i.getID() + ", Closed: " + i.isClosed() + "\n"
        #add light sensor
        output += "The Light Sensor ID's are " 
        for i in self.lightSensors:
            output += "ID: " + i.getID() + ", Activated: " + i.isActivated() + ", Reading: " + i.getReading() + ", Threshhold: " + i.getThreshhold() + "\n"
        #add sound sensor
        output += "The Sound Sensor ID's are " 
        for i in self.soundSensors:
            output += "ID: " + i.getID() + ", Activated: " + i.isActivated() + ", Reading: " + i.getReading() + ", Threshhold: " + i.getThreshhold() + "\n"
        #add motion sensor
        output += "The Motion Sensor ID's are " 
        for i in self.motionSensors:
            #getReading is Activated, getValue is Reading
            output += "ID: " + i.getID() + ", Activated: " + i.getReading() + ", Reading: " + i.getValue() + ", Threshold: " +i.getThreshhold() + "\n"
        #return result of all
        return output

