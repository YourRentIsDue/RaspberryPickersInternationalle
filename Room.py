class Room():
    def __init__(self, name, lamps = [], curtains = [], sensors = []):
        self.name = name
        self.lamps = lamps
        self.curtains = curtains
        self.sensors = sensors

    def getName(self):
        return self.name
    
    def getLamps(self):
        return self.lamps
    
    def getCurtains(self):
        return self.curtains
    
    def getSensors(self):
        return self.sensors
    
    def findLamp(self, lampID):
        for i in lamps:
            if i.getID() == lampID:
                return i
            
        print("Could not find specified lamp")

    def findCurtain(self, curtainID):
        for i in curtains:
            if i.getID == curtainID:
                return i

        print("Could not find specified curtain")
    
    def findSensor(self,sensorID):
        for i in sensors:
            if i.getID == sensorID:
                return i
        
        print("Could not find specified curtain")
