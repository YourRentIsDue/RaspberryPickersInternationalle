import Sensors
import Devices

class Room():

    #Creating the room
    def __init__(self, name, lamps = [], curtains = [], sensors = []):
        self.name = name
        self.lamps = lamps
        self.curtains = curtains
        self.sensors = sensors

    #Method to return the room name
    def getName(self):
        return self.name
    
    #Method to return the array of lamps
    def getLamps(self):
        return self.lamps
    
    #Method to return the array of curtains
    def getCurtains(self):
        return self.curtains
    
    #Method to return the array of sensors
    def getSensors(self):
        return self.sensors
    
    #Method to find a specified lamp via ID
    def findLamp(self, lampID):
        #Looping through the array of lamps
        for i in lamps:
            #Checking if the specified ID matches the lamp ID
            if i.getID() == lampID:
                return i
        
        #Printing out an error message if the lamp could not be found
        print("Could not find specified lamp")

    #Method to find a specified curtain via ID
    def findCurtain(self, curtainID):
        #Looping through the array of curtains
        for i in curtains:
            #Checking if the specified ID matches the curtain ID
            if i.getID == curtainID:
                return i

        #Printing out an error message if the curtain could not be found
        print("Could not find specified curtain")
    
    #Method to find the specified sensor via ID
    def findSensor(self,sensorID):
        #Looping through the array of sensors
        for i in sensors:
            #Checking if the specified ID matches the sensor ID
            if i.getID == sensorID:
                return i
        
        #Printing out an error message if the sensor could not be found
        print("Could not find specified sensor")
