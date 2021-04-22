class Sensor:
    
    def __init__(self, id, location=None):
        self.id = id
        self.location = location
        self.activated = True

    def getReading(self):
        return None

    def getID(self):
        return self.id

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location
    
    def setActivated(self, activated):
        self.activated = activated
