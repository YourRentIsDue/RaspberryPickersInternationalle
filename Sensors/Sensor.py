class Sensor:

    def __init__(self, id, location=None, thresh = 0):
        self.id = id
        self.location = location
        self.activated = True
        self.thresh = thresh
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
    def setThreshhold(self, value):
        self.thresh = int(value)
    

    def isActivated(self):
        return self.activated

    def getThreshhold(self):
        return self.thresh

