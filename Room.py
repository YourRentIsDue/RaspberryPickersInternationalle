class Room():
    def __init__(self, name, lamps = [], curtains = [], sensors = []):
        self.name = name
        self.lamps = lamps
        self.curtains = curtains
        self.sensors = sensors

    def getName():
        return self.name
    
    def getLamps():
        return self.lamps
    
    def getCurtains():
        return self.curtains
    
    def getSensors():
        return self.sensors
    
    def findLamp(lampID):
        for i in lamps:
            if i.getID() == lampID:
                return i
            
        print("Could not find specified lamp")

    def findCurtain(curtainID):
        for i in curtains:
            if i.getID == curtainID:
                return i

        print("Could not find specified curtain")
    
    def findSensor(sensorID):
        for i in sensors:
            if i.getID == sensorID:
                return i
        
        print("Could not find specified curtain")
