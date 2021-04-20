class Sensor:

    def __init__ (self, id, location = None):
        self.id = id
        self.location = location

    def getReading(self):
        return None
    
    def getID(self):
        return self.id
    
    def getLocation(self):
        return self.location