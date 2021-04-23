import Sensors
import Devices
import datetime


class Room:
    # Creating the room
    def __init__(self, name, lamps=[], curtains=[], lightSensors=[], soundSensors=[], motionSensors=[]):
        self.name = name
        self.lamps = lamps
        self.curtains = curtains
        self.lightSensors = lightSensors
        self.soundSensors = soundSensors
        self.motionSensors = motionSensors
        self.motionActivateTime = 0
        self.nightTimeStart = 20 #hour
        self.nightTimeEnd = 7 #hour
        
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
    def checkSensors(self,curTime):

        test =1
        #if nighttime
        if curTime.hour > self.nightTimeStart or curTime.hour < self.nightTimeEnd:
            #check for movement
            for m in self.motionSensors:
                if m.activated:
                    if m.getReading() == True:
                        for lamp in self.lamps:
                            lamp.activated = True
                        self.motionActivateTime = curTime
            #if clap
            for s in self.soundSensors:
                if s.activated:
                    if s.getReading() >= s.getThreshhold():
                        for lamp in self.lamps:
                            #if lights on turn off, if off then on
                            if lamp.activated:
                                lamp.activated = False
                            else:
                                lamp.activated = True
            
            #turn off lights if no movement for certain amount of time
            #could not think how to fix this 
            #if self.motionActivateTime != 0 and curTime - self.motionActivateTime < 500:
            #    for lamp in self.lamps:
            #        lamp.activated = False

            #close curtains
            for c in self.curtains:
                c.closed = True
        #if daytime
        else:
            #i apologise for the redundency i am very tired
            #open the curtains
            for c in self.curtains:
                c.closed = False
            #check it's not light enough    
            for l in self.lightSensors:
                if l.activated:
                    if l.getReading() <= l.getThreshhold():
                        #check for movement
                        for m in self.motionSensors:
                            if m.activated:
                                if m.getReading() == True:
                                    for lamp in self.lamps:
                                        lamp.activated = True
                                    self.motionActivateTime = curTime
                        #if clap
                        for s in self.soundSensors:
                            if s.activated:
                                if s.getReading() >= s.getThreshhold():
                                    for lamp in self.lamps:
                                        #if lights on turn off, if off then on
                                        if lamp.activated:
                                            lamp.activated = False
                                        else:
                                            lamp.activated = True
                        
                        #turn off lights if no movement for certain amount of time
                        #could not think how to fix this 
                        #if self.motionActivateTime != 0 and curTime - self.motionActivateTime < 500:
                        #    for lamp in self.lamps:
                        #        lamp.activated = False



    def __str__(self):
        #empty string
        output = ""
        #add name
        output += "The name is " + self.name + "\n"
        #add lamp
        output += "The Lamp Details are " 
        for i in self.lamps:
            output += "ID: " + str(i.getID()) + ", Activated: " + str(i.isActivated()) + ", Colour: " + str(i.getColour()) + ", Brightness: " + str(i.getBrightness()) + "\n"
        #add curtain
        output += "The Curtain Details are " 
        for i in self.curtains:
            output += "ID: " + str(i.getID()) + ", Closed: " + str(i.isClosed()) + "\n"
        #add light sensor
        output += "The Light Sensor ID's are " 
        for i in self.lightSensors:
            output += "ID: " + str(i.getID()) + ", Activated: " + str(i.isActivated()) + ", Reading: " + str(i.getReading()) + ", Threshhold: " + str(i.getThreshhold()) + "\n"
        #add sound sensor
        output += "The Sound Sensor ID's are " 
        for i in self.soundSensors:
            output += "ID: " + str(i.getID()) + ", Activated: " + str(i.isActivated()) + ", Reading: " + str(i.getReading()) + ", Threshhold: " + str(i.getThreshhold()) + "\n"
        #add motion sensor
        output += "The Motion Sensor ID's are " 
        for i in self.motionSensors:
            #getReading is Activated, getValue is Reading
            output += "ID: " + str(i.getID()) + ", Activated: " + str(i.getReading()) + ", Reading: " + str(i.getValue()) + ", Threshold: " + str(i.getThreshhold()) + "\n"
        #return result of all
        return output

